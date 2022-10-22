import numpy as np
import os, glob
from collections import deque
from queue import PriorityQueue

import MazeDefault
import MazeReward
import MazeForce
import SupportFunction
#gay_dict = {'x': 0, ' ': 1, 'S': 2, 's': 2, '+': 3}
#fileName = "mazeForceMAXPOINT.txt"
customInputPath = "none"
def writeToFile (Path, num):
    with open(Path, mode='w') as f:
        if (num == 0):
            f.write("NO")
        else:
            f.write(str(num))
def makePath (filePath):
    #Create big level_xxx folder
    fileName = os.path.split(filePath)[1].split('.')[0]
    OutputFolderPath = os.path.join(os.path.split(filePath)[0], fileName)
    os.makedirs(OutputFolderPath, exist_ok=True)
    return OutputFolderPath
    
if __name__ == "__main__":
    if (customInputPath == "none"):
        customInputPath = "input"
        
    #DEFAULT MAP
    for filePath in glob.glob (os.path.join(customInputPath, "level_1", "*.txt")):
        gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = SupportFunction.ReadFile (filePath)

        #Create big level_xxx folder
        OutputFolderPath = makePath (filePath)
        
        #create algorithm's folder
        os.makedirs(os.path.join(OutputFolderPath, "dfs"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "bfs"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "ucs"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "bestfs"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "astar"), exist_ok=True)

        #Run Algo and export to file
        dfs, routeDFS = MazeDefault.DFS (gay_map, start_x, start_y, exit_x, exit_y)
        writeToFile(os.path.join(OutputFolderPath, "dfs", "output.txt"), dfs[exit_y][exit_x])

        bfs, routeBFS = MazeDefault.BFS (gay_map, start_x, start_y, exit_x, exit_y)
        writeToFile(os.path.join(OutputFolderPath, "bfs", "output.txt"), bfs[exit_y][exit_x])
        
        ucs, routeUCS = MazeDefault.UCS (gay_map, start_x, start_y, exit_x, exit_y)
        writeToFile(os.path.join(OutputFolderPath, "ucs", "output.txt"), ucs[exit_y][exit_x])
        
        bestfs, routeBESTFS = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 1)
        writeToFile(os.path.join(OutputFolderPath, "bestfs", "output.txt"), bestfs[exit_y][exit_x])
        
        astar, routeASTAR = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 0)
        writeToFile(os.path.join(OutputFolderPath, "astar", "output.txt"), astar[exit_y][exit_x])
        
    #Map with bonus points 
    for filePath in glob.glob (os.path.join(customInputPath, "level_2", "*.txt")):
        
        #Create big level_xxx folder
        makePath (filePath)
        
        #create algorithm's folder
        os.makedirs(os.path.join(OutputFolderPath, "algo"), exist_ok=True)
    
        cost, trace = MazeReward.MazeRewardSearch(gay_map, bonusP, start_x, start_y, exit_x, exit_y)
        
    #Map with forced points  
    for filePath in glob.glob (os.path.join(customInputPath, "level_3", "*.txt")):

        #Create big level_xxx folder
        makePath (filePath)
        
        #create algorithm's folder
        os.makedirs(os.path.join(OutputFolderPath, "algo1"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "algo2"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "algo3"), exist_ok=True)
    
        
        cost, trace = MazeForce.MazeForceSearch(gay_map, forceP, start_x, start_y, exit_x, exit_y, maxTime = 7.5)

    """         
    gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = SupportFunction.ReadFile (fileName)
    route = []
    #bonusP = []
    #forceP = []
    
    gay_map = np.array(gay_map)

    if (len(forceP)!=0):
<<<<<<< Updated upstream
        cost, trace = MazeForce.MazeForceSearch(gay_map, forceP, start_x, start_y, exit_x, exit_y, maxTime = 7.5)
        print (cost)
        print (trace)

    elif (len(bonusP)!=0):
        cost, trace = MazeReward.MazeRewardSearch(gay_map, bonusP, start_x, start_y, exit_x, exit_y)
        print (cost)
        print (trace)
=======
        cost, trace = MazeForce.MazeForceSearch(gay_map, forceP, start_x, start_y, exit_x, exit_y)    
        print(cost,trace)
    elif (len(bonusP)!=0):
        cost, trace = MazeReward.MazeRewardSearch(gay_map, bonusP, start_x, start_y, exit_x, exit_y)
        print(cost,trace)
        #print (trace)
        pass
>>>>>>> Stashed changes
    else:
        dfs, routeDFS = MazeDefault.DFS (gay_map, start_x, start_y, exit_x, exit_y)
        bfs, routeBFS = MazeDefault.BFS (gay_map, start_x, start_y, exit_x, exit_y)
        ucs, routeUCS = MazeDefault.UCS (gay_map, start_x, start_y, exit_x, exit_y)
        bestfs, routeBESTFS = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 1)
        astar, routeASTAR = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 0)
        print ("dfs")
        print (dfs)
        print (routeDFS)
        print ("bfs")
        print (bfs)
        print (routeBFS)
        print ("ucs")
        print (ucs)
        print (routeUCS)
        print ("bestfs")
        print (bestfs)
        print (routeBESTFS)
        print ("astar")
        print (astar)
        print (routeASTAR)"""

    
