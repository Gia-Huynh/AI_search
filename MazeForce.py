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
        #Tim khoang cach nho nhat toi TAT CA cac diem con lai, vi target la (0, 0), target khong ton tai
        test = MazeDefault.BFS(gay_map, SpecialP[b][1], SpecialP[b][0], 0, 0)[0] 
        for a in range (b+1, num):
            gae[b, a] = test [SpecialP[a][0]][SpecialP[a][1]]
            gae[a, b] = gae[b, a]
    return gae, num, SpecialP

def Generate_Array_From_Trace (gay_map, SpecialP, VisitIndex):
    result = []
    #TEST_SUM = 0
    for i in range (0, len(VisitIndex)-1):
        _,trace = MazeDefault.UCS(gay_map, SpecialP[i][1], SpecialP[i][0], SpecialP[i+1][1], SpecialP[i+1][0])
        #TEST,trace = MazeDefault.UCS(gay_map, SpecialP[i][1], SpecialP[i][0], SpecialP[i+1][1], SpecialP[i+1][0])
        #TEST_SUM+=TEST[SpecialP[i+1][0]][SpecialP[i+1][1]]
        result+=trace
    #print (TEST_SUM)
    return result
    
def TinhToan (DisArr, num, VisitIndex):
    Total = 0
    for i in range (0, len(VisitIndex)-1):
        Total = Total + DisArr[VisitIndex[i], VisitIndex[i+1]]
    Total = Total + DisArr[0, VisitIndex[0]]
    Total = Total + DisArr[VisitIndex[0], num-1]
    return Total
def VetCan (DisArr, num, SpecialP, maxTime):
    begin_time = time.time()
    VisitIndex = np.arange(1,num-1, step=1,dtype = np.int16)
    BestVisitIndex = np.copy(VisitIndex)
    cum = np.full_like (VisitIndex, 0,dtype = np.int16)
    
    #0, 1,...n
    Min = TinhToan(DisArr, num, VisitIndex)
    #print (Min)
    #print (VisitIndex)

    #sinh hoan vi, https://en.wikipedia.org/wiki/Heap%27s_algorithm
    i=1
    n = len(VisitIndex)
    while (i<n):
        if (time.time() - begin_time > maxTime):
            break
        if (cum[i] < i):
            if (i%2==0):
                VisitIndex[0], VisitIndex[i] = VisitIndex[i], VisitIndex[0]
            else:
                VisitIndex[cum[i]], VisitIndex[i] = VisitIndex[i], VisitIndex[cum[i]]
            if (Min > TinhToan(DisArr, num, VisitIndex)):
                #print (TinhToan(DisArr, num, VisitIndex))
                #print (VisitIndex)
                Min = TinhToan(DisArr, num, VisitIndex)
                BestVisitIndex = np.copy(VisitIndex)
            cum[i]+=1
            i=1
        else:
            cum[i] = 0
            i += 1
    #print (time.time() - begin_time)
    return Min, BestVisitIndex

def StupidBFS (DisArr, num, SpecialP, maxTime):
    #nigger = DisArr.flatten()
    #sortedIndices = np.argsort(nigger)
    VisitIndex = [0]
    Visited = np.zeros (num)
    Visited[0] = 1
    #count = 1
    selected = 0
    while (len(VisitIndex)!=num-1):
        MinCost = np.argmax(DisArr)
        for i in range (0, num-1):
            if (Visited[i] == 0) and (DisArr[VisitIndex[len(VisitIndex)-1], i] < MinCost):
                MinCost = DisArr[VisitIndex[len(VisitIndex)-1], i]
                selected = i
        VisitIndex.append(selected)
        Visited[selected] = 1
    VisitIndex.append(num-1)
    #DONE
    #print (VisitIndex)
    #print (TinhToan (DisArr, num, VisitIndex))
    return TinhToan (DisArr, num, VisitIndex), VisitIndex
            
def MazeForceSearch (gay_map, bonusP, start_x, start_y, exit_x, exit_y, maxTime = 7.5):
    #Distance Array
    DisArr, num, SpecialP = Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y)
    MinTime = 10
    BestVisitIndex = []

    #Neu so luong node qua nhieu de DFS het sach, chuyen qua xai heuristic search
    if (len(bonusP)<10):
        MinTime, BestVisitIndex = VetCan(DisArr, num, SpecialP, maxTime = maxTime)
    else:
        MinTime, BestVisitIndex = StupidBFS(DisArr, num, SpecialP, maxTime = maxTime)
    #print (BestVisitIndex)
    return MinTime, Generate_Array_From_Trace (gay_map, SpecialP, BestVisitIndex)

if __name__ == "__main__":
    print ("Chay nham file roi")
    pass
    
