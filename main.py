import numpy as np
import os, glob, time
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

#if __name__ == "__main__":
if (True):
    if (customInputPath == "none"):
        customInputPath = "input"
        #customInputPath = os.path.join("..","Input")
    #DEFAULT MAP
    old_time = time.time()
    for filePath in glob.glob (os.path.join(customInputPath, "level_1", "*.txt")):
        gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = SupportFunction.ReadFile (filePath)
        #print (filePath)
        #Create big level_xxx folder
        OutputFolderPath = makePath (filePath)
        
        #create algorithm's folder
        os.makedirs(os.path.join(OutputFolderPath, "dfs"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "bfs"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "ucs"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "bestfs"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "astar"), exist_ok=True)
        #Run Algo and export to file
        old_time = time.time()
        dfs, routeDFS = MazeDefault.DFS (gay_map, start_x, start_y, exit_x, exit_y)
        writeToFile(os.path.join(OutputFolderPath, "dfs", "dfs.txt"), dfs[exit_y][exit_x])
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "dfs", "dfs.jpg"), routeDFS)
        print ("dfs ",time.time() - old_time)
        old_time = time.time()
        

        bfs, routeBFS = MazeDefault.BFS (gay_map, start_x, start_y, exit_x, exit_y)
        writeToFile(os.path.join(OutputFolderPath, "bfs", "bfs.txt"), bfs[exit_y][exit_x])
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "bfs", "bfs.jpg"), routeBFS)
        print ("bfs ",time.time() - old_time)
        old_time = time.time()
        
        ucs, routeUCS = MazeDefault.UCS (gay_map, start_x, start_y, exit_x, exit_y)
        writeToFile(os.path.join(OutputFolderPath, "ucs", "ucs.txt"), ucs[exit_y][exit_x])
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "ucs", "ucs.jpg"), routeUCS)
        print ("ucs ",time.time() - old_time)
        old_time = time.time()

        
        bestfs, routeBESTFS = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 1, choice = 0)
        writeToFile(os.path.join(OutputFolderPath, "bestfs", "bestfs_heuristic_1.txt"), bestfs[exit_y][exit_x])
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "bestfs", "bestfs_heuristic_1.jpg"), routeBESTFS)
        print ("bestfs ",time.time() - old_time)
        old_time = time.time()
        bestfstwo, routeBESTFStwo = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 1, choice = 1)
        writeToFile(os.path.join(OutputFolderPath, "bestfs", "bestfs_heuristic_2.txt"), bestfstwo[exit_y][exit_x])
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "bestfs", "bestfs_heuristic_2.jpg"), routeBESTFStwo)

        
        old_time = time.time()
        astar, routeASTAR = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 0, choice = 0)
        writeToFile(os.path.join(OutputFolderPath, "astar", "astar_heuristic_1.txt"), astar[exit_y][exit_x])
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "astar", "astar_heuristic_1.jpg"), routeASTAR)
        print ("astar ",time.time() - old_time)
        astartwo, routeASTARtwo = MazeDefault.InformedSearch (gay_map, start_x, start_y, exit_x, exit_y, bestFirst = 0, choice = 1)
        writeToFile(os.path.join(OutputFolderPath, "astar", "astar_heuristic_2.txt"), astar[exit_y][exit_x])
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "astar", "astar_heuristic_2.jpg"), routeASTAR)
    
    #Map with bonus points 
    for filePath in glob.glob (os.path.join(customInputPath, "level_2", "*.txt")):

        gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = SupportFunction.ReadFile (filePath)

        #Create big level_xxx folder
        OutputFolderPath = makePath (filePath)
        
        #create algorithm's folder
        os.makedirs(os.path.join(OutputFolderPath, "DiemThuong"), exist_ok=True)
        old_time = time.time()
        cost, RewardSearch = MazeReward.MazeRewardSearch(gay_map, bonusP, start_x, start_y, exit_x, exit_y)
        print ("DiemThuong ",time.time() - old_time)
        writeToFile(os.path.join(OutputFolderPath, "DiemThuong", "DiemThuong.txt"), cost)
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "DiemThuong", "DiemThuong.jpg"), RewardSearch)
    #Map with forced points  
    for filePath in glob.glob (os.path.join(customInputPath, "level_3", "*.txt")):
        gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = SupportFunction.ReadFile (filePath)
        #Create big level_xxx folder
        OutputFolderPath = makePath (filePath)
        
        #create algorithm's folder
        os.makedirs(os.path.join(OutputFolderPath, "algo1_vetcan"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "algo2_heuristic"), exist_ok=True)
        os.makedirs(os.path.join(OutputFolderPath, "algo3_kethop"), exist_ok=True)
    
        
        old_time = time.time()
        costVC, Vetcan = MazeForce.MazeForceSearchVetCan(gay_map, forceP, start_x, start_y, exit_x, exit_y, maxTime = 5)
        writeToFile(os.path.join(OutputFolderPath, "algo1_vetcan", "algo1_vetcan.txt"), costVC)    
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "algo1_vetcan", "algo1_vetcan.jpg"), Vetcan)
        print ("algo1_vetcan ",time.time() - old_time)
        old_time = time.time()
        
        costHeu, Heuristic = MazeForce.MazeForceSearchHeuristic(gay_map, forceP, start_x, start_y, exit_x, exit_y, maxTime = 5)
        writeToFile(os.path.join(OutputFolderPath, "algo2_heuristic", "algo2_heuristic.txt"), costHeu)
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "algo2_heuristic", "algo2_heuristic.jpg"), Heuristic)
        print ("algo2_heuristic ",time.time() - old_time)
        old_time = time.time()
        
        costSmart, Smart = MazeForce.MazeForceSearchSmart(gay_map, forceP, start_x, start_y, exit_x, exit_y, maxTime = 5)
        writeToFile(os.path.join(OutputFolderPath, "algo3_kethop", "algo3_kethop.txt"), costSmart)
        draw.drawImage (filePath, os.path.join(OutputFolderPath, "algo3_kethop", "algo3_kethop.jpg"), Smart)
        print ("algo3_kethop ",time.time() - old_time)
        old_time = time.time()
    for filePath in glob.glob (os.path.join(customInputPath, "advance", "*.txt")):
        #gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y = SupportFunction.ReadFile (filePath)
        #Create big level_xxx folder
        OutputFolderPath = makePath (filePath)

    
