# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:07:39 2016

@author: 21163
"""

from mrjob.job import MRJob
from mrjob.protocol import StandardJSONProtocol
#import re

from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))



#WORD_RE = re.compile(r"[\w']+")
snowball_stemmer = SnowballStemmer('english')
class MRWordFreqCount(MRJob):
    INPUT_PROTOCOL = StandardJSONProtocol
    def mapper(self, key, line):
        yield(key,1)
 
    def combiner(self, word, counts):
        yield (word, sum(counts))
 
    def reducer(self, word, counts):
        yield (word, sum(counts))
 
if __name__ == '__main__':
    MRWordFreqCount.run()