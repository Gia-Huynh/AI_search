import numpy as np
from collections import deque
from queue import PriorityQueue
import MazeDefault
import SupportFunction
gay_dict = {'x': 0, ' ': 1, 'S': 2, 's': 2, '+': 3}
def ReadFile (filename):
    #0.........x
    #.
    #.
    #y
    with (open(filename, "r")) as f:
        bonusP = []
        forceP = []
        gay_map = []
        exit_x = -1
        exit_y = -1
        start_x = 0
        start_y = 0
        gay = f.readline()
        n = int (gay)
        
        for i in range (0, n):
            gay = f.readline().split()
            if (gay[2] == "0"):
                forceP.append (gay[0:1])
            else:
                bonusP.append (gay[0:2])
        gay = f.readline().rstrip('\r\n')
        while(gay != ''):
            map_line = [gay_dict[t] for t in gay]
            gay_map.append (map_line)
            gay = f.readline().rstrip('\r\n')
            try:
                start_x = map_line.index(2)
                start_y = len(gay_map)-1
            except:
                pass
        try:
            exit_x = gay_map[len(gay_map)-1].index(1)
            exit_y = len(gay_map)-1
        except:
            try:
                exit_x = gay_map[0].index(1)
                exit_y = 0
            except:
                try:
                    inverse_gay_map = list(zip (*gay_map))
                    exit_y = inverse_gay_map[0].index(1)
                    exit_x = 0
                except:
                    try:
                        exit_y = inverse_gay_map[len(inverse_gay_map)-1].index(1)
                        exit_x = len(inverse_gay_map)-1
                    except:
                        print ("Can not find exit location")
                        pass

        return gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y

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

    
