import numpy as np
from collections import deque
from queue import PriorityQueue

if __name__ == "__main__":
    gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = ReadFile ("maze.txt")
    gay_map = np.array(gay_map)
    if (len(bonusP)!=0):
        pass
    else if (len(forceP)!=0):
        pass
    else:
        dfs = DFS (gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y)
        bfs = BFS (gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y)
        ucs = UCS (gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y)
        bestfs = BestFS (gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y)
        astar = AStar (gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y)
        print (" ")
        print (dfs)
        print (" ")
        print (bfs)
        print (" ")
        print (ucs)
        print (" ")
        print (bestfs)
        print (" ")
        print (astar)

    
