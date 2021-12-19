# coding: utf8

### imports
import spacy
import collections
from operator import itemgetter
import sys
import os
### language config
nlp = spacy.load('en')

### algorithm class
class Algo_NLP(object):
	"""docstring for Algo_NLP"""
	def __init__(self, subject, texts):
		self.subject = subject
		self.texts = texts
		
	"""
	in: all the texts
	out: all the importent Sentences
	"""
	def Importent_Sentences(self):
		dic = {}

		texts = [nlp(text) for text in self.texts]

		for te in self.texts: ### loop on all the texts
			ts = self.texts ### main text
			ts.remove(te)

			for sent in te.sents: ## Loop on Sentences in the main text

				Sum_high = []
				for text in ts: ## for all texts
					a = sorted(text.sents, key = lambda x: sent.similarity(x), reverse = True) ## sorting all the Sentences in the texts by similarity

					Sum_high.append(sent.similarity(a[0])) ## Add the Highest similarity

				dic[sent] = (sum(Sum_high) / len(Sum_high))

		sorted_list = sorted(dic.items(), key = lambda kv: kv[1]) ## sort from high to low
		sorted_dic = collections.OrderedDict(sorted_list) ## convert to dic

		lis = []
		
		for k, v in sorted_dic.items(): ## filtering all the bad
			if v > 0.88:
				lis.append(k)

		lis.reverse()

		for v in lis: ## taking just the highest similaritys
			for v2 in lis:
				if v.similarity(v2) > 0.85 and lis.index(v) < lis.index(v2):
					lis.remove(v2)

		return lis ## return list of the importent sen


	"""
	In: importent Sentences
	Out: a summary of all the Sentences
	"""
	def summary(self):
		texts = [nlp(text) for text in self.texts]
		most_importent_sents = Importent_Senteces(texts)

		lis = []
		for text in most_importent_sents:
			tok = [token.text for token in text if not token.is_stop and token.is_alpha] ## remove all but the good stuff
			lis.extend(tok)

		dic = {}

		for word in lis:
			count = lis.count(word)
			dic[word] = count

		max_key = max(dic, key=dic.get)
		max_value = dic[max_key]

		for word in dic:
			dic[word] = dic[word] / max_value


		dic_sen = {}
		value = 0
		for sen in most_importent_sents:
			for k,v in dic.items():
				value =  value + (v * str(sen).count(k))

			dic_sen[sen] = value
			value = 0


		sorted_list = sorted(dic_sen.items(), key = lambda kv: kv[1]) ## sort from low to high
		sorted_dic = collections.OrderedDict(sorted_list) ## convert to dic
		sorted_list = list(sorted_dic.keys())
		sorted_list.reverse()


		string = ''
		for s in sorted_list:
			string = string + str(s)

		return string