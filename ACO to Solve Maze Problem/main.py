#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from node import Node
from ant import Ant
import matplotlib.pyplot as plt
f = open("maps/map1.txt", "r")
dataList = []
for x in f:
    x =x.replace('S','2')
    x = x.replace('B','0')
    x = x.replace('O','1')
    x= x.replace('E','3')
    dataList.append(x.split())
node_list = []
for i in range(len(dataList)):
    for j in range(len(dataList)):
        if(dataList[i][j]=='1' or dataList[i][j]=='2' or dataList[i][j]=='3'):
            node_list.append([i,j])
if __name__ == '__main__':
    nodes = {}
    for nodeCoor in node_list:
        nodes[tuple(nodeCoor)] = Node(tuple(nodeCoor))
    for nodeCoor in nodes:
        for x in range(len(dataList)+1):
            for y in range(len(dataList)+1):
                if (x, y) != nodeCoor and Ant.keyExist(nodes, (x,y)):
                    if (x==nodeCoor[0] and abs(y-nodeCoor[1]) == 1) or (y==nodeCoor[1] and abs(x-nodeCoor[0]) == 1):
                        nodes[nodeCoor].add_connected_node(nodes[(x, y)])
    
    entry = (0,0)
    ex = (0,0)
    for i in range(len(dataList)):
        for j in range(len(dataList)):
            if(dataList[i][j]=='2'):
                entry = (i,j)
            if(dataList[i][j]=='3'):
                ex = (i,j)
    #Edit these variables to edit the maze 
    entrance = nodes[entry]
    exits = [nodes[ex]]
    mazeSize = [len(dataList), len(dataList)] #[x, y]
    n_ant = 20
    alpha = 1
    rho = 0.1
    initial_pheromone = 0.1
    for nodeCoor in nodes:
        nodes[nodeCoor].set_pheromone(initial_pheromone)
    ants = [Ant() for _ in range(n_ant)]
        
    max_iteration = 200
    percentage_of_dominant_path = 0.9
    iteration = 0
    
    while iteration < 50 :
        for ant in ants:
            ant.reset()
            ant.get_path(entrance, exits, alpha)
        
        for node in nodes:
            nodes[node].evaporate_pheromone(rho)
            nodes[node].deposit_pheromone(ants)
            
        iteration += 1
        print("Iteration : ",iteration)
        
    paths = []
    pathsCount = []
    for ant in ants:
        if ant.nodes not in paths:
            paths.append(ant.nodes)
            pathsCount.append(1)
        else:
            pathsCount[paths.index(ant.nodes)] += 1
    pathIndex = pathsCount.index(max(pathsCount))
    solution = paths[pathIndex]
    print("Solution = [", end = "")
    x1 = []
    y1 = []
    for i in range(len(solution)):
        x1.append(solution[i].coordinates[0])
        y1.append(solution[i].coordinates[1])
    
    for i in range(len(solution)-1):
        print(solution[i].coordinates, end = ", ")
    print(str(solution[-1].coordinates) + "]")
    print("Path Length: " + str(len(solution)))
    print("Iteration: " + str(iteration))
    from matplotlib import pyplot
    data = []
    for i in range(len(dataList)):
        newList = []
        for j in range(len(dataList)):
            if(dataList[i][j]=='1' or dataList[i][j]=='2' or dataList[i][j]=='3'):
                newList.append(1)
            else:
                newList.append(0)
        data.append(newList)
    pyplot.figure(figsize=(5,5))
    plt.title("Path from " +str(entry)+" To " +str(ex))
    plt.imshow(data, cmap='gray')
    plt.plot(y1,x1,color='red')
    plt.scatter([entry[1]],[entry[0]],color='green')
    plt.scatter([ex[1]],[ex[0]],color='blue')
    
    pyplot.show()
            
        
        
        


