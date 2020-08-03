from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
#分词
# Tokenize sentences from the text 分句
sent = sent_tokenize(r)

print (len(sent))
print (sent[random.randint(0,len(sent))])

# 分词
raw_words = word_tokenize(r)

# 词形归一化
wordnet_lematizer = WordNetLemmatizer()
words = [wordnet_lematizer.lemmatize(raw_word) for raw_word in raw_words]

#去除标点
words=[word for word in words if word.isalpha()]

# 去除停用词
filtered_words = [word for word in words if word not in stopwords.words('english')]

print (len(words))
print(len(filtered_words))