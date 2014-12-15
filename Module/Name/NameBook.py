#coding: utf-8

import sys
sys.path.append("../")

import os
import random
from Util import UtilDefine
from Util.UtilJson import JsonDecoder

class Surname:
	def __init__(self):
		self.jsonDecoder = JsonDecoder()
		dataPath = os.getcwd() + "/../../Data/surname.json"
		self.jsonDecoder.loadByPath(dataPath)
		self.content = self.jsonDecoder.getByKey("list")

	def getRank(self):
		return random.randint(0,UtilDefine.RANDOM_STD)

	def getSurname(self):
		rand_rank = self.getRank()
		for each in self.content:
			name_rank = each["rank"]
			if rand_rank >= name_rank:
				return each["surname"]

class Name:
	def __init__(self):
		self.nameLevel1 = []
		self.nameLevel2 = []
		self.nameLevel3 = []
		self.nameLevel4 = []
		self.nameLevel5 = []
		self.jsonDecoder = JsonDecoder()
		dataPath = os.getcwd() + "/../../Data/name.json"
		self.jsonDecoder.loadByPath(dataPath)
		self.content = self.jsonDecoder.getByKey("list")
		self.doClassifyName()
		
	def getRandomWord(self):
		list = self.nameLevel1 + self.nameLevel2 + self.nameLevel3 + self.nameLevel4 + self.nameLevel5
		random.shuffle(list)
		return self.doGetName(self.content)
	
	def getManWord(self):
		list = self.nameLevel1 + self.nameLevel2 + self.nameLevel3
		random.shuffle(list)
		return self.doGetName(list)

	def getWomanWord(self):
		list = self.nameLevel3 + self.nameLevel4 + self.nameLevel5
		random.shuffle(list)
		return self.doGetName(list)
		
	def getWordByNature(self,nature):
		
		if nature == UtilDefine.NAME_NATURE_TRUEMAN:
			if self.getWordNumberRank() == UtilDefine.WORD_NUM_SINGLE:
				return self.doGetName(self.nameLevel1,UtilDefine.NAME_GET_SINGLE)
			else:
				list = self.nameLevel1 + self.nameLevel2 + self.nameLevel3
				random.shuffle(list)
				return self.doGetName(list,UtilDefine.NAME_GET_SINGLE) + self.doGetName(self.nameLevel1,UtilDefine.NAME_GET_SINGLE)
				
		elif nature == UtilDefine.NAME_NATURE_MAN:
			list = self.nameLevel2 + self.nameLevel3
			random.shuffle(list)
			return self.doGetName(list)
			
		elif nature == UtilDefine.NAME_NATURE_WOMAN:
			list = self.nameLevel4 + self.nameLevel3
			random.shuffle(list)
			return self.doGetName(list)

		elif nature == UtilDefine.NAME_NATURE_TRUEWOMAN:
			if self.getWordNumberRank() == UtilDefine.WORD_NUM_SINGLE:
				return self.doGetName(self.nameLevel5,UtilDefine.NAME_GET_SINGLE)
			else:
				list = self.nameLevel3 + self.nameLevel4 + self.nameLevel5
				random.shuffle(list)
				return self.doGetName(list,type = UtilDefine.NAME_GET_SINGLE) + self.doGetName(self.nameLevel5,type = UtilDefine.NAME_GET_SINGLE)
	
	def doGetName(self,list,type = UtilDefine.NAME_GET_RANDOM):
		
		type_rank = UtilDefine.WORD_NUM_SINGLE
		if type == UtilDefine.NAME_GET_RANDOM:
			type_rank = self.getWordNumberRank()
		elif type == UtilDefine.NAME_GET_SINGLE:
			type_rank = UtilDefine.WORD_NUM_SINGLE
		elif type == UtilDefine.NAME_GET_DOUBLE:
			type_rank = ~(UtilDefine.WORD_NUM_SINGLE)
			
		if type_rank == UtilDefine.WORD_NUM_SINGLE:
			return list[self.getRank(list)]
		else:
			middword = list[self.getRank(list)]
			lastword = list[self.getRank(list)]
			while(True):
				if middword == lastword:
					lastword = self.content[self.getRank()]
				else:
					break;
			return middword + lastword

	def getRank(self,list):
		return random.randint(0,len(list) - 1)
		
	def getWordNumberRank(self):
		return random.randint(0,3)
		
	def doClassifyName(self):
		for each in self.content:
			if   each["level"] == UtilDefine.NAME_LEVEL1:
				self.nameLevel1.append(each["word"])
			elif each["level"] == UtilDefine.NAME_LEVEL2:
				self.nameLevel2.append(each["word"])
			elif each["level"] == UtilDefine.NAME_LEVEL3:
				self.nameLevel3.append(each["word"])
			elif each["level"] == UtilDefine.NAME_LEVEL4:
				self.nameLevel4.append(each["word"])
			elif each["level"] == UtilDefine.NAME_LEVEL5:
				self.nameLevel5.append(each["word"])
				
		
class NameBook:
	def __init__(self):
		self.surname = Surname()
		self.name    = Name()
		
	def getHumanName(self):
		return self.surname.getSurname() + self.name.getName()

	def getRandomManName(self):
		return self.surname.getSurname() + self.name.getManWord()

	def getRandomWomanName(self):
		return self.surname.getSurname() + self.name.getWomanWord()

	def getNameByNature(self,nature):
		return self.surname.getSurname() + self.name.getWordByNature(nature)





















