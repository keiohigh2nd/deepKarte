# -*- coding: utf-8 -*-
import json, random, MeCab
import detection, codecs, math
import collections
import numpy as np
import in_out


def vectorlize_Plist(patient_plist):
	#病気名を形態素分析してベクトル化した
	#ただしindexは病名だけで有効である
        from sklearn.feature_extraction.text import CountVectorizer
        vectorizer = CountVectorizer(min_df=1)
        X = vectorizer.fit_transform(patient_plist)
        index = vectorizer.get_feature_names()
        return X.toarray(), index		

def find_similar_patients_by_p(matrix, query_id):
	sim_patients = []
	counter = 0
	for row_id in xrange(len(matrix)):
		#類似患者の定義
		tmp_dist = matrix[query_id] - matrix[row_id]
		tmp = np.power(tmp_dist, 2).sum()
		if tmp < 2:
			sim_patients.append(row_id)
	return sim_patients

if __name__ == "__main__":

	#類次患者を#Pで絞る. ID - #P
	fw = codecs.open("processed_data/patinet_plist.txt","r","utf-8")
	lines = fw.readlines()
	fw.close()
	num_patients = len(lines)

	patient_plist = []
	for line in lines:
		tmp = line.split(",")
		patient_plist.append(tmp[1].strip("#"))

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
		similar_patients_id = find_similar_patients_by_p(plist_mat, i)
		print "Number of similar patient is %s"%len(similar_patients_id)
		f.write(str(i))
		f.write(',')
		for j in similar_patients_id:
			f.write(str(j))
			f.write(',')
		f.write('\n')
	f.close()
