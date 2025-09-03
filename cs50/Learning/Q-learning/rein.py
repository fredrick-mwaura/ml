# Steps for Reinforcement Learning
"""
1. The Agent is at state zero in an environment:

2. It will take an action based on a policy:
  - The policy can be random or based on a strategy (e.g., epsilon-greedy)

3. It will receive a reward or punishment based on that action.

4.By learning from previous moves, the agent will update its policy to maximize future rewards / optimize.

5. Repeat and evaluate:
  - Continue the process for multiple episodes, periodically evaluating the agent's performance.
  - Adjust hyperparameters as needed to improve learning.
"""
# --- IGNORE ---v

"""
  Q(s, a) ← Q(s, a) + a((r + y maxa' Q(s', a')) - Q(s, a))

ε-greedy ==> explore && exploit
ε - how often to explore(random action)

"""
