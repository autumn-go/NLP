#!/usr/bin/env python

import re

file1_out = "file1_out.txt"
file1_out_clean = "file1_out_clean.txt"
file1_out_clean_only_fang_bing = "file1_out_clean_only_fang-bing.txt"


fd = open(file1_out_clean, "w+", encoding='UTF-8')
fd1 = open(file1_out_clean_only_fang_bing, "w+", encoding='UTF-8')

index = 1
with open(file1_out, 'r', encoding='UTF-8') as indata:
	for line in indata:
		if line.strip().find(str(index)) == 0:
			arr = re.split(str(index), line.strip())
			del arr[0]
			line_clean = str(index).join(arr)
			fd.write("%s\n" % line_clean)
			fd1.write("%s\n" % line_clean)
			index += 1					
		else:
			fd.write("%s\n" % line.strip())

fd.close()
fd1.close()

