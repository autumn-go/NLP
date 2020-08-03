def CreateTuples(words):
   tuples = []

   for i in range( len(words)-1 ):
      tuples.append( (words[i], words[i+1]) )

   return tuples

# Iterate the bigrams and construct a sentence until a '.' is encountered.
def EmitSentence(cfdist):
   word1 = u'I'
   sentence = []
   sentence.append(word1)

   while word1 != '.,!':
      options = []
      for gram in cfdist[word1]:
         for result in range(cfdist[word1][gram]):
            options.append(gram)

      word1 = options[int((len(options))*random.random())]
      sentence.append(word1)

   print(sentence)



# Create the bigram word tuples
tuples = CreateTuples(words)

# Create a conditional frequency distribution based upon the tuples
cfdist = nltk.ConditionalFreqDist(tuples)

# Emit a random sentence based upon the corpus
EmitSentence( cfdist )