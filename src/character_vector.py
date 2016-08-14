# -*- coding: utf-8 -*-
import json, random, MeCab, collections, codecs
import numpy as np
import dictionarize, in_out, detection
	
def ch_hot_vector(index, ch):
        tmp_id = in_out.return_vector(index, ch)
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
			tmp[in_out.return_vector(index, sample_texts[i+j])] = 1
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

