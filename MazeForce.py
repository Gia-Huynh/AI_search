#sinh hoan vi, https://en.wikipedia.org/wiki/Heap%27s_algorithm
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
    TEST_SUM = 0
    #print (SpecialP)
    #print (VisitIndex)
    for j in range (0, len(VisitIndex)-1):
        #_,trace = MazeDefault.BFS(gay_map, SpecialP[i][1], SpecialP[i][0], SpecialP[i+1][1], SpecialP[i+1][0])
        i = VisitIndex[j]
        nig = VisitIndex[j+1]
        #print (SpecialP[i])
        TEST,trace = MazeDefault.UCS(gay_map, SpecialP[i][1], SpecialP[i][0], SpecialP[nig][1], SpecialP[nig][0])
        TEST_SUM+=TEST[SpecialP[nig][0]][SpecialP[nig][1]]
        result+=trace
    return result
    
def TinhToan (DisArr, num, VisitIndex):
    Total = 0
    for i in range (0, len(VisitIndex)-1):
        Total = Total + DisArr[VisitIndex[i], VisitIndex[i+1]]
    Total = Total + DisArr[0, VisitIndex[0]]
    Total = Total + DisArr[VisitIndex[len(VisitIndex)-1], num-1]
    return Total
def VetCan (DisArr, num, SpecialP, maxTime):
    begin_time = time.time()
    VisitIndex = np.arange(1,num-1, step=1,dtype = np.int16)
    BestVisitIndex = np.copy(VisitIndex)
    cum = np.full_like (VisitIndex, 0,dtype = np.int16)
    
    #0, 1,...n
    Min = TinhToan(DisArr, num, VisitIndex)
    #sinh hoan vi, https://en.wikipedia.org/wiki/Heap%27s_algorithm
    i=1
    n = len(VisitIndex)
    count = 0
    while (i<n):
        if (time.time() - begin_time > maxTime):
            print ("Vet Time exceeded")
            break
        if (cum[i] < i):
            if (i%2==0):
                VisitIndex[0], VisitIndex[i] = VisitIndex[i], VisitIndex[0]
            else:
                VisitIndex[cum[i]], VisitIndex[i] = VisitIndex[i], VisitIndex[cum[i]]
            #print (VisitIndex)
            count+=1
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
    return Min, BestVisitIndex

def StupidBFS (DisArr, num, SpecialP, maxTime):
    #nigger = DisArr.flatten()
    #sortedIndices = np.argsort(nigger)
    VisitIndex = [0]
    Visited = np.zeros (num)
    Visited[0] = 1
    #count = 1
    selected = 0
    asmgljaf=np.amax(DisArr)+1 #Very big number
    while (len(VisitIndex)!=num-1):
        MinCost = asmgljaf
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

