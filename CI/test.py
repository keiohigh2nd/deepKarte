# -*- coding: utf-8 -*-
from nose.tools import *
import numpy as np

def test_propensity():
	import causalinference.core.data as d
	import causalinference.core.propensity as p
	from utils import random_data


	D = np.array([0, 0, 0, 1, 1, 1])
	X = np.array([[7, 8], [3, 10], [7, 10], [4, 7], [5, 10], [9, 8]])
	Y = random_data(D_cur=D, X_cur=X)
	print Y

	data = d.Data(Y, D, X)
	propensity = p.Propensity(data, [0, 1], [])
	print propensity

def causal_ATE():
	from causalinference import CausalModel
	from utils import random_data

        D = np.array([0, 0, 0, 1, 1, 1])
        X = np.array([[7, 8], [3, 10], [7, 10], [4, 7], [5, 10], [9, 8]])
        Y = random_data(D_cur=D, X_cur=X)
	print Y

	causal = CausalModel(Y, D, X)
	#causal.est_via_ols()
	#print causal.estimates	
	
	causal.est_propensity_s()
	print causal.propensity
	# -*- coding: utf-8 -*-
	#プロペンシティスコアを元に自分でマッチングすれば良い。

	#estimated propensity scores
	print causal.propensity['fitted']	
	
	#結果はYだから

if __name__ == "__main__":
	causal_ATE()
