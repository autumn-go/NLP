1. 抽取所有医案中草药、方剂数据，输出文件：rdf_triplet_clean.txt；（进行少部分人工校对）
python .\tools_extract_triplet_from_medical_case1.py


2. 对file1增加草药数据，输出文件file1_out；
python .\tools_add_herb_to_file1.py


3. 去掉file1_out中多余的编号1,2,3....1732，
python .\tools_file1_clean.py
输出文件：
file1_out_clean；（在file1_out基础上，去掉了方剂前面的编号）
file1_out_clean_only_fang-bing.txt（只包含病和方的对应关系，用作实验结果分析，也是第5步的输入）


4. 对图表示文件file1_out_clean进行编码，输出为可被node2vec接受的格式
python .\tools_construct_graph.py
输出文件：
nodes_dictionary.txt	 （节点编号）
graph_edges.txt	（边转换为编号，可直接运行node2vec）


5. 从图中找出方剂和疾病的节点，及对应关系，后续用于KNN的推荐算法分析
python .\tools_find_fang_bing_from_graph.py
输出文件：
graph_edges_bing-fang-relation.txt	（方剂和边对应关系，用节点的编号表示）
nodes_dictionary_bing.txt		（疾病的节点编码）
nodes_dictionary_fang.txt		（方剂的节点编码）


