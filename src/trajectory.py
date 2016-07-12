import one_hot_vector

if __name__ == "__main__":
        #count, index = load_sample()

        p_text, p_json = one_hot_vector.read_json("output/json_multi_lab_time_series_patient.json")

        #Unidentified two spaces
        num_patients = len(p_json)
	p = 1
	Time = len(p_json["%s"%p])
	
        for p in xrange(num_patients):
		for t in xrange(Time):
                	tmp = p_json["%s"%p]["%s"%t]["WBC"]
			print tmp
