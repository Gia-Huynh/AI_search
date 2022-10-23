import numpy as np
import os, glob
from collections import deque
from queue import PriorityQueue

import MazeDefault
import MazeReward
import MazeForce
import SupportFunction
import draw
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
    levelName = os.path.basename(os.path.split(filePath)[0])
    FatherPath = os.path.abspath(os.path.join(os.path.split(filePath)[0], '..', '..'))
    OutputFolderPath = os.path.join(FatherPath, 'output')
    #LevelFolderPath = os.path.join(os.path.split(filePath)[0], fileName)
    LevelFolderPath = os.path.join(OutputFolderPath, levelName, fileName)
    #print (LevelFolderPath)
    os.makedirs(LevelFolderPath, exist_ok=True)
    return LevelFolderPath
    
if __name__ == "__main__":
    if (customInputPath == "none"):
        customInputPath = "input"
        
    #DEFAULT MAP
    for filePath in glob.glob (os.path.join(customInputPath, "level_1", "*.txt")):
        gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = SupportFunction.ReadFile (filePath)
        print (filePath)
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
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "dfs", "output.jpg"), routeDFS)
        
        bfs, routeBFS = MazeDefault.BFS (gay_map, start_x, start_y, exit_x, exit_y)
        writeToFile(os.path.join(OutputFolderPath, "bfs", "output.txt"), bfs[exit_y][exit_x])
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "bfs", "output.jpg"), routeBFS)
        
        ucs, routeUCS = MazeDefault.UCS (gay_map, start_x, start_y, exit_x, exit_y)
        writeToFile(os.path.join(OutputFolderPath, "ucs", "output.txt"), ucs[exit_y][exit_x])
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "ucs", "output.jpg"), routeUCS)
        
        bestfs, routeBESTFS = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 1)
        writeToFile(os.path.join(OutputFolderPath, "bestfs", "output.txt"), bestfs[exit_y][exit_x])
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "bestfs", "output.jpg"), routeBESTFS)
        
        astar, routeASTAR = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 0)
        writeToFile(os.path.join(OutputFolderPath, "astar", "output.txt"), astar[exit_y][exit_x])
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "astar", "output.jpg"), routeASTAR)
    #Map with bonus points 
    for filePath in glob.glob (os.path.join(customInputPath, "level_2", "*.txt")):

        gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = SupportFunction.ReadFile (filePath)

        #Create big level_xxx folder
        OutputFolderPath = makePath (filePath)
        
        #create algorithm's folder
        os.makedirs(os.path.join(OutputFolderPath, "DiemThuong"), exist_ok=True)
    
        cost, RewardSearch = MazeReward.MazeRewardSearch(gay_map, bonusP, start_x, start_y, exit_x, exit_y)
        writeToFile(os.path.join(OutputFolderPath, "DiemThuong", "output.txt"), cost)
        
    #Map with forced points  
    for filePath in glob.glob (os.path.join(customInputPath, "level_3", "*.txt")):
        gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = SupportFunction.ReadFile (filePath)
        """print (filePath)
        print (gay_map)
        for a in range (0, len(gay_map)):
            print (len(gay_map[a]))"""
        #Create big level_xxx folder
        OutputFolderPath = makePath (filePath)
        
        #create algorithm's folder
        os.makedirs(os.path.join(OutputFolderPath, "algo1_vetcan"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "algo2_heuristic"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "algo3_kethop"), exist_ok=True)
    
        
        costVC, Vetcan = MazeForce.MazeForceSearchVetCan(gay_map, forceP, start_x, start_y, exit_x, exit_y, maxTime = 7.5)
        writeToFile(os.path.join(OutputFolderPath, "algo1_vetcan", "output.txt"), costVC)     
        costHeu, ForceSearch = MazeForce.MazeForceSearchHeuristic(gay_map, forceP, start_x, start_y, exit_x, exit_y, maxTime = 7.5)
        writeToFile(os.path.join(OutputFolderPath, "algo2_heuristic", "output.txt"), costHeu)

    
