#!/usr/bin/env python

inf = "file1_out_clean.txt"
# inf = "file1.txt"
outf1 = "nodes_dictionary.txt"
outf2 = "graph_edges.txt"

outf3 = "nodes_dictionary_fang.txt"
outf4 = "nodes_dictionary_bing.txt"
outf5 = "graph_edges_bing-fang-relation.txt"

fd1 = open(outf1, "w+", encoding='UTF-8')
fd2 = open(outf2, "w+", encoding='UTF-8')

nodes_dic = {}
index = 0
with open(inf, 'r', encoding='UTF-8') as indata:
	for line in indata:
		arr = line.strip().split(" ")
		if len(arr) != 2:
			# print("%s |  %s" % (line.strip(), arr))
			continue

		node1, node2 = line.strip().split()[0:2]
		if node1 not in nodes_dic.keys():
			nodes_dic[node1] = str(index)
			index += 1

		if node2 not in nodes_dic.keys():
			nodes_dic[node2] = str(index)
			index += 1

		fd2.write("%s %s\n" % (nodes_dic[node1], nodes_dic[node2]))


for key,value in nodes_dic.items():
    fd1.write("%s %s\n" % (value, key))

print("total nodes: %d", index)

fd1.close()
fd2.close()
print("Done!")
