import os

import pymongo

__author__ = 'jslvtr'


class Database(object):
    #URI = os.environ.get("MONGOLAB_URI")
    URI = "mongodb://freshlens:VMSktsp2Ykw!*ND@ds241688.mlab.com:41688/heroku_rrk7322c"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client.get_default_database()  # ['heroku_rrk7322c']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)
