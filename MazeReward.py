import numpy as np
from collections import deque
from queue import PriorityQueue
import MazeDefault

def Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y):
    SpecialP = bonusP.copy()
    SpecialP.insert (0, [start_y, start_x, 0])
    SpecialP.append ([exit_y, exit_x, 0])
    print (SpecialP)
    #[Start, specialP, specialP, specialP, Exit]
    num = len(SpecialP)
    gae = np.zeros ((num, num), dtype = np.int8)
    print (gae.shape)
    print (np.array(SpecialP).shape)
    #B tham A
    for b in range (0, num-1):
        gae[b, b] = 1
        for a in range (b+1, num):
            print (b," ",a)
            gae[b, a] = SpecialP[a][2] + MazeDefault.BFS(gay_map, SpecialP[b][1], SpecialP[b][0], SpecialP[a][1], SpecialP[a][0])[SpecialP[a][1]][SpecialP[a][0]]
            gae[a, b] = gae[b, a] - SpecialP[a][2] + SpecialP[b][2] 
    return gae
def MazeRewardSearch (gay_map, bonusP, start_x, start_y, exit_x, exit_y):
    DistanceArr = Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y)
    print (DistanceArr)
    return result


if __name__ == "__main__":
    pass
    
