import sys
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml
import string
import random
import shelve
import numpy as np
import scipy.sparse as sparse
import cPickle as pickle
from collections import defaultdict, namedtuple
import codecs, json

def randomString(length=16):
	return "".join([random.choice(string.letters) for _ in xrange(length)])

def token((disp, repr)):
	return {'disp':disp, 'repr':repr}

def randomText(length, words):
	return " ".join([random.choice(words) for _ in xrange(length)])

def remove_prefix(w):
	if '_' in w:
		return w.split('_', 1)[1]
	else:
		return w

def word_shuffle(words_list):
	random.shuffle(words_list)
	#words_list = words_list[:500]
	words_list = words_list[:500]
	#vocab_list = set(words_list)
        return words_list

def read_file(filename):
	f = codecs.open(filename,"r","utf-8")
	text = f.read()
	f.close()
	return text

def devide_dictionary(words, div_n):
	words = word_shuffle(words)
    	l = len(words)
    	size = l / div_n + (l % div_n > 0)
    	return [words[i:i+size] for i in range(0, l, size)]


random.seed(2014)

icd9_words = read_file('data/one_icd9_words_only.txt')
rad_words = read_file('data/one_rad_words_only.txt')
wjn_words = read_file('data/one_wjn_words_only.txt')
come_words = read_file('data/one_come_words_only.txt')


icd9_words = icd9_words.split("\r\n")
icd9_words[-1] = icd9_words[-1].strip("\n")

come_words = come_words.split("\r\n")
come_words[-1] = come_words[-1].strip("\n")

rad_words = rad_words.split("\n")
wjn_words = wjn_words.split("\n")


"""
wjn_words = file('data/wjn_words_only.txt').read().splitlines()
rad_words = file('data/rad_words_only.txt').read().splitlines()
icd9_words = file('data/icd9_words_only.txt').read().splitlines()
come_words = file('data/come_words_only.txt').read().splitlines()
DIV_N = 30
#Japanese words
wjn_words = devide_dictionary(wjn_words, DIV_N)
#Radiology words
rad_words = devide_dictionary(rad_words, DIV_N)
#ICD9 disease name or chief complaint
icd9_words = devide_dictionary(icd9_words, DIV_N)
#Come Dictionary
come_words = devide_dictionary(come_words, DIV_N)
"""

def randomPatient(p_id, f, i_name):
	Time_points = 1
	global vocab
	p_dict = {}
	#pat['index'] = randomString()
        tmp = ''
	pat_id = randomString()
	change_id = random.randint(0, Time_points-1)
        #時系列ごとに疾患が増えて行 -> MD commentの所に加えて行く

        for t in xrange(Time_points):
		random_int = 2
        	dig_code = randomText(1, icd9_words)
        	ana_pos = randomText(random_int , rad_words)
		if int(t) == int(change_id):
			tmp_Triage = dig_code + ' ' + ana_pos + ' ' + randomText(random_int + 1, wjn_words)
		else:
			tmp_Triage = dig_code + ' ' + ana_pos + ' ' + randomText(random_int, wjn_words)
                tmp += tmp_Triage
                t_dict = {}
                word_list = tmp + ' ' + randomText(random_int, come_words)
                word_list = word_list.split(" ")
		#Shuffle words to predict order
		random.shuffle(word_list)
                word_list = " ".join(word_list)
		age_tmp = str(np.random.choice(range(20,80)))
		sex_tmp = np.random.choice(['M', 'F'])[0]
		t_dict = {
				"patient_id": pat_id,
				"Subject" : dig_code,
				"Object" : tmp_Triage,
				"Assessment" : word_list,
				"Plan" : word_list,
				"Age" : age_tmp,
				"Sex" : sex_tmp,
				"Time" : t,
				"change_point" : change_id
			}
		p_dict[t] = t_dict
	label_1 = { "index": { "_index": "test2", "_type": "Patient", "_id": "%s"%p_id } }
	#label_2 = { "id":"%s"%p_id, "Age":"%s"%age_tmp, "Sex":"%s"%sex_tmp, "Department":"Not Yet" }
	#label_3 = { "index": { "_index": "test2", "_type":  "karte", "_parent": "%s"%p_id } }
	#label_4 = { "id": "%s"%p_id, "Subject": "%s"%dig_code, "Object":"%s"%tmp_Triage, "Assesment":"%s"%word_list, "Plan":"%s"%word_list }

	f.write("{ \"index\": { \"_index\": \"%s\", \"_type\": \"Patient\", \"_id\": \"%s\" } }"%(i_name, p_id))
	f.write("\n")
        f.write("{ \"id\":\"%s\", \"Age\":\"%s\", \"Sex\":\"%s\", \"Department\":\"Not Yet\" }"%(p_id, age_tmp, sex_tmp))	
	f.write("\n")
	f.write("{ \"index\": { \"_index\": \"%s\", \"_type\":  \"karte\", \"_parent\": \"%s\" } }"%(i_name, p_id))
	f.write("\n")
	f.write("{ \"id\": \"%s\", \"Subject\": \"%s\", \"Object\": \"%s\", \"Assesment\": \"%s\", \"Plan\": \"%s\" }"%(p_id, dig_code, tmp_Triage, word_list, word_list))
	f.write("\n")

	label = {
			"patient_id": pat_id,
                        "change_point" : change_id
		}
        return p_dict, label, label_1

def generate_patients(n):
    for _ in xrange(n):
        pat = randomPatient()

    jsonstring = json.dumps(pat, ensure_ascii=False)
    return jsonstring

if __name__ == "__main__":

    try:
        n = int(sys.argv[1])
    except:
        print "usage: python generate_patients.py numPatients"
        sys.exit()

    pat_dics = {}
    p_labels = {}
    f = codecs.open("elastic_search/es_test.txt","w","utf-8")

    index_name = sys.argv[2]
    for t in xrange(n):
       pat_dics[t], p_labels[t], lab = randomPatient(t,f, index_name)

    f.close()

    f.close()
    #jsonstring = json.dumps(pat_dics, ensure_ascii=False)
    #label_jsonstring = json.dumps(p_labels, ensure_ascii=False)

    #f = codecs.open("output/one_json_time_series_patient.json","w","utf-8")
    #f_label = codecs.open("output/one_p_labels.json","w","utf-8")
    #f = open("tmp/json_time_series_patient.json", "w")
    #json.dump(pat_dics, f, ensure_ascii=False)
    #json.dump(p_labels, f_label, ensure_ascii=False)


