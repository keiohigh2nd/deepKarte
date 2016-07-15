import kanji, vectorlize, in_out

def process(text):
	chrs = kanji.hasKanji(text)
	return chrs

if __name__ == "__main__":
        #count, index = load_sample()

        p_text, p_json = in_out.read_json("output/json_multi_lab_time_series_patient.json")

        #Unidentified two spaces
        num_patients = len(p_json)
	p = 1
	Time = len(p_json["%s"%p])

	
	tmp_chr = []
        for p in xrange(num_patients):
		tmp_array = []
		for t in xrange(Time):
			lab = "WBC"
                	tmp_array.append(p_json["%s"%p]["%s"%t][lab])
                	tmp_chr.append(process(p_json["%s"%p]["%s"%t]["A/P"]))
	
	print tmp_chr
	count, index = vectorlize.dictionarize_text(tmp_chr)
