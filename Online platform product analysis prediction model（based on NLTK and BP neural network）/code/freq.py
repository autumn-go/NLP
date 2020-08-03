import nltk
from nltk import FreqDist
from matplotlib import rcParams

fd = FreqDist(filtered_words)
mc = fd.most_common(20)

print(mc)
fd.plot(20,cumulative=False)