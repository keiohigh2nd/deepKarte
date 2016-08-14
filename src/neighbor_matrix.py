import numpy as np


def neighbor_matrix(arr_text, index_corpus):
        s_matrix = np.zeros((len(index_corpus), len(index_corpus)))
        arr_text = arr_text.split(" ")
        del arr_text[-1]
        del arr_text[0]
        for t in xrange(len(arr_text)):
                try:
                        i = index_corpus.index(arr_text[t])
                        if t > 0:
                                m_1 = index_corpus.index(arr_text[t-1])
                                s_matrix[i][m_1] += 1
                        if t < len(arr_text)-1:
                                m1 = index_corpus.index(arr_text[t+1])
                                s_matrix[i][m1] += 1
                        if t > 1:
                                m_2 = index_corpus.index(arr_text[t-2])
                                s_matrix[i][m_2] += 1
                        if t < len(arr_text)-2:
                                m1 = index_corpus.index(arr_text[t+2])
                                s_matrix[i][m2] += 1
                except:
                        pass
        return s_matrix



