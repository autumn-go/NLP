with open('path') as f1:
    res1 = f1.read()
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [res1] 
vector = TfidfVectorizer() 
tfidf = vector.fit_transform(corpus) 

wordlist = vector.get_feature_names()
weightlist = tfidf.toarray()  
for i in range(len(weightlist)):  
    print("-------------")  
    for j in range(len(wordlist)):  
        print(wordlist[j],weightlist[i][j])