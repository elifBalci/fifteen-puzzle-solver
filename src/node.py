class Node:
    def __init__(self, action, parent, state, cost, heuristic_cost):
        self.heuristic_cost = heuristic_cost
        self.action = action
        self.cost = cost
        self.parent = parent
        self.state = state



