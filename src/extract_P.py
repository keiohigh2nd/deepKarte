# -*- coding: utf-8 -*-
import json, random, MeCab
import detection, codecs, math
import collections
import numpy as np
import one_hot_vector

def read_json(filename):
        f = open(filename, 'r')
        jsonData = json.load(f,"utf-8")
        text = json.dumps(jsonData)
        f.close()
        return text, jsonData

def parse_text(text, tagger):
	encode_text = text.encode('utf-8')
        res = m.parse(encode_text)
        return res.decode('utf-8')

def vec(arr):
	from sklearn.feature_extraction.text import CountVectorizer
	vectorizer = CountVectorizer(min_df=1)
	X = vectorizer.fit_transform(arr)
	index = vectorizer.get_feature_names()
	return X.toarray(), index

def find_P(text, index_corpus, file, m):
	arr = text.split(" ")
	P_list = []
	for word in arr:
		if int(word.find("#")) != -1:
			fw.write(word)
			fw.write(",")
			tmp = one_hot_vector.parse_text(word, m)
			#P_list.append(tmp)
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

def show_noun(pid):
	f = codecs.open("processed_data/word_index.txt","r","utf-8")
        index_corpus = f.read().split(",")
        f.close()

	fp = codecs.open("processed_data/similar_plist.txt","r","utf-8")
	plist = fp.read().split("\n")
	fp.close()

	similar_patients_id = plist[pid].split(",")
	del similar_patients_id[-1]

	max_N_list = find_coexist_words(similar_patients_id)
        max_N_words = []
        tmp = ""
        for i in max_N_list:
                max_N_words.append(index_corpus[i])
                tmp += index_corpus[i]

	m = MeCab.Tagger ("-Owakati")
        encode_text = tmp.encode('utf-8')
        res = m.parseToNode(encode_text)
        noun_box = []
        while res:
                tmp = res.feature.decode('utf-8').split(",")
                if tmp[0] == u'名詞':
                        noun_box.append(tmp[6])
                res = res.next
	#view以下のCSVに書き込みたいなら、ここで書き込め
	return noun_box

if __name__ == "__main__":
	p_text, p_json = read_json("output/one_json_time_series_patient.json")

        #Unidentified two spaces
        num_patients = len(p_json)
	print "Number of Patient is %s"%num_patients

	m = MeCab.Tagger ("-Owakati")
	#m = MeCab.Tagger ("-Ochasen")

	#Indexの読み込み
	f = codecs.open("processed_data/word_index.txt","r","utf-8")	
	index_corpus = f.read().split(",")
	f.close()

	patient_plist = []
	fw = codecs.open("processed_data/patinet_plist.txt","w","utf-8")
	for i in xrange(num_patients):
		text = p_json["%s"%i]["0"]["A/P"]
		fw.write(p_json["%s"%i]["0"]["patient_id"])
		fw.write(",")
		patient_plist.append(find_P(text, index_corpus, fw, m))
		fw.write("\n")
	fw.close()

	plist_mat, plist_index =  vectorlize_Plist(patient_plist)

	#類似患者集団を抽出しcsvに入れ込む
	#ここ以外で使えるIDと行列は、患者のIndexと類似する患者集団のINDEX
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



	#病名が類似している類似患者は先に割り出しておく
	#共起単語の発見
	#similar_patients_idはcsvで開けて、index_corpusも開ける
	
	p_id = 1
	noun_box = show_noun(p_id)


