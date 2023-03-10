import numpy as np
from collections import deque
from queue import PriorityQueue
gay_dict = {'x': 0, ' ': 1, 'S': 2, 's': 2, '+': 3}
def DFS_rec (gay_map , curr_x, curr_y, result):
    route = []
    N = len (gay_map)
    M = len (gay_map[0])
    #print (curr_x,"  ", M)
    #print (curr_y,"  ", N)
    steps = np.array([[1,0],[-1,0],[0,1],[0,-1]])
    x = 0
    y = 0
    #if (curr_x == 0) or (curr_x == M) or (curr_y == 0) or (curr_y == N):
    if (curr_x == 0) or (curr_x == M-1) or (curr_y == 0) or (curr_y == N-1):
        #print ("FOUND")
        return 1, []
    #print (result)
    for direction in steps:
        if (0<=curr_x + direction[0] < M) and (0<=curr_y+direction[1] < N):
            x = curr_x + direction[0]
            y = curr_y + direction[1]
            
            if ((gay_map[y][x]==0) or (result[y][x]<=result[curr_y][curr_x]+1)):
                continue
            
            if (y,x) not in route:
                route.append((y,x))
                
            result[y][x] = result[curr_y][curr_x] + 1
            #print (result)
            dfs_result, dfs_trace = DFS_rec(gay_map , x, y, result)
            
            if (dfs_result==1):
                #print (route)
                route+=list(dfs_trace)
                return 1, route
            
            elif(dfs_result==-1):
                route.pop()
            #result[y][x] = N * M + 1
    #print (route)
    return -1, []
def DFS (gay_map , start_x, start_y, exit_x, exit_y):
    route = []
    route.append((start_y,start_x))
    result = np.full_like(gay_map, len (gay_map)*len (gay_map[0])+1)
    #result = np.full(gay_map.shape, np.amax(gay_map)+1)
    result[start_y][start_x] = 1
    #print ("DFS-ing")
    dfs_output, route = DFS_rec (gay_map , start_x, start_y, result)
    #print ("Done DFS-ing")
    result[result == len (gay_map)*len (gay_map[0])+1] = 0
    route = [(YE[1], YE[0]) for YE in route]
    if (exit_x>=0) and(exit_y>=0):
        route.insert(0,(exit_x, exit_y))
    return result, route

def BFS (gay_map , start_x, start_y, exit_x, exit_y):
    N = len (gay_map)
    M = len (gay_map[0])

    visited = np.full_like(gay_map, 0)
    # 0: Not visited yet
    # 1: Visited
    # 2: Visiting (in queue)
    
    result = np.full_like(gay_map, 0)
    # Cost of traversal to location [y][x]
    
    steps = np.array([[1,0],[-1,0],[0,1],[0,-1]])
    
    queue = deque()
    queue.append ((start_x, start_y))
    x = 0
    y = 0

    #Tracing
    gay_trace = np.zeros((N,M,2), dtype = np.int16)
    path = []
    trace = []
    while (queue):
        try:
            nigger = queue.popleft()
            #[0] = x; [1] = y;
        except:
            return result, trace
        #curr xai de visualize cac diem BFS di qua, khong phai de output ra path tu entry -> exit
        curr = []
        for direction in steps:
            if (0<=(nigger + direction)[0] < M) and (0<=(nigger + direction)[1] < N):
                x, y = (nigger + direction)
                if (gay_map[y][x]==0):
                    continue
                if (visited[y][x]==0):
                    curr.append((y,x))
                    result[y][x] = result[nigger[1]][nigger[0]]+1

                    #Check if y, x is exit
                    if (x, y) == (exit_x, exit_y):
                        path.append(curr)
                        gay_trace[y][x][0] = nigger[0]
                        gay_trace[y][x][1] = nigger[1]
                        
                        x = exit_x
                        y = exit_y
                        temp = 0
                        while not((x==0) and (y==0)):
                            trace.append((x, y))
                            temp = gay_trace[y][x][0]
                            y = gay_trace[y][x][1]
                            x = temp
                        trace.reverse()                
                        return result, trace
                    
                    if (visited[y][x]!=2):
                        gay_trace[y][x][0] = nigger[0]
                        gay_trace[y][x][1] = nigger[1]
                        #[0] = x; [1] = y;
                        visited[y][x] = 2
                        queue.append((x, y))
            else:
                continue
            visited[nigger[1]][nigger[0]] = 1
        path.append(curr)
    #Cannot Find Exit_x, exit_y, rip bozo
    return result, trace

