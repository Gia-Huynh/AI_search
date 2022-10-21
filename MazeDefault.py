import numpy as np
from collections import deque
from queue import PriorityQueue
gay_dict = {'x': 0, ' ': 1, 'S': 2, 's': 2, '+': 3}
def DFS_rec (gay_map , curr_x, curr_y, result,route):
    N = len (gay_map)
    M = len (gay_map[0])
    steps = np.array([[1,0],[-1,0],[0,1],[0,-1]])
    x = 0
    y = 0
    if (curr_x == 0) or (curr_x == M) or (curr_y == 0) or (curr_y == N):
        return 1
    #print (result)
    for direction in steps:
        if (0<=curr_x + direction[0] < M) and (0<=curr_y+direction[1] < N):
            x = curr_x + direction[0]
            y = curr_y + direction[1]
            if ((gay_map[y][x]==0) or (result[y][x]<=result[curr_y][curr_x])):
                continue
            #or (result[y][x] > result[nigger[1]][nigger[0]]+gay_map[y][x]):
            if (y,x) not in route:
                route.append((y,x))
            result[y][x] = result[curr_y][curr_x] + gay_map[y][x]
            if (DFS_rec(gay_map , x, y, result, route)==1):
                return 1
            elif(DFS_rec(gay_map, x, y, result, route)==-1):
                route.pop()
            result[y][x] = N * M + 1
    return -1
def DFS (gay_map , start_x, start_y, exit_x, exit_y,route):
    route.append((start_y,start_x))
    result = np.full_like(gay_map, len (gay_map)*len (gay_map[0])+1)
    result[start_y][start_x] = 1
    dfs_output = DFS_rec (gay_map , start_x, start_y, result,route)
    #print (dfs_output)
    result[result == len (gay_map)*len (gay_map[0])+1] = 0
    return result

def BFS (gay_map , start_x, start_y, exit_x, exit_y, trace):
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

    trace = []
    while (queue):
        try:
            nigger = queue.popleft()
            #[0] = x; [1] = y;
        except:
            return result
        curr = []
        for direction in steps:
            if (0<=(nigger + direction)[0] < M) and (0<=(nigger + direction)[1] < N):
                x, y = (nigger + direction)
                if (gay_map[y][x]==0):
                    continue
                if (visited[y][x]==0):
                #or (result[y][x] > result[nigger[1]][nigger[0]]+gay_map[y][x]):
                    curr.append((y,x))
                    result[y][x] = result[nigger[1]][nigger[0]]+gay_map[y][x]
                    if (visited[y][x]!=2):
                        visited[y][x] = 2
                        queue.append((x, y))
            else:
                continue
            visited[nigger[1]][nigger[0]] = 1
        trace.append(curr)
    print (trace)
    return result

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
    while (True):
        try:
            nigger = queue.get(block = False)[1]
            #[0] = x; [1] = y;
        except:
            return result
        for direction in steps:
            if (0<=(nigger + direction)[0] < M) and (0<=(nigger + direction)[1] < N):
                x, y = (nigger + direction)
                if (gay_map[y][x]==0):
                    continue
                if (visited[y][x]==0):
                #or (result[y][x] > result[nigger[1]][nigger[0]]+gay_map[y][x]):
                    result[y][x] = result[nigger[1]][nigger[0]]+gay_map[y][x]
                    if (visited[y][x]!=2):
                        visited[y][x] = 2
                        queue.put((result[y][x], (x, y)))
            else:
                continue
            visited[nigger[1]][nigger[0]] = 1
    return result
def HeuristicFunction (curr_x, curr_y, exit_x, exit_y):
    return ((exit_x-curr_x)**2 + (exit_y-curr_y)**2)
def HeuristicFunctionAstar (curr_x, curr_y, exit_x, exit_y):
    return (abs(exit_x-curr_x)+abs(exit_y-curr_y))
def InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 1):
    N = len (gay_map)
    M = len (gay_map[0])
    visited = np.full_like(gay_map, 0)
    result = np.full_like(gay_map, 0)
    steps = np.array([[1,0],[-1,0],[0,1],[0,-1]])
    queue = PriorityQueue()
    queue.put ((0,(start_x, start_y)))
    x = 0
    y = 0
    while (True):
        try:
            nigger = queue.get(block = False)[1]
            if (nigger[0], nigger[1]) == (exit_x, exit_y):
                return result
            #[0] = x; [1] = y;
        except:
            return result
        for direction in steps:
            if (0<=(nigger + direction)[0] < M) and (0<=(nigger + direction)[1] < N):
                x, y = (nigger + direction)
                if (gay_map[y][x]==0):
                    continue
                if (visited[y][x]==0):
                #or (result[y][x] > result[nigger[1]][nigger[0]]+gay_map[y][x]):
                    result[y][x] = result[nigger[1]][nigger[0]]+gay_map[y][x]
                    if (visited[y][x]!=2):
                        visited[y][x] = 2
                        #BEST FIRST SEARCH
                        if (bestFirst == 1):
                            queue.put((HeuristicFunction(x, y, exit_x, exit_y), (x, y)))
                        #A STAR
                        #
                        if (bestFirst == 0):
                            queue.put((result[y][x] + HeuristicFunctionAstar(x, y, exit_x, exit_y), (x, y)))
            else:
                continue
            visited[nigger[1]][nigger[0]] = 1
    return result

if __name__ == "__main__":
    print ("CHAY NHAM FILE ROI")

    
