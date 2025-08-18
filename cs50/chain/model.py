from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference

# 1. Define the DBN model
model = DBN()

# Add edges: Weather_t -> Weather_t+1
model.add_edges_from([(('Weather', 0), ('Weather', 1))])

# 2. Define CPDs (only use variable names, not tuples with time indices)

# Initial distribution P(Weather_0)
cpd_start = TabularCPD(
    variable='Weather',
    variable_card=2,
    values=[[0.5], [0.5]],
    state_names={'Weather': ['sun', 'rain']}
)

# Transition distribution P(Weather_t+1 | Weather_t)
cpd_transition = TabularCPD(
    variable='Weather2',
    variable_card=2,
    evidence=['Weather'],
    evidence_card=[2],
    values=[
        [0.8, 0.3],  # P(sun | sun), P(sun | rain)
        [0.2, 0.7]   # P(rain | sun), P(rain | rain)
    ],
    state_names={'Weather': ['sun', 'rain']}
)

# Add CPDs (pgmpy will align them to slices automatically)
model.add_cpds(cpd_start, cpd_transition)

# 3. Initialize inference
dbn_inf = DBNInference(model)

# 4. Forward sampling (simulate a sequence)
samples = []
state = {'Weather': 'sun'}  # initial state
for t in range(10):
    q = dbn_inf.forward_inference([('Weather', t)], evidence={('Weather', t): state['Weather']})
    prob_sun = q[('Weather', t)].values[0]
    state['Weather'] = 'sun' if prob_sun > 0.5 else 'rain'
    samples.append(state['Weather'])

print(samples)
