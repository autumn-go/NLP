1. ��ȡ����ҽ���в�ҩ���������ݣ�����ļ���rdf_triplet_clean.txt���������ٲ����˹�У�ԣ�
python .\tools_extract_triplet_from_medical_case1.py


2. ��file1���Ӳ�ҩ���ݣ�����ļ�file1_out��
python .\tools_add_herb_to_file1.py


3. ȥ��file1_out�ж���ı��1,2,3....1732��
python .\tools_file1_clean.py
����ļ���
file1_out_clean������file1_out�����ϣ�ȥ���˷���ǰ��ı�ţ�
file1_out_clean_only_fang-bing.txt��ֻ�������ͷ��Ķ�Ӧ��ϵ������ʵ����������Ҳ�ǵ�5�������룩


4. ��ͼ��ʾ�ļ�file1_out_clean���б��룬���Ϊ�ɱ�node2vec���ܵĸ�ʽ
python .\tools_construct_graph.py
����ļ���
nodes_dictionary.txt	 ���ڵ��ţ�
graph_edges.txt	����ת��Ϊ��ţ���ֱ������node2vec��


5. ��ͼ���ҳ������ͼ����Ľڵ㣬����Ӧ��ϵ����������KNN���Ƽ��㷨����
python .\tools_find_fang_bing_from_graph.py
����ļ���
graph_edges_bing-fang-relation.txt	�������ͱ߶�Ӧ��ϵ���ýڵ�ı�ű�ʾ��
nodes_dictionary_bing.txt		�������Ľڵ���룩
nodes_dictionary_fang.txt		�������Ľڵ���룩


