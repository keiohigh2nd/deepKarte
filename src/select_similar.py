# -*- coding: utf-8 -*-
import numpy as np
import one_hot_vector

def return_patient_index(p_id):
        p_text, p_json = one_hot_vector.read_json("output/one_json_time_series_patient.json")
	for i in xrange(len(p_json)):
		if p_id == p_json["%s"%i]["0"]["patient_id"]:
			return i

def return_patient_ID(p_index):
	try:
		p_text, p_json = one_hot_vector.read_json("output/one_json_time_series_patient.json")
		return p_json["%s"%p_index]["0"]["patient_id"]
	except:
		print "This ID is not found"
	

def calc_dist(a, b):
	N = len(a)
	tmp_Matrix = a-b
	val = 0
	mat = np.fabs(tmp_Matrix)
	return mat.sum()

def find_similar_patient(p_id):
	p_index = return_patient_index(p_id)

	with open("processed_data/Neighbor_mat.npy", "rb") as npy:
        	tmp_m = np.load(npy)

	min_value = 10000
	min_id = 0
	for i in xrange(len(tmp_m)):
		if i == p_index:
			continue
		tmp_min = calc_dist(tmp_m[i], tmp_m[p_index])
		if int(min_value) > int(tmp_min):
			min_value = tmp_min
			min_id = i
	return return_patient_ID(min_id)

if __name__ == "__main__":
        #自分が検索されてしまう問題
	patient_id = "quVWwJbugJYxynem"
	ind = find_similar_patient(patient_id)
	print ind
