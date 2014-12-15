# coding: utf-8
import json
from Module.Util import UtilDefine

'''
#input1 = open("/Users/zxianer/Programs/Test/CN/name",'r')
#input2 = open("/Users/zxianer/Programs/Test/CN/rank2",'r')
#output = open("/Users/zxianer/Programs/Test/CN/namerank",'w')

name_str = input1.read()
rank_str = input2.read()

name = name_str.split('\n')
rank = rank_str.split('\n')

name_rank = []

for i in range(len(rank)):
	for j in range(len(name)):
		rank_each = rank[i]
		name_each = name[j]
		if rank_each.find(name_each) != -1:
			name_rank.append(name_each)	
			name[j] = " "

for k in range(len(name)):
	word = name[k]
	if word != " ":
		name_rank.append(word)

for each in name_rank:
	output.write(each + '\n')
'''

'''
input = open("/Users/zxianer/Programs/Test/CN/namerank",'r')
output = open("/Users/zxianer/Programs/Test/CN/namerank_json",'w')

name_rank = input.read()

name_rank_str = name_rank.split('\n')

name_rank_num = []
name_dict = {"list":[]}
sum = 10000

for i in range(len(name_rank_str)):
	word = ""
	rank = 0;
	temp_dict = {}
	if i < 100:
		rank = 30
	elif i < 200:
		rank = 25
	elif i < 300:
		rank = 20
	elif i < 400:
		rank = 15
	elif i < 500:
		rank = 10
	
	sum -= rank
	
	temp_dict["surname"] = name_rank_str[i]
	temp_dict["rank"] = sum
	name_dict["list"].append(temp_dict)

encodejson = json.dumps(name_dict,ensure_ascii=False)

output.write(encodejson)

'''

'''
import random

input = open("/Users/zxianer/Programs/Test/CN/namerank_json",'r')

json_str = input.read()
totalrank = 10000
obj = json.loads(json_str,encoding='utf-8')

list = obj["list"]

name_word = ""
name_rank = 0

ll = []

for i in range(500):
	rank = int(random.random()*totalrank)
	for each in list:
		if rank >= each["rank"]:
			name_word = each["surname"]
			name_rank = each["rank"]
			break
	ll.append(name_word)

for j in ll:
	print j
'''

'''
from UtilJson import JsonDecoder 

a = JsonDecoder()
a.loadByPath("/Users/zxianer/Programs/Test/CN/namerank_json")

b = a.getByKey("list")

for each in b:
	print each['surname']
'''

'''
input = open("/Users/zxianer/Programs/Test/CN/name_name",'r')
output = open("/Users/zxianer/Programs/Test/CN/name.json",'w')

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

str = input.read()

list = str.split('\n')

name=[]
d = {"list":[]}
for each in list:
	if each not in name:
		d["list"].append(each)
		
encodejson = json.dumps(d,ensure_ascii=False)

output.write(encodejson)
'''
'''
#output.write(encodejson)


from NameBook import NameBook
from UtilJson import JsonDecoder
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


input = open("/Users/zxianer/Programs/Test/CN/name1.json","r")
output = open("/Users/zxianer/Programs/Test/CN/name2","w")

str = input.read()

list = str.split("\n")

d = {"list":[]}

for each in list:
	s={}
	line = each.split(" ")
	s["word"] = line[0]
	s["level"] = int(line[1])
	d["list"].append(s)

encodejson = json.dumps(d,ensure_ascii=False)
output.write(encodejson)
'''

'''
from NameBook import NameBook
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

a = NameBook()

print a.getNameByNature(UtilDefine.NAME_NATURE_WOMAN)
'''


import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)



















