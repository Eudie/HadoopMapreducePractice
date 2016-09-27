# -*- coding: utf-8 -*-
"""
Building the mapreduce using csv as input
"""

from mrjob.job import MRJob
from StringIO import StringIO
#import re
import csv
import sys
#from nltk.stem import SnowballStemmer
#from nltk.corpus import stopwords
#stop_words = set(stopwords.words('english'))
 
#WORD_RE = re.compile(r"[\w']+")
#snowball_stemmer = SnowballStemmer('english')
line = sys.stdin
class MRWordFreqCount(MRJob):
 
    def mapper(self, _, line):
        line = unicode(line, errors='ignore')
        a = csv.reader(StringIO(line), delimiter = ',')
#        for items in csv.reader(StringIO(line), delimiter = ','):
#            a = items[0]
#            #b = items[1]



            

#        for word in Words: #WORD_RE.findall(line):
#            IntWord = word.lower()
#            ExtWord = snowball_stemmer.stem(IntWord)
#            if ExtWord not in stop_words:
#                yield (ExtWord, 1)
        yield(a[1],1)
 
    def combiner(self, word, counts):
        yield (word, sum(counts))
 
    def reducer(self, word, counts):
        yield (word, sum(counts))
 
if __name__ == '__main__':
    MRWordFreqCount.run()