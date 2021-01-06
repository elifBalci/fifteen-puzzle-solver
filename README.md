# fifteen-puzzle-solver

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a00febaccb054b18bb22b1c020ea774a)](https://app.codacy.com/gh/elifBalci/fifteen-puzzle-solver?utm_source=github.com&utm_medium=referral&utm_content=elifBalci/fifteen-puzzle-solver&utm_campaign=Badge_Grade)

This project aims to create a random 15-puzzle with given solution depth and solve it with one of the specified algorithms. Diagonal moves allowed.
Available algorithms are: 

	- Uniform Cost Search 
	
	- A* Search w/heuristic 1
	
	- A* Search w/heuristic 2
	

Heuristic 1 : Number of misplaced tiles
Heuristic 2: City block distance of tiles to their original positions.

Example Input: 

> main = Main(8, "ucs") 8: depth of the solution, "ucs": strategy to use

Example Output:

> Max nodes in memory is : 1337

> Current cost is: 8 Solution is  [4, -3,-1, 5] 

> Used strategy:  a_star_2 

> Expanded 337  nodes 

> Number of nodes stored in memory 1337  nodes 

> Took 0.7859866619110107  seconds to run


How to run?

> python3 main.py

UML Diagram 

![UML](https://github.com/elifBalci/fifteen-puzzle-solver/blob/main/fifteen_puzzle.jpg)

