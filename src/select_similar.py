# -*- coding: utf-8 -*-
import numpy as np
import in_out

def return_patient_index(p_id):
	p_text, p_json = in_out.read_json("output/one_json_time_series_patient.json")
	for i in xrange(len(p_json)):
		if p_id == p_json["%s"%i]["0"]["patient_id"]:
			return i

def return_patient_ID(p_index):
	p_text, p_json = in_out.read_json("output/one_json_time_series_patient.json")
	return p_json["%s"%p_index]["0"]["patient_id"]
	
def calc_dist(a, b):
	N = len(a)
	tmp_Matrix = a-b
	val = 0
	mat = np.fabs(tmp_Matrix)
	return mat.sum()

def find_similar_patient_byID(p_id):
	#This is for patient ID
	p_text, p_json = in_out.read_json("output/one_json_time_series_patient.json")
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
	print min_id
	return return_patient_ID(min_id)

def find_similar_patient_byPlist(pid, plist):
        #This is for patient ID

        with open("processed_data/Neighbor_mat.npy", "rb") as npy:
                tmp_m = np.load(npy)

        min_value = 100000
        min_id = 0
        for i in plist:
                tmp_min = calc_dist(tmp_m[int(i)], tmp_m[int(pid)])
                if int(min_value) > int(tmp_min):
                        min_value = tmp_min
                        min_id = i
        return min_id


def find_similar_from_p(pid):
	f = open('processed_data/similar_plist.txt')
	lines = f.readlines()
	f.close()

	tmp = lines[pid].split(",")
	del tmp[0]
	return tmp

if __name__ == "__main__":
	#Patient list from #Problem list
	pid = 20
	plist = find_similar_from_p(pid)
	del plist[0]
	del plist[-1]

	patient_id = "quVWwJbugJYxynem"
	print plist
	print find_similar_patient_byPlist(pid, plist)
	
