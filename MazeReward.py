import numpy as np
from collections import deque
from queue import PriorityQueue
import MazeDefault

def Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y):
    SpecialP = bonusP.copy()
    SpecialP.insert (0, [start_y, start_x, 0])
    SpecialP.append ([exit_y, exit_x, 0])
    trace =[]
    print (SpecialP)
    #[Start, specialP, specialP, specialP, Exit]
    num = len(SpecialP)
    gae = np.zeros ((num, num), dtype = np.int8)
    #B tham A
    for b in range (0, num-1):
        #gae[b, b] = 99
        for a in range (b+1, num):
            gae[b, a] = SpecialP[a][2] + MazeDefault.BFS(gay_map, SpecialP[b][1], SpecialP[b][0], SpecialP[a][1], SpecialP[a][0], trace)[SpecialP[a][0]][SpecialP[a][1]]
            gae[a, b] = gae[b, a] - SpecialP[a][2] + SpecialP[b][2]
            #print (SpecialP[b]," ",SpecialP[a]," ",SpecialP[a][2]," ",gae[b, a] - SpecialP[a][2])
            pass
            
        #print(MazeDefault.BFS(gay_map, SpecialP[b][1], SpecialP[b][0], SpecialP[2][1], SpecialP[2][0], trace))
    #gae[num-1, num-1] = 99
    return gae
def MazeRewardSearch (gay_map, bonusP, start_x, start_y, exit_x, exit_y):
    DistanceArr = Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y)
    print (DistanceArr)
    return DistanceArr


if __name__ == "__main__":
    pass
    
