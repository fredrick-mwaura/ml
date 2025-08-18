from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.sampling import BayesianModelSampling
from collections import Counter

"""
RAIN --------> MAINTEINANCE
 |              |
 |              |
 |              |
 |              |
TRAIN -------> APPOINTMENT

"""

# Define the Bayesian Network structure
model = DiscreteBayesianNetwork([
    ('rain', 'maintenance'),
    ('rain', 'train'),
    ('maintenance', 'train'),
    ('train', 'appointment')
])

# Conditional Probability Distributions (CPDs) / conditional probability tables
"""
syntax:
TabularCPD(
    variable=,          -- the node (var name)
    variable_card,      -- possible states of the node
    values,             -- probability values (2D list) ! np.array
    evidence=           -- parent (if any)
    evidence_card=      -- no of states for each parent
)
"""
rain_cpd = TabularCPD(
    variable='rain',
    variable_card=3,
    values=[[0.7], [0.2], [0.1]],
    state_names={'rain': ['none', 'light', 'heavy']}
)

maintenance_cpd = TabularCPD(
    variable='maintenance',
    variable_card=2,
    values=[
        [0.4, 0.2, 0.1],
        [0.6, 0.8, 0.9]
    ],
    evidence=['rain'],
    evidence_card=[3],
    state_names={
        'maintenance': ['yes', 'no'],
        'rain': ['none', 'light', 'heavy']
    }
)

train_cpd = TabularCPD(
    variable='train',
    variable_card=2,
    values=[
        [0.8, 0.9, 0.6, 0.7, 0.4, 0.5],
        [0.2, 0.1, 0.4, 0.3, 0.6, 0.5]
    ],
    evidence=['rain', 'maintenance'],
    evidence_card=[3, 2],
    state_names={
        'train': ['on time', 'delayed'],
        'rain': ['none', 'light', 'heavy'],
        'maintenance': ['yes', 'no']
    }
)

appointment_cpd = TabularCPD(
    variable='appointment',
    variable_card=2,
    values=[
        [0.9, 0.6],  # P(appointment=attend | train)
        [0.1, 0.4]   # P(appointment=miss | train)
    ],
    evidence=['train'],
    evidence_card=[2],
    state_names={
        'appointment': ['attend', 'miss'],
        'train': ['on time', 'delayed']
    }
)

# Add CPDs to the model
model.add_cpds(rain_cpd, maintenance_cpd, train_cpd, appointment_cpd)

# Check if the model is valid
assert model.check_model()

# Perform rejection sampling
sampler = BayesianModelSampling(model)
N = 10000
data = []

# Generate all samples at once for better performance
samples = sampler.forward_sample(size=N)

# Filter samples where train is delayed
delayed_samples = samples[samples['train'] == 'delayed']
data = delayed_samples['appointment'].tolist()

print("Appointment distribution when train is delayed:")
print(Counter(data))