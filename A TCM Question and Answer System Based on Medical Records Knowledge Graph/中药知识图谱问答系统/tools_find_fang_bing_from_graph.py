#!/usr/bin/env python

inf1 = "file1_out_clean_only_fang-bing.txt"
# inf = "file1.txt"
inf2 = "nodes_dictionary.txt"

outf1 = "nodes_dictionary_fang.txt"
outf2 = "nodes_dictionary_bing.txt"
outf3 = "graph_edges_bing-fang-relation.txt"

fd1 = open(outf1, "w+", encoding='UTF-8')
fd2 = open(outf2, "w+", encoding='UTF-8')
fd3 = open(outf3, "w+", encoding='UTF-8')

# 加载字典编码
nodes_dic = {}
with open(inf2, 'r', encoding='UTF-8') as indata:
	for line in indata:
		arr = line.strip().split(" ")
		if len(arr) != 2:
			print("%s |  %s" % (line.strip(), arr))
			continue

		val, key = line.strip().split()[0:2]
		nodes_dic[key] = val
print(len(nodes_dic))


fang_s = set()
bing_s = set()
with open(inf1, 'r', encoding='UTF-8') as indata:
	for line in indata:
		arr = line.strip().split(" ")
		if len(arr) != 2:
			# print("%s |  %s" % (line.strip(), arr))
			continue

		node1, node2 = line.strip().split()[0:2]
		fd3.write("%s %s\n" % (nodes_dic[node1], nodes_dic[node2]))
		fang_s.add(node1)
		bing_s.add(node2)

for key in fang_s:
    fd1.write("%s %s\n" % (nodes_dic[key], key))

for key in bing_s:
    fd2.write("%s %s\n" % (nodes_dic[key], key))

fd1.close()
fd2.close()
print("Done!")
