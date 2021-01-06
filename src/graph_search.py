import time
from node import Node


def check_similarity(puzzle1, puzzle2):
    for i in range(len(puzzle1)):
        if not puzzle1[i] == puzzle2[i]:
            return False
    return True


def trace_to_root(node):
    solution = []
    while node is not None:
        solution.append(node.action)
        node = node.parent
    solution.reverse()
    print("Solution is ", solution)
    return solution


def is_action_possible(action, position_of_zero):
    if position_of_zero == 0:
        if action == 1 or action == 5 or action == 4:
            return True
    if position_of_zero == 1:
        if action == 1 or action == 5 or action == 4:
            return True
    if position_of_zero == 2:
        if action == -1 or action == +1 or action == 3 or action == 4 or action == 5:
            return True
    if position_of_zero == 3:
        if action == -1 or action == 3 or action == 4:
            return True
    if position_of_zero == 4:
        if action == -4 or action == 4 or action == -3 or action == 5 or action == 1:
            return True
    if position_of_zero == 7:
        if action == -4 or action == 4 or action == 3 or action == -5 or action == -1:
            return True
    if position_of_zero == 8:
        if action == -4 or action == 4 or action == -3 or action == 5 or action == 1:
            return True
    if position_of_zero == 11:
        if action == -4 or action == 4 or action == 3 or action == -5 or action == -1:
            return True
    if position_of_zero == 12:
        if action == 1 or action == -3 or action == -4:
            return True
    if position_of_zero == 13:
        if action == 1 or action == -1 or action == -3 or action == -4 or action == -5:
            return True
    if position_of_zero == 14:
        if action == 1 or action == -1 or action == -3 or action == -4 or action == -5:
            return True
    if position_of_zero == 15:
        if action == -1 or action == -5 or action == -4:
            return True
    if position_of_zero == 5 or position_of_zero == 6 or position_of_zero == 9 or position_of_zero == 10:
        return True
    else:
        return False


def take_action(puzzle, action):
    position_of_zero = None
    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            position_of_zero = i
    if is_action_possible(action, position_of_zero):
        position_new = position_of_zero + action
        puzzle[position_of_zero] = puzzle[position_new]
        puzzle[position_new] = 0
    return puzzle


class GraphSearch:
    def __init__(self, fifteen_puzzle, algorithm):
        self.iterative_lengthening = None
        self.switch = {'a_star_1': self.execute_algorithm, 'a_star_2': self.execute_algorithm,
                       'ucs': self.execute_algorithm}
        self.algorithm = algorithm
        self.fifteen_puzzle = fifteen_puzzle
        self.expand_count = 0
        self.opened = 0
        self.explored = []
        self.frontier = []
        self.max_nodes_in_mem = 0
        self.length_limit = 1
        self.start()

    def start(self):
        start_time = time.time()
        self.execute_algorithm()
        print("Used strategy: ", self.algorithm)
        print("Expanded", self.expand_count, " nodes")
        print("Number of nodes stored in memory", self.opened, " nodes")
        print("Took", time.time() - start_time, " seconds to run")

    def execute_algorithm(self):
        # add to frontier: not allowable, not duplicates
        # sort the frontier
        # pop from frontier
        parent = None
        current_cost = 0
        while not self.check_goal_state():
            self.expand(parent, current_cost)
            current_cost, parent = self.pop()
            self.max_nodes_in_mem = max(self.max_nodes_in_mem, (len(self.frontier) + len(self.explored)))
            print("Max nodes in memory is : " + str(self.max_nodes_in_mem))
            print("Current cost is: " + str(current_cost))
        trace_to_root(parent)
        return True

    def expand(self, parent, current_cost):
        self.expand_count = self.expand_count + 1
        for i in range(len(self.fifteen_puzzle.possible_action)):
            position_zero = self.fifteen_puzzle.get_position_zero()
            if is_action_possible(self.fifteen_puzzle.possible_action[i], position_zero):
                action = self.fifteen_puzzle.possible_action[i]
                cost = current_cost + self.fifteen_puzzle.cost[action]
                heuristic_cost = cost
                if self.algorithm == "a_star_1":
                    heuristic_cost = heuristic_cost + self.heuristic_h1()
                if self.algorithm == "a_star_2":
                    heuristic_cost = heuristic_cost + self.heuristic_h2()
                node = Node(action, parent, self.fifteen_puzzle.puzzle.copy(), cost, heuristic_cost)
                if not self.is_node_already_explored(node):
                    self.frontier.append(node)
                    self.opened = self.opened + 1
        self.sort_frontier()

    def is_node_already_explored(self, node):
        # check action, parent, state
        node_state = take_action(node.state.copy(), node.action)
        for i in range(len(self.explored)):
            explored_node = self.explored[i]
            explored_state = take_action(explored_node.state.copy(), explored_node.action)
            if check_similarity(node_state, explored_state):
                return True
        return False

    def pop(self):
        if not self.frontier:
            return 0, False
        action_to_take = self.frontier.pop(0)
        self.fifteen_puzzle.puzzle = action_to_take.state
        current_cost = action_to_take.cost
        self.fifteen_puzzle.take_action(action_to_take.action)
        self.explored.append(action_to_take)
        print()
        print("action is: " + str(action_to_take.action))
        self.fifteen_puzzle.pretty_print()
        return current_cost, action_to_take

    def sort_frontier(self):
        self.frontier.sort(key=lambda x: x.heuristic_cost)

    def check_goal_state(self):
        puzzle = self.fifteen_puzzle.puzzle
        goal = self.fifteen_puzzle.solution
        for i in range(len(puzzle)):
            if not puzzle[i] == goal[i]:
                return False
        return True

    def heuristic_h1(self):
        # number of misplaced tiles in the puzzle
        length = 15  # len(self.fifteen_puzzle.puzzle)
        number_of_misplaced = 0
        for i in range(length):
            if self.fifteen_puzzle.solution[i] != self.fifteen_puzzle.puzzle[i]:
                number_of_misplaced = number_of_misplaced + 1
        # number_of_misplaced = number_of_misplaced - 1  # eliminate tile 0
        return number_of_misplaced

    def heuristic_h2(self):
        # city block distance
        length = 15
        city_block_dist = 0
        for i in range(length):
            y_local = int(i / 4)
            x_local = i - y_local

            true_location = 0
            for j in range(length):
                if self.fifteen_puzzle.puzzle[i] == self.fifteen_puzzle.solution[j]:
                    true_location = j

            y_true = int(true_location) / 4
            x_true = true_location - y_true
            city_block_dist = city_block_dist + (abs(x_true - x_local) + abs(y_true - y_local))

        return city_block_dist
