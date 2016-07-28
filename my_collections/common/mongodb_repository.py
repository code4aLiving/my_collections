import pymongo
from pymongo import MongoClient
import json


class MongoDbItemsRepository():
	
	def __init__(self, connectionString='mongodb://admin:admin@ds036709.mlab.com:36709/'):
		self.connectionString = connectionString
		self.dbName = 'collections'
		self._connect()
		self.db = self.client[self.dbName]

	def _connect(self):
		self.client = MongoClient(self.connectionString + self.dbName)

	def database_exists(self, databaseName):
		names = self.client.database_names()
		return databaseName in names

	def insert_item(self, collectionName, item):
		collection = self.db[str(collectionName)]
		return collection.insert_one(item).inserted_id
	
	def get_items(self, collectionName, page=1, pageSize=100):
		collection = self.db[str(collectionName)]
		count = 0
		res = []
		for x in collection.find():
			res.append(x)
			count+=1
			if count >= pageSize:
				break
		return res

	def get_item_by_id(self, collectionName, itemId):
		pass