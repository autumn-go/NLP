import json
import time
import os
import re
# import hashlib
#pip install xpinyin
# from xpinyin import Pinyin


triplet_f = "rdf_triplet_clean.txt"

def write_into_file(f, content):
	with open(f, 'a+', encoding='UTF-8') as f:
		f.write("%s\n" % content)
		f.close()


def read_file_into_set(f):
	fset = set()
	index = 0
	with open(f, 'r', encoding='UTF-8') as indata:
		for line in indata:
			index += 1
			arr = re.split(str(index), line.strip())
			# if len(arr) > 2:
			# 	print("--------------- %s" % line)

			del arr[0]
			name=str(index).join(arr)
			# name = arr[1]
			# name = line.strip().strip(str(index))

			# if(index==29 or index==955 or index==22):
			# 	print("%s %s" % (line.strip(), name))
			# if name in fset:
			# 	print("%s %s" % (line.strip(), name))
			fset.add(name)

	return fset


def read_file1_part(fin, title, fout):
	fset = set()
	index = 1
	flag = 0 
	with open(fin, 'r', encoding='UTF-8') as indata:
		for line in indata:
			if line.strip().find(str(index)) == 0:
				flag = 0
				arr = re.split(str(index), line.strip())
				del arr[0]
				name=str(index).join(arr)
				if name == title:
					flag = 1
					write_into_file(fout, line.strip())
				index += 1					
			else:
				if flag:
					write_into_file(fout, line.strip())


def read_rdf_triplet_part(fin, title, fout):
	# print(title)
	tmp_s = set()
	with open(fin, 'r', encoding='UTF-8') as indata:
		for line in indata:
			arr = line.strip().split(" ")
			relation = arr[-1]
			# print(arr)
			# print(arr[-1])
			# print("%s | %s" % (line.strip(), arr))
			if len(arr) < 3:
				print("%s | %s" % (line.strip(), arr))
				print("----------------")
			elif arr[-1] == "组成" or arr[-1] == "治疗":
				arr.pop()
				if len(arr) >= 2:
					arr.pop()
			else:
				arr.pop()

			name = " ".join(arr)
			# print("test: %s" % name)

			if name == title and relation == "组成":
				if line.strip() not in tmp_s:
					arr1 = line.strip().split(" ")
					arr1.pop()
					content = " ".join(arr1)
					write_into_file(fout, content)

					tmp_s.add(line.strip())


file1 = "file1.txt"
file1_out = "file1_out.txt"

# fset = set()
index = 1
pre_name = ""
with open(file1, 'r', encoding='UTF-8') as indata:
	for line in indata:
		if line.strip().find(str(index)) == 0:
			arr = re.split(str(index), line.strip())
			del arr[0]
			tmpstr = str(index).join(arr)
			name = tmpstr.split(" ")[0]
			if pre_name != "":
				read_rdf_triplet_part(triplet_f, pre_name, file1_out)
				# break

			write_into_file(file1_out, line.strip())
			index += 1
			pre_name = name				
		else:
			write_into_file(file1_out, line.strip())
	if pre_name != "":
		read_rdf_triplet_part(triplet_f, pre_name, file1_out)



