from nltk.sentiment.vader import SentimentIntensityAnalyzer
n=0
def IdentifySentiment(sentence):
    sia = SentimentIntensityAnalyzer()
    ps = sia.polarity_scores(sentence)
    fw = open("file_path", 'a') #将要输出保存的文件地址
    for i in ps:
        fw.write(str(n)+':'+'{0}: {1},'.format(i, ps[i]))
        fw.write("\n") # 换行

for i in sent:
    n+=1
    IdentifySentiment(i)