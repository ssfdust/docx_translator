from django.shortcuts import render
from translation import models
from translation.regandtrans.stutter import Stutter
from translation.regandtrans.translatorbysimulate import BingTranslator
from translation.regandtrans.translatorbysimulate import GoogleTranslator
from django.http import JsonResponse
from hashlib import md5
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
        """get all the word pairs
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
    """get and handle with json

    :request: TODO
    :returns: TODO

    """
    json.loads(request.body)
    return JsonResponse()

