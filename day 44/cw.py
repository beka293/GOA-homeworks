def rps(p1, p2):
    if p1 == p2: return "Draw!"
    return "Player 1 won!" if p2 == {"rock": "scissors", "scissors": "paper", "paper": "rock"}[p1] else "Player 2 won!"





