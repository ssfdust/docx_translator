from django.shortcuts import render
from translation import models
from django.http import HttpResponse
from hashlib import md5
import json

# Create your views here.

class catalog_handle(object):

    """Docstring for newtable. """

    def __init__(self, catalog):
        """TODO: to be defined1.

        :catalog: TODO

        """
        self._catalog = catalog
        self.catalog_hash = self.get_catalog_hash()
        self.id = self.get_id(self.catalog_hash)
        self.storage_id = self.get_storage_id(self.id)
        self.storage_table = self.get_storage_table()

    def get_catalog_hash(self):
        """get the hash of catalog name
        :returns: TODO

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

    def get_storage_table(self, storage_id=self.storage_id):
        """TODO: Docstring for create_or_get.

        :storage_id: the storage id used by daatabase 
        :returns: create success or the info

        """
        table = getattr(models, "catalog_" + storage_id)
        return table

    def create_or_get(self, id=self.id):
        """insert a new line with current id and 
        catalog name if this catalog is not existed

        :id: TODO
        :returns: TODO

        """
        catalog_id_table = getattr(models, "catalog_ids")
        (ret, state) = catalog_id_table.objects.get_or_create(id=id, catalog=self._catalog)
        return state

    def insert_pairs(self, storage_table=self.storage_table, src_word, tar_word):
        """insert source word and target word pairs.

        :storage_table: TODO
        :src_word: the source word which needs to be translated
        :tar_word: the target word which is translated from the source word
        :returns: true or false

        """
        (ret, state) = storage_table.objects.get_or_create(id=self.id, src_word=src_word,tar_word=tar_word)
        return state

def get_json(request):
    """get and handle with json

    :request: TODO
    :returns: TODO

    """
    pass
