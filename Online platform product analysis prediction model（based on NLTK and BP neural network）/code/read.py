import nltk
import requests
import random
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# Read the "Origin of Species"
s = open("file_path")
q=s.readlines()
r="".join(q)
r=r.lower()
print(type(r))