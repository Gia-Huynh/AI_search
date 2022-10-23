import numpy as np
from collections import deque
from queue import PriorityQueue
import MazeDefault
import MazeReward
import MazeForce
import SupportFunction
#gay_dict = {'x': 0, ' ': 1, 'S': 2, 's': 2, '+': 3}
FileName = "mazeForceMAXPOINT.txt"
if __name__ == "__main__":
    gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = SupportFunction.ReadFile (FileName)
    route = []
    
    bonusP = []
    #forceP = []
    
    gay_map = np.array(gay_map)

    if (len(forceP)!=0):
        cost, trace = MazeForce.MazeForceSearch(gay_map, forceP, start_x, start_y, exit_x, exit_y, maxTime = 7.5)
        print (cost)
        print (trace)

    elif (len(bonusP)!=0):
        cost, trace = MazeReward.MazeRewardSearch(gay_map, bonusP, start_x, start_y, exit_x, exit_y)
        print (cost)
        print (trace)
    else:
        dfs, routeDFS = MazeDefault.DFS (gay_map, start_x, start_y, exit_x, exit_y)
        bfs, routeBFS = MazeDefault.BFS (gay_map, start_x, start_y, exit_x, exit_y)
        ucs, routeUCS = MazeDefault.UCS (gay_map, start_x, start_y, exit_x, exit_y)
        bestfs, routeBESTFS = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 1)
        astar, routeASTAR = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 0)
        print ("dfs")
        print (dfs)
        print (routeDFS)
        print ("bfs")
        print (bfs)
        print (routeBFS)
        print ("ucs")
        print (ucs)
        print (routeUCS)
        print ("bestfs")
        print (bestfs)
        print (routeBESTFS)
        print ("astar")
        print (astar)
        print (routeASTAR)

    
