from django.shortcuts import render
from translation import models
from translation.regandtrans.stutter import Stutter
from translation.regandtrans.translatorbysimulate import BingTranslator
from translation.regandtrans.translatorbysimulate import GoogleTranslator
from translation.docxreplace.docxrpls import docxrpls
from django.http import JsonResponse
from hashlib import md5
from django.core.files.base import ContentFile

import os
import logging
import json

# Create your views here.

class catalog_handle(object):

    """Docstring for newtable. """

    def __init__(self, catalog):
        """TODO: to be defined1.

        :catalog: catalog name

        """
        self._catalog = catalog
        self.catalog_hash = self.get_catalog_hash()
        self.id = self.get_id(self.catalog_hash)
        self.storage_id = self.get_storage_id(self.id)
        self.storage_table = self.get_storage_table()

    def get_catalog_hash(self):
        """get the hash of catalog name
        :returns: a md5 hash from catalog name

        """
        md5_handle = md5()
        encode_catalog = self._catalog.encode(encoding='utf-8')
        md5_handle.update(encode_catalog)
        md5_value = md5_handle.hexdigest()
        return md5_value

    def get_id(self, md5_value):
        """get the stroge id from the md5 md5_value

        :md5_value: the md5 value from the catalog
        :returns: integer number

        """
        cut = md5_value[-7:]
        id = int(cut, base=16)
        return id

    def get_storage_id(self, id):
        """get the storage id from id

        :id: catalog id
        :returns: a number from 0 to 100

        """
        storage_id = id % 100
        return "%03d" % storage_id

    def get_storage_table(self):
        """TODO: Docstring for create_or_get.

        :storage_id: the storage id used by daatabase 
        :returns: create success or the info

        """
        table = getattr(models, "catalog_" + self.storage_id)
        return table

    def create_or_get(self):
        """insert a new line with current id and 
        catalog name if this catalog is not existed

        :id: the catalog id
        :returns: create success or not

        """
        id = self.id
        catalog_id_table = getattr(models, "catalog_ids")
        (ret, state) = catalog_id_table.objects.get_or_create(id=id, catalog=self._catalog)
        return state

    def insert_pairs(self, src_word, tar_word):
        """insert source word and target word pairs.

        :storage_table: the storage table object
        :src_word: the source word which needs to be changed
        :tar_word: the target word which is changed from the source word
        :returns: true or false

        """
        storage_table = self.storage_table
        (ret, state) = storage_table.objects.get_or_create(id=self.id, src_word=src_word,tar_word=tar_word)
        return state

    def get_tar_word(self, src_word):
        """get the target word from database with the source word

        :src_word: the source word 
        :returns: target word

        """
        ret = self.storage_table.objects.get(src_word=src_word)
        return ret.tar_word

    def updata_word_pair(self, *, src_word, tar_word, new_src_word, new_tar_word):
        """update word pair stored in database

        :src_word: the source word which needs to be changed
        :tar_word: the target word which is changed from the source word
        :returns: success or fail

        """
        if src_word:
            new_pair = self.storage_table.objects.get(id=self.id, src_word=src_word)
        elif tar_word:
            new_pair = self.storage_table.objects.get(id=self.id, tar_word=tar_word)
        if new_tar_word:
            new_pair.tar_word = new_tar_word
        if new_src_word:
            new_pair.src_word = new_src_word
        new_pair.save()

    def delete_word_pair(self, *, src_word, tar_word):
        """delete the word pair which contains source word

        :src_word: the source word
        :returns: success or failed

        """
        if src_word:
            ret = self.storage_table.objects.get(src_word=src_word)
        elif tar_word:
            ret = self.storage_table.objects.get(tar_word=tar_word)
        ret.delete()

    def get_all_pairs(self):
        """
        get all the word pairs
        :returns: pair dict

        """
        id = self.id
        pairs_in_catalog = dict()
        pairs_in_catalog[self._catalog] = dict()
        ret = self.storage_table.objects.filter(id=id)
        for line in ret:
            pairs_in_catalog[self._catalog][line.src_word] = line.tar_word
        
        return pairs_in_catalog

