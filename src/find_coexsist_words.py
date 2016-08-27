# -*- coding: utf-8 -*-
import json, random, MeCab
import detection, codecs, math
import collections
import numpy as np
import in_out

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
	N = 100
	max_N_list = []
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
	#病名が類似している類似患者は先に割り出しておく
	#共起単語の発見
	#similar_patients_idはcsvで開けて、index_corpusも開ける
	tmp = show_noun(2)	
	for t in tmp:
		print t.encode('utf-8')

