# -*- coding: utf-8 -*-
import numpy as np
from collections import Counter
import in_out, re, json 

def get_common_words(arr, N, p_json):
        p_text, p_json = in_out.read_json("output/json_multi_lab_time_series_patient.json")
        time = len(p_json["%s"%str(0)])

	import MeCab
	tagger = MeCab.Tagger('-Ochasen')

	counter = Counter()
	for n in xrange(N):
		texts = p_json["%s"%arr[n]]["%s"%(time-1)]["A/P"].strip("\n").encode("utf-8")
  		node = tagger.parseToNode(texts)
		while node:
      			word = node.surface.decode('utf-8')
			node = node.next
			if re.match(ur"^[ぁ-んーァ-ンー\u4e00-\u9FFF]+$", word) != None and len(word) != 1:
        			counter[word] += 1

	#Word2vecで近い言葉
	topk = 10
	i = 0
	for word, cnt in counter.most_common():
		if i > topk:
			break
		print word
		

def get_parallel_value(arr, N, p_json):
        time = len(p_json["%s"%str(0)])

	dic = []
	t = 0
	f = open("view/tparallel.json", "w")
	text = ""
	for n in xrange(N):
		tmp_text = " { \"name\": %s,\"CRP\": %s, \"HR\": %s, \"Age\":%s,\"BP\": %s,\"WBC\": %s,\"Time\": %s,\"BS\": %s }" % ( n, p_json["%s"%arr[n]]["%s"%t]["CRP"], p_json["%s"%arr[n]]["%s"%t]["HR"], p_json["%s"%arr[n]]["%s"%t]["Age"], p_json["%s"%arr[n]]["%s"%t]["BP"], p_json["%s"%arr[n]]["%s"%t]["WBC"], p_json["%s"%arr[n]]["%s"%t]["Time"], p_json["%s"%arr[n]]["%s"%t]["BS"] )
	        f.write(tmp_text)
		if n != N-1:
			f.write(",")
	f.close()	       

def get_time_value(arr, N, p_json):
	time = len(p_json["%s"%str(0)])
	f = open("processed_data/cumu.json", "w")

	dic = []
	time_series_data = []
        f = open("view/tchart.json", "w")
	for n in xrange(N):
            tmp = []
	    value = ""
	    for t in xrange(time):
            	ie = "[%s,%s],"%(t, p_json["%s"%str(arr[n])]["%s"%t]["WBC"])
		value += ie
	    value = "[" + value[0:-1] + "]"
	    f.write("{ key:%s, values:%s  }"%(n, str(value)))
	    tmp_json = {
			"key": n,
			"values": "[" + value + "]"
	    }
	    dic.append(tmp_json)

	    if n != N-1:       
	      f.write(",")
	f.close()

	return time_series_data	

def get_counterfatctual(arr, N, p_json, treatment, pmat):
	#extract what kind of treatment
	index = in_out.return_index()
	treatment_id = in_out.return_vector(index, str(treatment))
	num_patient = len(p_json)

	#get data from database
	target_p = []
	i = 0
	for p in pmat:
		for pt in p:
			if pt[treatment_id] > 0:
				target_p.append(i)
				break
		i += 1
	print target_p

	#Start Training
	y_ = []
	for i in xrange(num_patient):
		y.append(p_json["%s"%str(i)]["1"]["WBC"])

	t_ = np.zeros(num_patient)
	for t in target_p:
		np.zeros[t] = 1
	
	x_ = pmat	
	#feed to NN

def convert_to_vec(filename):
	f = open(filename, "r")
        lines = f.readlines()
        f.close()

        f_w = open("processed_data/word_index.txt", "r")
        word_index = f_w.read().strip("\n").split(",")
        f_w.close()       

        arr = np.zeros(len(word_index)-1)
        for line in lines:
            tmp = line[7:].strip("\n").split(" ")
            for word in tmp:
               id = word_index.index(word)
               arr[id] = 1
        return arr

def find_similar_patient_bycontent(arr, N):
	#N is the number of similar patient you want to take
	#Database
	with open("processed_data/Neighbor_mat.npy", "rb") as npy:
        	pmat = np.load(npy)

	#Order Index
        tmp_min_arr = []
	for i in xrange(len(pmat)):
		tmp_min = in_out.calc_dist(pmat[i], arr)
                tmp_min_arr.append(tmp_min)

        it = np.argsort(tmp_min_arr)  #sorted index
        
	p_text, p_json = in_out.read_json("output/json_multi_lab_time_series_patient.json")
        #Output Search Result
        #print get_time_value(it, N, p_json)
        #print get_common_words(it, N, p_json)
        #print get_parallel_value(it, N, p_json)
        treatment = "免疫"
	print get_counterfatctual(arr, N, p_json, treatment, pmat)

if __name__ == "__main__":
	#ここがsearch queryのtext
	filename = "textsum/log_root/decode/decode1474332050"
	sample_arr = convert_to_vec(filename)
        find_similar_patient_bycontent(sample_arr, 10)
