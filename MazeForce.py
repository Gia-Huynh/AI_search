import numpy as np
from collections import deque
from queue import PriorityQueue
import MazeDefault
import MazeReward
import time

def Generate_Distance_Array (gay_map, forceP, start_x, start_y, exit_x, exit_y):
    SpecialP = forceP.copy()
    SpecialP.insert (0, [start_y, start_x])
    SpecialP.append ([exit_y, exit_x])
    num = len(SpecialP)
    
    trace =[]
    gae = np.zeros ((num, num), dtype = np.int16)
    
    for b in range (0, num-1):
        test = MazeDefault.BFS(gay_map, SpecialP[b][1], SpecialP[b][0], 0, 0)[0]
        for a in range (b+1, num):
            gae[b, a] = test [SpecialP[a][0]][SpecialP[a][1]]
            gae[a, b] = gae[b, a]
    return gae, num, SpecialP

def TinhToan (DisArr, num, VisitIndex):
    Total = 0
    for i in range (0, len(VisitIndex)-1):
        Total = Total + DisArr[VisitIndex[i], VisitIndex[i+1]]
    Total = Total + DisArr[0, VisitIndex[0]]
    Total = Total + DisArr[VisitIndex[0], num-1]
    
    return Total
def VetCan (DisArr, num, SpecialP, maxTime = 1):
    begin_time = time.time()
    VisitIndex = np.arange(1,num-1, step=1,dtype = np.int16)
    BestVisitIndex = np.copy(VisitIndex)
    cum = np.full_like (VisitIndex, 0,dtype = np.int16)
    
    #0, 1,...n
    Min = TinhToan(DisArr, num, VisitIndex)
    print (Min)
    print (VisitIndex)

    #sinh hoan vi, https://en.wikipedia.org/wiki/Heap%27s_algorithm
    i=1
    n = len(VisitIndex)
    while (i<n):
        if (cum[i] < i):
            if (i%2==0):
                VisitIndex[0], VisitIndex[i] = VisitIndex[i], VisitIndex[0]
            else:
                VisitIndex[cum[i]], VisitIndex[i] = VisitIndex[i], VisitIndex[cum[i]]
            if (Min > TinhToan(DisArr, num, VisitIndex)):
                print (TinhToan(DisArr, num, VisitIndex))
                print (VisitIndex)
                BestVisitIndex = np.copy(VisitIndex)
            cum[i]+=1
            i=1
        else:
            cum[i] = 0
            i += 1
    return Min, BestVisitIndex

def MazeForceSearch (gay_map, bonusP, start_x, start_y, exit_x, exit_y):
    #Distance Array
    DisArr, num, SpecialP = Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y)
    if (num<12):
        VetCan(DisArr, num, SpecialP)
    else:
        #Neu so luong node qua nhieu de DFS het sach, chuyen qua xai heuristic search
        pass
    return 0, 0

if __name__ == "__main__":
    pass
    
