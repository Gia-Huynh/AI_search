import numpy as np
from collections import deque
from queue import PriorityQueue
import MazeDefault
import MazeReward
import time

def Generate_Distance_Array (gay_map, forceP, start_x, start_y, exit_x, exit_y):
    SpecialP = forceP.copy()
    SpecialP.insert (0, [start_y, start_x, 0])
    SpecialP.append ([exit_y, exit_x, 0])
    trace =[]
    num = len(SpecialP)
    gae = np.zeros ((num, num), dtype = np.int16)
    for b in range (0, num-1):
        test = MazeDefault.BFS(gay_map, SpecialP[b][1], SpecialP[b][0], 0, 0)[0]
        for a in range (b+1, num):
            gae[b, a] = test [SpecialP[a][0]][SpecialP[a][1]] + SpecialP[a][2]
            gae[a, b] = gae[b, a] - SpecialP[a][2] + SpecialP[b][2]
    return gae, num, SpecialP

def VetCan (DisArr, num, SpecialP, maxTime = 1):
    begin_time = time.time()
    VisitIndex = np.arrange(1,num-1, step=1,dtype = np.int16)
    print (VisitIndex)
    cum = np.full_like (VisitIndex, 0,dtype = np.int16)
    
    
    

def MazeForceSearch (gay_map, bonusP, start_x, start_y, exit_x, exit_y):
    #Distance Array
    DisArr, num, SpecialP = Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y)
    return 0
    if (num<12):
        VetCan(DisArr, num, SpecialP)
    else:
        #Neu so luong node qua nhieu de DFS het sach, chuyen qua xai heuristic search
        pass







    #print (DisArr)
    Cost = np.full(num, np.amax(DisArr)+1)
    Cost[0] = 0;

    #BFS
    visited = np.zeros((num, num), dtype = np.int8)
    InQueue = np.zeros(num, dtype = np.int8)
    visited[:,0] = 1;
    queue = deque()
    queue.append (0)
    InQueue[0] = 1;
    trace = np.zeros(num, dtype = np.int8)
    while (queue):
        try:
            curr_node = queue.popleft()
        except Exception as e:
            break
            pass
        for i in range (0, num):
            if (visited[curr_node,i]==0):
                if (Cost[i] > Cost[curr_node]+DisArr[curr_node, i]):
                    Cost[i] = Cost[curr_node]+DisArr[curr_node, i]
                    visited[i,:] = visited[curr_node,:]
                    visited[i, curr_node] = 1
                    trace[i] = curr_node
                    
                    if (InQueue[i]==0):
                        queue.append(i)
                        InQueue[i] = 1
        InQueue[i] = 0
    #print (Cost)
    #print (trace)
    #END BFS
    BFS_Trace = []
    BFS_Trace_temp = []
    not_reached_end = True
    son = num-1
    while not_reached_end:
        father = trace[son]
        BFS_Trace_temp = []
        #[0] = y, [1] = x
        MazeDefault.BFS (gay_map, SpecialP[father][1], SpecialP[father][0], SpecialP[son][1], SpecialP[son][0], BFS_Trace_temp)
        #Vi ta dang di nguoc nen append vao dau list, cac nut father se o truoc cac nut con
        BFS_Trace = list(BFS_Trace_temp) + BFS_Trace
        son = father
        if (father == 0):
            not_reached_end = 0
    #BFS_Trace = list (BFS_Trace)
    BFS_Trace = [list(a) for a in BFS_Trace] #Chuyen ben trong tu tuple (y, x) qua list [y, x]
    BFS_Trace = [a[::-1] for a in BFS_Trace] #Dao nguoc x voi y
    #print (BFS_Trace)
    return Cost[num-1], trace

if __name__ == "__main__":
    pass
    
