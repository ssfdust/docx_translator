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
        self.full_text_list = list()

    def qu(self, tag):
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

        header_xmls = 'word/header[0-9]*.xml'
        for fname in filelist:
            if re.match(header_xmls, fname):
                self.files_ch.add(fname)
                self.xml = self.zf_in.read(fname)
                self.full_text_list.append(self.get_text_list(self.xml))

        doc_xml = 'word/document.xml'
        self.xml = zf_in.read(doc_xml)
        self.full_text_list.append(self.get_text_list(self.xml))

        footer_xmls = 'word/footer[0-9]*.xml'
        for fname in filelist:
            if re.match(footer_xmls, fname):
                self.files_ch.add(fname)
                self.xml = self.zf_in.read(fname)
                self.full_text_list.append(self.get_text_list(self.xml))

    def replace_docx(self, replacment=None):
        """
        replace the 

        :replacment: TODO
        :returns: TODO

        """
        i = 0
        filelist = self.zf_in.namelist()

        header_xmls = 'word/header[0-9]*.xml'
        for fname in filelist:
            if re.match(header_xmls, fname):
                self.files_ch.add(fname)
                self.xml = self.zf_in.read(fname)

        doc_xml = 'word/document.xml'
        self.xml = zf_in.read(doc_xml)
        self.full_text_list.append(self.get_text_list(self.xml))

        footer_xmls = 'word/footer[0-9]*.xml'
        for fname in filelist:
            if re.match(footer_xmls, fname):
                self.files_ch.add(fname)
                self.xml = self.zf_in.read(fname)
                self.full_text_list.append(self.get_text_list(self.xml))
