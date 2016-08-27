import json, random
import detection
import collections
import numpy as np
import dictionarize

def read_json(filename):
        f = open(filename, 'r')
        jsonData = json.load(f,"utf-8")
        text = json.dumps(jsonData)
        f.close()
        return text, jsonData

def get_index(word, index):
        i = 0
	for w in index:
          if w == word:
            return i
          i += 1

def dictionarize_text(arr):
	#Need preprocessing of texts
        cl = collections.Counter(arr)
	from sklearn.feature_extraction import DictVectorizer
	dictionarize_text(cl)
	sm = get_cov(cl, index)
        return count, index

if __name__ == "__main__":
        #count, index = load_sample()

	p_text, p_json = read_json("output/small/small_json_time_series_patient.json")

        #Unidentified two spaces
        texts = p_json["0"]["3"]["Plan"].split("  ")

	count_m, index = dictionarize.vec(texts)
	print index


