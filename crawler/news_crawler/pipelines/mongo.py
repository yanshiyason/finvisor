# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

class MongoPipeline(object):

    collection_name = 'articles'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.collection_name]
        self.create_indexes();

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print("--- INSERTING ARTICLE INTO MONGO ---")
        try:
            self.collection.insert_one(dict(item))
        except DuplicateKeyError:
            print("--- ALREADY INSERTED ---")

        return item

    def create_indexes(self):
        self.collection.create_index("meta.canonical", unique=True)
