# -*- coding: utf-8 -*-
import json
import numpy as np

def read_json(filename):
        f = open(filename, 'r')
        jsonData = json.load(f,"utf-8")
        text = json.dumps(jsonData)
        f.close()
        return text, jsonData

def parse_text(text, m):
        encode_text = text.encode('utf-8')
        res = m.parse(encode_text)
        return res.decode('utf-8')


def calc_dist(a, b):
        N = len(a)
        tmp_Matrix = a-b
        val = 0
        mat = np.fabs(tmp_Matrix)
        return mat.sum()

def return_index():
	f = open("processed_data/word_index.txt", 'r')
	lines = f.read()
	lines = lines.split(",")
	f.close()
	return lines

def return_vector(arr_index, text):
        return arr_index.index(text)

def return_patient_index(p_id):
        p_text, p_json = in_out.read_json("output/one_json_time_series_patient.json")
        for i in xrange(len(p_json)):
                if p_id == p_json["%s"%i]["0"]["patient_id"]:
                        return i

def return_patient_ID(p_index):
        p_text, p_json = in_out.read_json("output/one_json_time_series_patient.json")
        return p_json["%s"%p_index]["0"]["patient_id"]


