from causalinference import CausalModel
from causalinference.utils import random_data

Y, D, X = random_data()
causal = CausalModel(Y, D, X)

#Estimate ATE
causal.est_via_ols()
causal.est_via_weighting()
causal.est_via_blocking()
causal.est_via_matching(bias_adj=True)

