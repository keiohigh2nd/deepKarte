# -*- coding: utf-8 -*-
import json, random, MeCab
import detection, codecs, math
import collections
import numpy as np
import in_out

def find_P(text, index_corpus, file, m):
	#APの病名だけを抽出して分かち書きしてくれる関数
	arr = text.split(" ")
	P_list = []
	for word in arr:
		print "----"
		if int(word.find("#")) != -1:
			fw.write(word)
			fw.write(",")
			tmp = in_out.parse_text(word, m)
			P_list.append(tmp)
			#病気名をベクトル化するかはまた別に考えよう
	return tmp

def vectorlize_Plist(patient_plist):
	#病気名を形態素分析してベクトル化した
	#ただしindexは病名だけで有効である
        from sklearn.feature_extraction.text import CountVectorizer
        vectorizer = CountVectorizer(min_df=1)
        X = vectorizer.fit_transform(patient_plist)
        index = vectorizer.get_feature_names()
        return X.toarray(), index		

def find_similar_patients(matrix, query_id):
	sim_patients = []
	counter = 0
	for row_id in xrange(len(matrix)):
		#類似患者の定義
		tmp_dist = matrix[query_id] - matrix[row_id]
		tmp = np.power(tmp_dist, 2).sum()
		if tmp < 2:
			sim_patients.append(row_id)
	return sim_patients

def find_coexist_words(similar_patients_list):
	vec_corpus = np.load('processed_data/AP_patient.npy')
	r,c  = len(vec_corpus), len(vec_corpus[0])
	arr = np.zeros((1,c), dtype=np.int)

	for pid in similar_patients_list:
		arr = vec_corpus[int(pid)] + arr
	#   word index .... 
	#Pid
	#.
	#.
	#上からどんどんん[0,0,1...]というのに[0,0,1...]というのを足してる
	N = 20
	max_N_list = []
	print arr
	for i in xrange(N):
		tmp = np.argmax(arr)
		max_N_list.append(tmp)
		#上位が確定したものは0にしておく
		arr[0][tmp] = 0	 
	return max_N_list


if __name__ == "__main__":
	#p_text, p_json = read_json("output/one_json_time_series_patient.json")
	p_text, p_json = in_out.read_json("output/json_multi_lab_time_series_patient.json")


        #Unidentified two spaces
        num_patients = len(p_json)
	print "Number of Patient is %s"%num_patients

	m = MeCab.Tagger ("-Owakati")
	#m = MeCab.Tagger ("-Ochasen")

	#Indexの読み込み
	f = codecs.open("processed_data/word_index.txt","r","utf-8")	
	index_corpus = f.read().split(",")
	f.close()

	#類次患者を#Pで絞る. ID - #P
	patient_plist = []
	fw = codecs.open("processed_data/patinet_plist.txt","w","utf-8")
	for i in xrange(num_patients):
		text = p_json["%s"%i]["0"]["A/P"]
		fw.write(p_json["%s"%i]["0"]["patient_id"])
		fw.write(",")
		patient_plist.append(find_P(text, index_corpus, fw, m))
		fw.write("\n")
	fw.close()


	#病気だけの特別辞書
	# plist_mat 
	#		急 腎臓　肝臓
	# patient index 0   1     1
	plist_mat, plist_index =  vectorlize_Plist(patient_plist)
	

	#類似患者集団を抽出しcsvに入れ込む。ここ以外で使えるIDと行列は、患者のIndexと類似する患者集団のINDEX
	#ここの機能は確認済み
	sim_list = []
	f = codecs.open("processed_data/similar_plist.txt","w","utf-8")
	for i in xrange(num_patients):
		similar_patients_id = find_similar_patients(plist_mat, i)
		print "Number of similar patient is %s"%len(similar_patients_id)
		f.write(str(i))
		f.write(',')
		for j in similar_patients_id:
			f.write(str(j))
			f.write(',')
		f.write('\n')
	f.close()
