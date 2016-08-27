from causalinference import CausalModel
from causalinference.utils import random_data

Y, D, X = random_data()
causal = CausalModel(Y, D, X)

#Propensity Score
causal.est_propensity_s()