def SmartBFS (DisArr, num, SpecialP, maxTime):

    def greedySearch (DisArr, List, startIdx):
        if (len(List)==1):
            return DisArr[startIdx, List[0]], List
        VisitIndex = [startIdx]
        Visited = np.zeros (len(List), dtype = np.int16)
        #if (startIdx ==0):
        #    Visited[startIdx] = 1
        Cost = 0
        selected = 0
        gayMax = np.amax(DisArr)+1
        while (len(VisitIndex)!=len(List)+1):
            MinCost = gayMax
            for j in range (0, len(List)):
                i = List[j]

                if (Visited[j] == 0) and (DisArr[VisitIndex[len(VisitIndex)-1], i] < MinCost):
                    MinCost = DisArr[VisitIndex[len(VisitIndex)-1], i]
                    selected = j
            #print (selected)
            
            VisitIndex.append(List[selected])
            Cost+=MinCost
            Visited[selected] = 1
        #print (VisitIndex)
        return Cost, VisitIndex[1:]
        
    def TinhToanTwo (DisArr, groupList, permutation):
        #start at 0, end at N-1
        #groupList.back() se chua List co output Node trong do, o function ben ngoai phai swap(groupList[exit_idx], groupList[end] )
        FinalPath = [0]
        FinalCost = 0
        Exit_Node = 0
        
        for i in range (0, len(permutation)):
            currGroup = groupList[permutation[i]]
            Cost, Path = greedySearch(DisArr, currGroup, Exit_Node)
            FinalCost+= Cost
            FinalPath+= Path
            Exit_Node = FinalPath[-1]
        #Final, exit node
        
        FinalCost+= DisArr[Exit_Node, groupList[len(groupList)-1]]
        FinalPath+= groupList[len(groupList)-1]
        return FinalCost, FinalPath



    row = len(DisArr)   #row = column, ma tran khoang cach la ma tran vuong
    nigger = DisArr.flatten()
    positionArr = np.zeros((nigger.shape[0], 2), dtype=np.int16)
    count = 0
    for a in range (0, row):
        for b in range (0, row):
            positionArr[count][0] = a
            positionArr[count][1] = b
            count+=1
    sortedIndices = np.argsort(nigger)    
    father = np.arange (0, num)
    DistinctGroups = num    
    for a in sortedIndices:
        #khong sinh hoan vi group bat dau va group ket thuc, do vi tri la co dinh, max sinh duoc hoan vi cua 8 group
        if (DistinctGroups <= 9):
            break
        if (nigger[a] == 0):
            continue
        if ((father[positionArr[a][0]]==father[positionArr[a][1]])
            or (father[positionArr[a][0]]==len(DisArr)-1) or (father[positionArr[a][1]]==len(DisArr)-1)
            or(father[positionArr[a][0]]==0) or (father[positionArr[a][1]]==0)):
            continue
        pointOne = positionArr[a][0]
        pointTwo = positionArr[a][1]
        minFather = min (father[pointOne], father[pointTwo])
        maxFather = max (father[pointOne], father[pointTwo])
        father[father == maxFather] = minFather
        DistinctGroups-=1
    groupList = []
    for a in range (0, len(father)):
        if (father[a]==a):
            groupList.append([a])
        else:
            for i in groupList:
                if i[0] == father[a]:
                    i.append(a)
    
    VisitIndex = np.arange(1, len(groupList)-1, step=1,dtype = np.int16)
    BestVisitIndex = np.copy(VisitIndex)
    
    #sinh hoan vi, https://en.wikipedia.org/wiki/Heap%27s_algorithm
    cum = np.zeros (DistinctGroups-2,dtype = np.int16)
    n = DistinctGroups-2
    i=1
    Min, FinalPath = TinhToanTwo (DisArr, groupList, VisitIndex)
    while (i<n):
        if (cum[i] < i):
            if (i%2==0):
                VisitIndex[0], VisitIndex[i] = VisitIndex[i], VisitIndex[0]
            else:
                VisitIndex[cum[i]], VisitIndex[i] = VisitIndex[i], VisitIndex[cum[i]]

            Cost, Path =  TinhToanTwo (DisArr, groupList, VisitIndex)
            if (Min > Cost):
                Min = Cost
                FinalPath = Path
            cum[i]+=1
            i=1
        else:
            cum[i] = 0
            i += 1
    return Min[0], FinalPath
        


def MazeForceSearchVetCan (gay_map, bonusP, start_x, start_y, exit_x, exit_y, maxTime = 7.5):
    #Distance Array
    DisArr, num, SpecialP = Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y)
    MinTime = 0
    BestVisitIndex = []
    #Neu so luong node qua nhieu de DFS het sach, chuyen qua xai heuristic search
    if (len(bonusP)<9):
        MinTime, BestVisitIndex = VetCan(DisArr, num, SpecialP, maxTime = maxTime)
        BestVisitIndex=np.insert(BestVisitIndex,0,0)
        BestVisitIndex=np.append(BestVisitIndex,len(SpecialP)-1)
    return MinTime, Generate_Array_From_Trace (gay_map, SpecialP, BestVisitIndex)

            
def MazeForceSearchHeuristic (gay_map, bonusP, start_x, start_y, exit_x, exit_y, maxTime = 7.5):
    #Distance Array
    DisArr, num, SpecialP = Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y)
    MinTime = 10
    BestVisitIndex = []
    MinTime, BestVisitIndex = StupidBFS(DisArr, num, SpecialP, maxTime = maxTime)
    #print (BestVisitIndex)
    return MinTime, Generate_Array_From_Trace (gay_map, SpecialP, BestVisitIndex)

def MazeForceSearchSmart (gay_map, bonusP, start_x, start_y, exit_x, exit_y, maxTime = 7.5):
    #Distance Array
    DisArr, num, SpecialP = Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y)
    MinTime = 0
    BestVisitIndex = []
    #Neu so luong node qua nhieu de DFS het sach, chuyen qua xai heuristic search
    MinTime, BestVisitIndex = SmartBFS(DisArr, num, SpecialP, maxTime = maxTime)
    return MinTime, Generate_Array_From_Trace (gay_map, SpecialP, BestVisitIndex)

if __name__ == "__main__":
    print ("Chay nham file roi")
    pass
    
