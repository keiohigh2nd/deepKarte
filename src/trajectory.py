import one_hot_vector

def get_index():
        f = codecs.open("processed_data/word_index.txt","r","utf-8")
        index_corpus = f.read().split(",")
        f.close()
	return index_corpus

def get_trajectory():
	pass

if __name__ == "__main__":
        #count, index = load_sample()

        p_text, p_json = one_hot_vector.read_json("output/json_multi_lab_time_series_patient.json")

        #Unidentified two spaces
        num_patients = len(p_json)
	p = 1
	Time = len(p_json["%s"%p])

	word_index = get_index()	

        for p in xrange(num_patients):
		tmp_array = []
		for t in xrange(Time):
			lab = "WBC"
                	tmp_array.append(p_json["%s"%p]["%s"%t][lab])
