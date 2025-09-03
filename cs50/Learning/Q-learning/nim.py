import random

def train(episodes=200, alpha=0.1, gamma=0.9, epsilon=0.1):
    Q = {}

    def get_q(state, action):
        return Q.get((state, action), 0.0)

    def valid_actions(s):
        return [a for a in range(1, 4) if a <= s]

    def choose_action(state):
        if random.random() < epsilon:
            return random.choice(valid_actions(state))
        else:
            qs = [get_q(state, a) for a in valid_actions(state)]
            max_q = max(qs)
            best_actions = [a for a in valid_actions(state) if get_q(state, a) == max_q]
            return random.choice(best_actions)
    for episode in range(1, episodes + 1):
        state = 15
        history = []

        print(f"\n🎮 Episode {episode} — Starting pile: {state}")

        while state > 0:
            action = choose_action(state)
            print(f"AI chooses {action} (pile left: {state} → {state - action})")
            history.append((state, action))
            state -= action

        # Last move wins
        for i, (s, a) in enumerate(reversed(history)):
            reward = 1 if i == 0 else -1
            next_state = s - a
            next_qs = [get_q(next_state, a2) for a2 in valid_actions(next_state)]
            max_next_q = max(next_qs) if next_qs else 0
            old_q = get_q(s, a)
            Q[(s, a)] = old_q + alpha * (reward + gamma * max_next_q - old_q)

    def ai_move(state):
        qs = [get_q(state, a) for a in valid_actions(state)]
        max_q = max(qs)
        best_actions = [a for a in valid_actions(state) if get_q(state, a) == max_q]
        return random.choice(best_actions)

    return ai_move
def play(ai):
    pile = 15
    print("Welcome to Fred's Nim 😇! You vs AI. Take 1–5 objects per turn.")
    
    while pile > 0:
        print(f"\nPile size: {pile}")
        
        # Human move
        try:
            move = int(input("Your move (1–5): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if move < 1 or move > 5 or move > pile:
            print("Invalid move. Try again.")
            continue

        pile -= move
        if pile == 0:
            print("You win!")
            return

        # AI move
        ai_move = ai(pile)
        print(f"AI takes {ai_move}")
        pile -= ai_move
        if pile == 0:
            print("AI wins!")
            return