def UCS (gay_map , start_x, start_y, exit_x, exit_y):
    N = len (gay_map)
    M = len (gay_map[0])
    visited = np.full_like(gay_map, 0)
    # 0: Not visited yet
    # 1: Visited
    # 2: Visiting (in queue)
    result = np.full_like(gay_map, 0)
    # Cost of traversal to location [y][x]
    steps = np.array([[1,0],[-1,0],[0,1],[0,-1]])
    queue = PriorityQueue()
    queue.put ((0,(start_x, start_y)))
    x = 0
    y = 0

    #Tracing
    gay_trace = np.zeros((N,M,2), dtype = np.int16)
    path = []
    trace = []
    
    while (True):
        try:
            nigger = queue.get(block = False)[1]
            if (nigger[0], nigger[1]) == (exit_x, exit_y):
                return result, trace
            #[0] = x; [1] = y;
        except:
            return result, trace
        #curr xai de visualize cac diem BFS di qua, khong phai de output ra path tu entry -> exit
        curr = []
        for direction in steps:
            if (0<=(nigger + direction)[0] < M) and (0<=(nigger + direction)[1] < N):
                x, y = (nigger + direction)
                if (gay_map[y][x]==0):
                    continue
                if (visited[y][x]==0):
                    curr.append((y,x))
                    result[y][x] = result[nigger[1]][nigger[0]] + 1
                    
                    #Check if y, x is exit
                    if (x, y) == (exit_x, exit_y):
                        path.append(curr)
                        gay_trace[y][x][0] = nigger[0]
                        gay_trace[y][x][1] = nigger[1]
                        x = exit_x
                        y = exit_y
                        temp = 0
                        while not((x==0) and (y==0)):
                            trace.append((x, y))
                            temp = gay_trace[y][x][0]
                            y = gay_trace[y][x][1]
                            x = temp
                        trace.reverse()                
                        return result, trace
                    
                    gay_trace[y][x][0] = nigger[0]
                    gay_trace[y][x][1] = nigger[1]
                    visited[y][x] = 2
                    queue.put((result[y][x], (x, y)))
            else:
                continue
            visited[nigger[1]][nigger[0]] = 1
    return result, trace
def HeuristicFunction (curr_x, curr_y, exit_x, exit_y):
    return ((exit_x-curr_x)**2 + (exit_y-curr_y)**2)
def HeuristicFunctionAstar (curr_x, curr_y, exit_x, exit_y):
    return (abs(exit_x-curr_x)+abs(exit_y-curr_y))
def InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 1, choice = 0):
    N = len (gay_map)
    M = len (gay_map[0])
    visited = np.full_like(gay_map, 0)
    result = np.full_like(gay_map, 0)
    steps = np.array([[1,0],[-1,0],[0,1],[0,-1]])
    queue = PriorityQueue()
    queue.put ((0,(start_x, start_y)))
    x = 0
    y = 0
    
    #Tracing
    gay_trace = np.zeros((N,M,2), dtype = np.int16)
    path = []
    trace = []
    
    while (True):
        try:
            nigger = queue.get(block = False)[1]
            if (nigger[0], nigger[1]) == (exit_x, exit_y):
                return result, trace
            #[0] = x; [1] = y;
        except:
            return result, trace

        #curr xai de visualize cac diem BFS di qua, khong phai de output ra path tu entry -> exit
        curr = []
        
        for direction in steps:
            if (0<=(nigger + direction)[0] < M) and (0<=(nigger + direction)[1] < N):
                x, y = (nigger + direction)
                if (gay_map[y][x]==0):
                    continue
                if (visited[y][x]==0):
                    curr.append((y,x))
                    result[y][x] = result[nigger[1]][nigger[0]] + 1
                    
                    #Check if y, x is exit
                    if (x, y) == (exit_x, exit_y):
                        path.append(curr)
                        gay_trace[y][x][0] = nigger[0]
                        gay_trace[y][x][1] = nigger[1]
                        x = exit_x
                        y = exit_y
                        temp = 0
                        while not((x==0) and (y==0)):
                            trace.append((x, y))
                            temp = gay_trace[y][x][0]
                            y = gay_trace[y][x][1]
                            x = temp
                        trace.reverse()                
                        return result, trace
                    
                    visited[y][x] = 1
                    gay_trace[y][x][0] = nigger[0]
                    gay_trace[y][x][1] = nigger[1]
                    #BEST FIRST SEARCH
                    if (bestFirst == 1):
                        if (choice == 0):
                            queue.put((HeuristicFunction(x, y, exit_x, exit_y), (x, y)))
                        else:
                            queue.put((HeuristicFunctionAstar(x, y, exit_x, exit_y), (x, y)))
                    #A STAR
                    #
                    if (bestFirst == 0):
                        if (choice == 0):
                            queue.put((result[y][x] + HeuristicFunctionAstar(x, y, exit_x, exit_y), (x, y)))
                        else:
                            queue.put((result[y][x] + HeuristicFunction(x, y, exit_x, exit_y), (x, y)))
            else:
                continue
            visited[nigger[1]][nigger[0]] = 1
    return result, trace

if __name__ == "__main__":
    print ("CHAY NHAM FILE ROI")

    
