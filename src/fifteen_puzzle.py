import random
import graph_search


class FifteenPuzzle:
    def __init__(self, solution_depth):
        self.puzzle = [1, 2, 3, 4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        self.solution = self.puzzle.copy()
        self.solution_depth = solution_depth
        # possible actions in order: right, right+down, down, left+down, left, left+up, up, right+up
        self.possible_action = [1, 5, 4, 3, -1, -5, -4, -3]
        self.possible_action_map = {"right": 1, "down_right": 5, "down": 4, "down_left": 3, "left": -1, "up_left": -5,
                                    "up": -4, "up_right": -3}
        self.cost = {1: 1, 5: 3, 4: 1, 3: 3, -1: 1, -5: 3, -4: 1, -3: 3}
        self.actions = []

    def generate_random_puzzle(self):
        for i in range(self.solution_depth):
            position_zero = self.get_position_zero()
            action = self.perform_random_action()
            print(str(i) + ", zero : " + str(position_zero) + " action: " + str(action))

    def swap_tiles(self, position_zero, action):
        position_new = position_zero + action
        self.puzzle[position_zero] = self.puzzle[position_new]
        self.puzzle[position_new] = 0

    def pretty_print(self):
        i = 0
        while i < (len(self.puzzle)):
            print(str(self.puzzle[i]) + '\t' + str(self.puzzle[i + 1]) + '\t' + str(self.puzzle[i + 2]) + '\t' +
                  str(self.puzzle[i + 3]))
            i = i + 4

    def perform_random_action(self):
        success = False
        while not success:
            rand = random.randint(0, 7)
            action = self.possible_action[rand]
            success = self.perform_action_generation(action)
        return action

    def perform_action_generation(self, action):
        position_zero = self.get_position_zero()
        if 0 <= position_zero + action < 16:
            if position_zero <= 3 and (action == -5 or action == -4 or action == -3):
                return False
            if position_zero % 4 == 0 and (action == -5 or action == -1 or action == 3):
                return False
            if position_zero >= 12 and (action == 5 or action == 4 or action == 3):
                return False
            if ((position_zero + 1) % 4 == 0) and (action == 5 or action == 1 or action == -3):
                return False
            else:
                if len(self.actions) > 0:
                    if action == (self.actions[len(self.actions) - 1] * (-1)):
                        # continue to prevent loops
                        return False
                self.actions.append(action)
                self.swap_tiles(position_zero, action)
                return True
        else:
            return False

    def take_action(self, action):
        position_zero = self.get_position_zero()
        if graph_search.is_action_possible(action, position_zero):
            self.actions.append(action)
            self.swap_tiles(position_zero, action)
            return True
        return False

    def get_position_zero(self):
        for i in range(len(self.puzzle)):
            if self.puzzle[i] == 0:
                return i

        return -1


def main():
    solution_depth = 2
    fifteen_puzzle = FifteenPuzzle(solution_depth)
    fifteen_puzzle.generate_random_puzzle()
    fifteen_puzzle.puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    fifteen_puzzle.pretty_print()


if __name__ == '__main__':
    main()
