from model import model

# Calculate probability for a given observation
"""""""""""""""""""""""""""""""""""rain,maintenance, train,  meeting """""""""
probability = model.probability([["none", "no", "on time", "attend"]])
"""
likelihood of missing the meeting despite all othe being postive
"""


probability = model.probabilty([["none", "no", "on time", "miss"]])

print(probability)
