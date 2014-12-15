# coding: utf-8

import json
import UtilDefine

class JsonDecoder:

	def loadByPath(self,path):
		file = open(path,"r")
		self.jsonData = file.read()
		self.content  = json.loads(self.jsonData,encoding = UtilDefine.CODE_TYPE)
	
	def loadByData(self,data):
		self.jsonData = data
		self.content  = json.loads(self.jsonData,encoding = UtilDefine.CODE_TYPE)
		
	def getByKey(self,key):
		return self.content[key]
		
	def setByKey(self,key,value):
		self.content[key] = value
