from logic import *

rain = Symbol("rain") #it rained
hagrid = Symbol("hagrid") #visited hagrid
dumbledore = Symbol("dumbledore") #visited dumbledore

Sentence = And(rain, hagrid)

print(Sentence.formula())

# knowledge = Implication(Not(rain), hagrid)
# print(knowledge.formula())

knowledge = And(
    
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)
# print(knowledge.formula())

print(model_check(knowledge, rain))

