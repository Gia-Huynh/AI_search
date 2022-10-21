import numpy as np
from collections import deque
from queue import PriorityQueue
import MazeDefault

def Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y):
    SpecialP = bonusP.copy()
    SpecialP.insert (0, [start_x, start_y, 0])
    SpecialP.append ([exit_x, exit_y, 0])
    #[Start, specialP, specialP, specialP, Exit]
    num = len(SpecialP)
    gae = np.zeros (num, dtype = np.int8)
    """gae[0,0] = 1
    for a in range (0, num):
        gae[0,a+1] = bonusP[a][2] + MazeDefault.BFS(gay_map, start_x, start_y, bonusP[a][0], bonusP[a][1])
    gae[0,num+1] = MazeDefault.BFS(gay_map, start_x, start_y, exit_x, exit_y)"""

    for b in range (0, num-1):
        gae[b, b] = 1
        for a in range (b+1, num):
            gae[b, a] = bonusP[a][2] + MazeDefault.BFS(gay_map, bonusP[b][0], bonusP[b][1], bonusP[a][0], bonusP[a][1])
            gae[a, b] = gae[b, a]
    return gae
def MazeRewardSearch (gay_map, bonusP, start_x, start_y, exit_x, exit_y):
    DistanceArr = Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y)
    print (DistanceArr)
    return result


if __name__ == "__main__":
    pass
    
