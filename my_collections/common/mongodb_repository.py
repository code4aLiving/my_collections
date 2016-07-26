import pymongo
from pymongo import MongoClient


class MongoDbRepository():
	
	def __init__(self, connectionString='mongodb://localhost:27017/', username="", password=""):
		self.connectionString = connectionString
		self.username = username
		self.password = password
		self._connect()

	def _connect():
		self.mongoClient = MongoClient(self.connectionString)


	def database_exists(self, databaseName):
		names = self.mongoClient.database_names()
		return databaseName in names
		