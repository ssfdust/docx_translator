import tempfile
from zipfile import ZipFile, ZIP_DEFLATED
from xml.etree import ElementTree as ET
import re

class docxrpls(object):

    """Docstring for docxrpls. """

    def __init__(self, filename):
        """TODO: to be defined1. """
        self.nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        self.xml = ""
        self._docxfile = filename
        self.zf_in = None
        self.zf_out = None
        self.files_ch = set()
        self.changed = ""
        self.full_text_list = list()
        self.read_docx()

    def qn(self, tag):
        """
        Stands for 'qualified name', a utility function to turn a namespace
        prefixed tag name into a Clark-notation qualified tag name for lxml. For
        example, ``qn('p:cSld')`` returns ``'{http://schemas.../main}cSld'``.
        Source: https://github.com/python-openxml/python-docx/
        """
        prefix, tagroot = tag.split(":")
        uri = self.nsmap[prefix]
        return '{{{}}}{}'.format(uri, tagroot)

    def get_text_list(self):
        """
        get the text from the docx file and turn them
        into the list format.

        Source:https://github.com/ankushshah89/python-docx2txt/blob/master/docx2txt/docx2txt.py
        :returns: TODO

        """
        text_list = []
        root = ET.fromstring(self.xml)
        for child in root.iter():
            if child.tag == self.qn('w:t'):
                t_text = child.text
                text_list.append(t_text if t_text is not None else "")

        return text_list

    def read_docx(self):
        """
        replace the source text

        """
        self.zf_in = ZipFile(self._docxfile)
        filelist = self.zf_in.namelist()

        doc_xml = 'word/document.xml'
        self.xml = self.zf_in.open(doc_xml).read()
        self.full_text_list = self.get_text_list()

    def replace_docx(self, replacment=None):
        """
        replace the document

        :replacment: TODO
        :returns: TODO

        """
        doc_xml = 'word/document.xml'
        self.xml = self.zf_in.read(doc_xml)
        self.replace_text(replacment)

    def replace_text(self, r):
        """
        replace the contenct with replacement

        :r: the replacement list
        :returns: TODO

        """
        root = ET.fromstring(self.xml)
        r_copy = r.copy()
        try:
            for child in root.iter():
                if child.tag == self.qn('w:t') and child.text == r_copy[0][0]:
                    #it is one-to-one correspondence
                    child.text = r_copy[0][1]
                    r_copy.pop(0)
        except:
            print("the replacement doesn't match")
        finally:
            self.changed = ET.tostring(root).decode('utf-8')

    def create_new_file(self, newfilename):
        """
        with the changed content to build a new file

        :newfilename: the new file name
        :returns: TODO

        """
        all_file = set(self.zf_in.namelist())
        doc_xml = 'word/document.xml'
        doc_xml_set = {'word/document.xml'}
        file_to_copy = all_file - doc_xml_set 
        print(file_to_copy)

        self.zf_out = ZipFile(newfilename, mode="w", compression=self.zf_in.compression)
        self.zf_out.writestr(doc_xml, self.changed.encode('utf-8'))

        for fname in file_to_copy:
            self.zf_out.writestr(fname, self.zf_in.open(fname).read(), compress_type=ZIP_DEFLATED)
        
        print(self.zf_out.namelist())

    def close(self):
        self.zf_in.close()
        self.zf_out.close()

