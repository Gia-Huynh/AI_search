import numpy as np
from collections import deque
from queue import PriorityQueue
import MazeDefault
import SupportFunction
#gay_dict = {'x': 0, ' ': 1, 'S': 2, 's': 2, '+': 3}

if __name__ == "__main__":
    gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = SupportFunction.ReadFile ("maze.txt")
    gay_map = np.array(gay_map)
    if (len(bonusP)!=0):
        pass
    else if (len(forceP)!=0):
        pass
    else:
        dfs = MazeDefault.DFS (gay_map, start_x, start_y, exit_x, exit_y)
        bfs = MazeDefault.BFS (gay_map, start_x, start_y, exit_x, exit_y)
        ucs = MazeDefault.UCS (gay_map, start_x, start_y, exit_x, exit_y)
        bestfs = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 1)
        astar = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 0)
        print ("dfs")
        print (dfs)
        print ("bfs")
        print (bfs)
        print ("ucs")
        print (ucs)
        print ("bestfs")
        print (bestfs)
        print ("astar")
        print (astar)

    
