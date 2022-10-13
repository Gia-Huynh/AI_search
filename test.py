import numpy as np
from collections import deque
gay_dict = {'x': 0, ' ': 1, 'S': 2, 's': 2, '+': 3}
def ReadFile (filename):
    #0.........x
    #.
    #.
    #y
    with (open(filename, "r")) as f:
        bonusP = []
        forceP = []
        gay_map = []
        exit_x = -1
        exit_y = -1
        start_x = 0
        start_y = 0
        gay = f.readline()
        n = int (gay)
        
        for i in range (0, n):
            gay = f.readline().split()
            if (gay[2] == "0"):
                forceP.append (gay[0:1])
            else:
                bonusP.append (gay[0:2])
        gay = f.readline().rstrip('\r\n')
        while(gay != ''):
            map_line = [gay_dict[t] for t in gay]
            gay_map.append (map_line)
            gay = f.readline().rstrip('\r\n')
            try:
                start_x = map_line.index(2)
                start_y = len(gay_map)-1
            except:
                pass
        try:
            exit_x = gay_map[len(gay_map)-1].index(1)
            exit_y = len(gay_map)-1
        except:
            try:
                exit_x = gay_map[0].index(1)
                exit_y = 0
            except:
                try:
                    inverse_gay_map = list(zip (*gay_map))
                    exit_y = inverse_gay_map[0].index(1)
                    exit_x = 0
                except:
                    try:
                        exit_y = inverse_gay_map[len(inverse_gay_map)-1].index(1)
                        exit_x = len(inverse_gay_map)-1
                    except:
                        print ("Can not find exit location")
                        pass
        print ("Exit location: (x",exit_x,", y",exit_y,")")
        return gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y
        #Exit = gay_map [y][x]
        #for i in gay_map:
        #    print (i)
def DFS (gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y):
    N = len (gay_map)
    M = len (gay_map[0])

    visited = np.full_like(gay_map, 0)
    # 0: Not visited yet
    # 1: Visited
    # 2: Visiting (in stack)
    
    result = np.full_like(gay_map, 0)
    # Cost of traversal to location [y][x]
    
    #cost = np.full_like(gay_map, 0) #WTF
    steps = np.array([[1,0],[-1,0],[0,1],[0,-1]])
    
    stack = deque()
    stack.append ((start_x, start_y))
    x = 0
    y = 0
    while (True):
        try:
            nigger = stack.pop()
            #[0] = x; [1] = y;
        except:
            return result
        #print (result)
        for direction in steps:
            if (0<=(nigger + direction)[0] < M) and (0<=(nigger + direction)[1] < N):
                x, y = (nigger + direction)
                if (gay_map[y][x]==0):
                    continue
                if (visited[y][x]==0) or (result[y][x] > result[nigger[1]][nigger[0]]+gay_map[y][x]):
                    result[y][x] = result[nigger[1]][nigger[0]]+gay_map[y][x]
                    if (visited[y][x]!=2):
                        visited[y][x] = 2
                        stack.append((x, y))
            else:
                continue
            visited[nigger[1]][nigger[0]] = 1
    return result

def BFS (gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y):
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
    while (True):
        try:
            nigger = queue.popleft()
            #[0] = x; [1] = y;
        except:
            return result
        for direction in steps:
            if (0<=(nigger + direction)[0] < M) and (0<=(nigger + direction)[1] < N):
                x, y = (nigger + direction)
                if (gay_map[y][x]==0):
                    continue
                if (visited[y][x]==0) or (result[y][x] > result[nigger[1]][nigger[0]]+gay_map[y][x]):
                    result[y][x] = result[nigger[1]][nigger[0]]+gay_map[y][x]
                    if (visited[y][x]!=2):
                        visited[y][x] = 2
                        queue.append((x, y))
            else:
                continue
            visited[nigger[1]][nigger[0]] = 1
    return result

if __name__ == "__main__":
    gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = ReadFile ("maze.txt")
    gay_map = np.array(gay_map)
    dfs = DFS (gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y)
    bfs = BFS (gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y)
    print (dfs)
    print (bfs)

    
