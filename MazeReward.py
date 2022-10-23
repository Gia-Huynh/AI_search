import numpy as np
from collections import deque
from queue import PriorityQueue
import MazeDefault



def BFS_reward (gay_map, start_x, start_y, bonusP):
    N = len (gay_map)
    M = len (gay_map[0])
    visited = np.full_like(gay_map, 0)    
    result = np.full_like(gay_map, 0)
    steps = np.array([[1,0],[-1,0],[0,1],[0,-1]])
 
    queue = deque()
    queue.append ((start_x, start_y))
    x = 0
    y = 0

    #Tracing
    #gay_trace = np.zeros((N,M,2), dtype = np.int16)
    #path = []
    #trace = []
    while (queue):
        try:
            nigger = queue.popleft()
        except:
            return result
        for direction in steps:
            if (0<=(nigger + direction)[0] < M) and (0<=(nigger + direction)[1] < N):
                x, y = (nigger + direction)
                if (gay_map[y][x]==0):
                    continue
                if ((visited[y][x]==0) or (result[y][x] > result[nigger[1]][nigger[0]]+1)):
                    result[y][x] = result[nigger[1]][nigger[0]]+1
                        #[0] = x; [1] = y;
                    check = False
                    for a in bonusP:
                        if (a[0], a[1]) == (y, x):
                            check = True
                        
                    if (visited[y][x] != 2):
                        visited[y][x] = 2
                        if (check == False):
                            queue.append((x, y))
            else:
                continue
            visited[nigger[1]][nigger[0]] = 1 #da tham
        
    return result



def Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y):
    SpecialP = bonusP.copy()
    SpecialP.insert (0, [start_y, start_x, 0])
    SpecialP.append ([exit_y, exit_x, 0])
    trace =[]
    num = len(SpecialP)
    gae = np.zeros ((num, num), dtype = np.int16)
    for b in range (0, num-1):
        test = BFS_reward(gay_map, SpecialP[b][1], SpecialP[b][0], bonusP)
        #test = MazeDefault.BFS(gay_map, SpecialP[b][1], SpecialP[b][0], 0,0)[0]
        for a in range (b+1, num):
            gae[b, a] = test [SpecialP[a][0]][SpecialP[a][1]] + SpecialP[a][2]
            gae[a, b] = gae[b, a] - SpecialP[a][2] + SpecialP[b][2]           
    return gae, num, SpecialP

def MazeRewardSearch (gay_map, bonusP, start_x, start_y, exit_x, exit_y):
    #Distance Array
    DisArr, num, SpecialP = Generate_Distance_Array (gay_map, bonusP, start_x, start_y, exit_x, exit_y)
    #print (DisArr)
    Cost = np.full(num, np.amax(DisArr)+1)
    Cost[0] = 0

    #BFS
    visited = np.zeros((num, num), dtype = np.int16)
    InQueue = np.zeros(num, dtype = np.int16)
    visited[:,0] = 1
    queue = deque()
    queue.append (0)
    InQueue[0] = 1
    trace = np.zeros(num, dtype = np.int16)
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
        _, BFS_Trace_temp = MazeDefault.BFS (gay_map, SpecialP[father][1], SpecialP[father][0], SpecialP[son][1], SpecialP[son][0])
        #Vi ta dang di nguoc nen append vao dau list, cac nut father se o truoc cac nut con
        BFS_Trace = list(BFS_Trace_temp) + BFS_Trace
        son = father
        if (father == 0):
            not_reached_end = 0
    BFS_Trace = [list(a) for a in BFS_Trace] #Chuyen ben trong tu tuple (y, x) qua list [y, x]
    #BFS_Trace = [a[::-1] for a in BFS_Trace] #Dao nguoc x voi y
    return Cost[num-1], BFS_Trace

if __name__ == "__main__":
    pass
    
