# -*- coding: utf-8 -*-
import json, random, MeCab
import detection, codecs
import collections
import numpy as np
import dictionarize, in_out

def return_vector(arr_index, text):
	return arr_index.index(text)

def neighbor_matrix(arr_text, index_corpus):
	s_matrix = np.zeros((len(index_corpus), len(index_corpus)))	
	arr_text = arr_text.split(" ")
	del arr_text[-1]
	del arr_text[0]
	for t in xrange(len(arr_text)):	
		try:
			i = index_corpus.index(arr_text[t])
			if t > 0:
				m_1 = index_corpus.index(arr_text[t-1])
                       		s_matrix[i][m_1] += 1
                	if t < len(arr_text)-1:
                        	m1 = index_corpus.index(arr_text[t+1])
                        	s_matrix[i][m1] += 1
			if t > 1:
                                m_2 = index_corpus.index(arr_text[t-2])
                                s_matrix[i][m_2] += 1
                        if t < len(arr_text)-2:
                                m1 = index_corpus.index(arr_text[t+2])
                                s_matrix[i][m2] += 1
		except:
			pass
	return s_matrix
		
	
def ch_hot_vector(index, ch):
        tmp_id = return_vector(index, ch)
        size = len(index)
        tmp_vec = np.zeros((size))
        tmp_vec[tmp_id]  = 1
        return tmp_vec

def create_data(nb_of_samples, sequence_len):
	f = codecs.open("processed_data/word_index.txt","r","utf-8")
	index = f.read().split(",")
	f.close()
	
	p_text, p_json = in_out.read_json("output/one_json_time_series_patient.json")
	sample_texts = p_json["2"]["0"]["A/P"]
	samples = []
	for i in xrange(nb_of_samples):
		tmp = np.zeros(len(index))
		for j in xrange(sequence_len):
			tmp[return_vector(index, sample_texts[i+j])] = 1
		samples.append(tmp)
	return samples


if __name__ == "__main__":
        #count, index = load_sample()

	p_text, p_json = in_out.read_json("output/one_json_time_series_patient.json")

        #Unidentified two spaces
        num_patients = len(p_json)
	print "Number of Patient is %s"%num_patients

	m = MeCab.Tagger ("-Owakati")
	#m = MeCab.Tagger ("-Ochasen")

	
	tmp = []
	fp = open("processed_data/patient_id.txt", "w")
	for i in xrange(num_patients):
		text = p_json["%s"%i]["0"]["A/P"]
		fp.write(p_json["%s"%i]["0"]["patient_id"])
		fp.write("\n")
		tmp.append(in_out.parse_text(text, m))
	fp.close()

	vec_corpus, index_corpus = dictionarize.vec(tmp)
	
	np.save('processed_data/AP_patient.npy', vec_corpus)
	
	f = codecs.open("processed_data/word_index.txt","r","utf-8")
        index = f.read().split(",")
        f.close()	


	"""
	f = codecs.open("processed_data/word_index.txt","w","utf-8")
	for word in index_corpus:
		f.write(word)
		f.write(",")
	f.close()
	"""
	#ここからはsampleだが,parseしなくても可
	#Example
	sample = p_json["2"]["0"]["A/P"]
	parsed_sample = in_out.parse_text(text, m)
	#print ch_hot_vector(index_corpus, sample[1])

	nb_of_samples = 4
	sequence_len = 3
	print create_data(nb_of_samples, sequence_len)		

