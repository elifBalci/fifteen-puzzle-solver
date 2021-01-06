from fifteen_puzzle import FifteenPuzzle
from graph_search import GraphSearch


class Main:
    def __init__(self, solution_depth, algorithm):
        self.solution_depth = solution_depth
        self.fifteen_puzzle = None
        self.algorithm = algorithm
        self.graph_search = None
        self.create_puzzle_and_solver()
        self.algorithm_list = ["ucs", "a_star_1", "a_star_2"]

    def create_puzzle_and_solver(self):
        self.fifteen_puzzle = FifteenPuzzle(self.solution_depth)
        self.fifteen_puzzle.generate_random_puzzle()
        print("----puzzle----")
        self.fifteen_puzzle.pretty_print()
        self.graph_search = GraphSearch(self.fifteen_puzzle, self.algorithm)


main = Main(2, "ucs")
