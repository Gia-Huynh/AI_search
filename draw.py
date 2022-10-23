from fileinput import filename
import os
import matplotlib.pyplot as plt
from SupportFunction import *


def visualize_maze(matrix, bonus, start, end, route, OutputFilePath):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    #1. Define walls and array of direction based on the route
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]=='x']
    if route:
        route = [(NIGGER[1], NIGGER[0]) for NIGGER in route]
        direction=[]
        for i in range(1,len(route)):
            if route[i][0]-route[i-1][0]>0:
                direction.append('v') #^
            elif route[i][0]-route[i-1][0]<0:
                direction.append('^') #v        
            elif route[i][1]-route[i-1][1]>0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    #2. Drawing the map
    ax=plt.figure(dpi=100).add_subplot(111)

    for i in ['top','bottom','right','left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=100,color='black')
    
    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
                marker='P',s=100,color='green')

    plt.scatter(start[1],-start[0],marker='*',
                s=100,color='gold')

    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1][1],-route[i+1][0],
                        marker=direction[i],color='silver')

    try:
        plt.text(end[1], end[0],'EXIT',color='red',
             horizontalalignment='center',
             verticalalignment='center')
    except:
        pass
    plt.xticks([])  
    plt.yticks([])
    #plt.savefig(algo + ".jpg")
    plt.savefig (OutputFilePath)
    plt.close('all')
    #plt.show()

def read_file(file_name: str = 'maze.txt'):
  f=open(file_name,'r')
  n_bonus_points = int(next(f)[:-1])
  bonus_points = []
  for i in range(n_bonus_points):
    x, y, reward = map(int, next(f)[:-1].split(' '))
    bonus_points.append((x, y, reward))

  text=f.read()
  matrix=[list(i) for i in text.splitlines()]
  f.close()
  #github conflict
  start = []
  end = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]=='s' or matrix[i][j]=='S' :
            # temp = []
            # temp.append(i)
            # temp.append(j)
            start.append(i)
            start.append(j)
            start = tuple(start)
        elif matrix[i][j]==' ':
            if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                end.append(i)
                end.append(j)
                end = tuple(end)
            pass
    #print(start,end)
    #print("wat")
  return bonus_points, matrix, start, end

def drawImage (textInputPath, OutputFilePath, route):
    #print (route," ",OutputFilePath)
    bonus_points, matrix, start, end = read_file(textInputPath)
    visualize_maze(matrix,bonus_points,start,end, route, OutputFilePath)


"""
<<<<<<< Updated upstream

  return bonus_points, matrix

def draw(input_path,output_path, route,algo='bfs'):
    bonus_points, matrix = read_file('input_path')

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S' or matrix[i][j]=='s':
                start=(i,j)

            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)
                    
            else:
                pass

    visualize_maze(matrix,bonus_points,start,end)



if __name__ == "__main__":

    bonus_points, matrix = read_file('maze.txt')

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=(i,j)

            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)
                    
            else:
                pass

    visualize_maze(matrix,bonus_points,start,end)
=======
  start = []
  end = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]=='s' or matrix[i][j]=='S' :
            # temp = []
            # temp.append(i)
            # temp.append(j)
            start.append(i)
            start.append(j)
            start = tuple(start)
        elif matrix[i][j]==' ':
            if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                end.append(i)
                end.append(j)
                end = tuple(end)
            pass
    print(start,end)
  return bonus_points, matrix, start, end


bonus_points, matrix, start, end = read_file('maze.txt')
# chay thuat toan lay route va thay vào hàm bên dưới khúc route = 
visualize_maze(matrix,bonus_points,start,end,route=None,algo='bfs')"""