def tranAstutter(request):
    """
    get and handle with json

    :request: TODO
    :returns: TODO

    """
    if request.method == 'POST':
        json.loads(request.body)
        return JsonResponse()

def file_uploader(request):
    """
    upload a file and store it in tempfile
    XHR2 support file transmission 
    ajax should use FormData class to implement it
    """
    if request.method == 'POST':
        res = dict()
        upload_file = request.FILES['docx_file']
        if upload_file:
            file_content = ContentFile(upload_file.read())
            docx_f, status = models.docx_file.objects.get_or_create(file_name=upload_file.name)
            docx_f.file_path.save(upload_file.name, file_content)
            docx_f.save()
            res['overwrite'] = status
            res['req_path'] = docx_f.file_path.url

        return JsonResponse(res)

def file_handler(request):
    """
    handle file with json passed from frontend
    request json format
    this api accept 3 kinds of json
    one starts with "action", it suppports two methods.one is translate,
    another is replace
    
    eg.
    {
        "action":"translate"
        "api":"google"
        "target_lang":"zh-CN"
        "req_path":"<req_path>"
    }

    {
        "action":"subsitute"
        "word_cat":"<word_catalog>"
        "req_path":"<req_path>"
    }

    it will response with the json:
    {
        "status":"success"
        "trans_path":"trans_path"
    }
    """
    if request.method == 'POST':
        req = json.loads(request.body)
        if req['action'] == "subsitute":
            res = dict()
            word_cat = req['word_cat']
            req_path = req['req_path']
            res['status'], res['res_path'] = docx_keyword_replace(req_path, word_cat)
            return JsonResponse(res)
        elif req['action'] == 'translate':
            res = dict()
            tar_lang = req['tar_lang']
            req_path = req['req_path']
            api = req['api']
            res['status'], res['res_path'] = docx_translation(req_path, tar_lang=tar_lang, api=api)
            return JsonResponse(res)
        else:
            return JsonResponse({"error":"wrong action"})


def file_downloader(request):
    """
    download file with json requset

    """
    if request.method == 'POST':
        req = json.loads(request.body)
        if req['req_path']:
            file = './' + req['req_path']
            with open(req) as f:
                 pass

def docx_keyword_replace(docx, catalog):
    uploads_path = os.path.dirname(docx)
    docx = os.path.basename(docx)
    changed_file = uploads_path + "/new_" + docx
    database = catalog_handle(catalog)
    all_data = database.get_all_pairs()
    file_handle  = docxrpls('./' + uploads_path + '/' + docx)
    dict_list = [(i, x) for i,x in all_data[catalog].items()]
    full_text_list = file_handle.full_text_list

    for c, i in enumerate(full_text_list):
        for r in dict_list:
            full_text_list[c] = i.replace(*r)
    replace = [(src, tar) for src, tar in zip(file_handle.get_text_list(), full_text_list)]
    file_handle.replace_docx(replace)
    
    file_handle.create_new_file('./' + changed_file)
    file_handle.close()

    return ("ture", changed_file)

def docx_translation(docx, tar_lang=None, api='google'):
    uploads_path = os.path.dirname(docx)
    docx = os.path.basename(docx)
    trans_file = uploads_path + '/trans_' + docx
    file_handle = docxrpls('./' + uploads_path + '/' + docx)
    full_text_list = file_handle.full_text_list

    if not tar_lang:
        tar_lang = 'zh-CN'
    if api == 'google':
        trans = GoogleTranslator(full_text_list, tar_lang)
        trans.translate()
    elif api == "bing":
        trans = BingTranslator(full_text_list, tar_lang)
        trans.translate()
    replace = [(src, tar) for src, tar in zip(full_text_list, trans.trans)]
    file_handle.replace_docx(replace)
    file_handle.create_new_file('./' + trans_file)
    file_handle.close()

    return ("true", trans_file)

