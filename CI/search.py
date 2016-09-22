

def find_similar_patient_bycontent(arr, N):

        #Database
        with open("processed_data/Neighbor_mat.npy", "rb") as npy:
                pmat = np.load(npy)

        #Order Index
        tmp_min_arr = []
        for i in xrange(len(pmat)):
                tmp_min = calc_dist(pmat[i], arr)
                tmp_min_arr.append(tmp_min)

        it = np.argsort(tmp_min_arr)  #sorted index

        p_text, p_json = in_out.read_json("output/json_multi_lab_time_series_patient.json")
        #Output Search Result
        print get_counter_factual(it, N, p_json)




if __name__ == "__main__":
        #ここがsearch queryのtext
        filename = "textsum/log_root/decode/decode1474332050"

