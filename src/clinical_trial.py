import json, random, codecs
import one_hot_vector

def test(p_json):
	fa = codecs.open("output/d_lab.json","w","utf-8")
	num_patients = len(p_json)
	p = 1
	Time = len(p_json["%s"%p])

	p_dict = {}
	for p in xrange(num_patients):
		t = random.randint(0,2)
		fa.write("{")	
		fa.write('\"Age\" : %s,'% p_json["%s"%p]["%s"%t]["Age"])
		fa.write('\"Time\" : %s,'% p_json["%s"%p]["%s"%t]["Time"])
		fa.write('\"BP\" : %s,'% p_json["%s"%p]["%s"%t]["BP"])
		fa.write('\"WBC\" : %s,'% p_json["%s"%p]["%s"%t]["WBC"])
		fa.write('\"CRP\" : %s,'% p_json["%s"%p]["%s"%t]["CRP"])
		fa.write('\"HR\" : %s,'% p_json["%s"%p]["%s"%t]["HR"])
		fa.write('\"BS\" : %s,'% p_json["%s"%p]["%s"%t]["BS"])
		if p == num_patients-1:
	        	fa.write("}")
		else:
	        	fa.write("},")
		
	fa.close()
	


if __name__ == "__main__":
        #count, index = load_sample()

        p_text, p_json = one_hot_vector.read_json("output/json_multi_lab_time_series_patient.json")

        #Unidentified two spaces
        num_patients = len(p_json)
        p = 1
        Time = len(p_json["%s"%p])

	test(p_json)
