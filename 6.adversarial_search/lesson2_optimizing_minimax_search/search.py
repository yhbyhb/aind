
from minimax import minimax_decision

def get_action(gameState, depth_limit):
    # TODO: Implement a function that calls minimax_decision
    # for each depth from 1...depth_limit (inclusive of both endpoints)
    m = None
    for d in range(1, depth_limit+1):
        m = minimax_decision(gameState, d)
    return m