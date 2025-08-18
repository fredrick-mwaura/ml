from model import infer
# Evidence: train = "delayed"
evidence = {'train': 'delayed'}

# Query all other nodes
query_vars = ['rain', 'maintenance', 'appointment']

result = {}
for var in query_vars:
    posterior = infer.query(variables=[var], evidence=evidence)
    result[var] = posterior

# Print nicely
for var, dist in result.items():
    print(var)
    states = dist.state_names[var]
    probs = dist.values
    for s, p in zip(states, probs):
        print(f"  {s}: {p:.4f}")
