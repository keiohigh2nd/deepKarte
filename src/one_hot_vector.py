# -*- coding: utf-8 -*-
import json, random, MeCab
import detection, codecs
import collections
import numpy as np
import dictionarize, in_out, neighbor_matrix

if __name__ == "__main__":
	#このスクリプトはword_indexと近傍行列とPatient IDリストを作る
	p_text, p_json = in_out.read_json("output/json_multi_lab_time_series_patient.json")

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

	#1文字ずつ分けて辞書作っている
	vec_corpus, index_corpus = dictionarize.vec(tmp)
	#vec_corpus, index_corpus = dictionarize.vec_oneword(tmp)
	
	np.save('processed_data/AP_patient.npy', vec_corpus)

	f = codecs.open("processed_data/word_index.txt","w","utf-8")
	for word in index_corpus:
		f.write(word)
		f.write(",")
	f.close()

	#word neighbor MATRIX
	w_range = 5 #ここの実装はまだ
	sm_tensor = []
	for i in xrange(num_patients):
		text = p_json["%s"%i]["0"]["A/P"]
		arr_text = in_out.parse_text(text, m)
		mat = neighbor_matrix.neighbor_matrix(arr_text, index_corpus)
		sm_tensor.append(mat)
	np.save('processed_data/Neighbor_mat.npy', sm_tensor)
	#tmp = np.load('processed_data/Neighbor_mat.npy')
