#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This ACO from https://github.com/terrsoshi/MazeACO

from random import random

class Ant:
    def __init__(self):
        self.nodes = []
        
    def get_path(self, entrance, exits, alpha):
        self.nodes.append(entrance)
        while self.nodes[-1] not in exits:
            totalPheromone = 0
            if self.nodes[-1]!=entrance:
                if len(self.nodes[-1].connected_nodes)>1:
                    routes = [node for node in self.nodes[-1].connected_nodes if node != self.nodes[-2]]
                else:
                    routes = self.nodes[-1].connected_nodes
            else:
                routes = self.nodes[-1].connected_nodes
            for connected_node in routes:
                totalPheromone += (connected_node.pheromone**alpha)
            cumuPheromone = []
            cumu = 0
            for i in routes:
                prob = (i.pheromone**alpha)/totalPheromone
                cumu += prob
                cumuPheromone.append(cumu)
            randomNum = random()
            for i in range(len(cumuPheromone)):
                if randomNum <= cumuPheromone[i]:
                    nodeIndex = i
                    break
            
            self.nodes.append(routes[nodeIndex])
            
        newNodes = [self.nodes[0]]
        for i in self.nodes:
            for check in newNodes:
                index = newNodes.index(check)
                if i == check:
                    del newNodes[index:]
                    break
            newNodes.append(i)
        self.nodes = newNodes
    
    def get_path_length(self):
        return len(self.nodes)

    def reset(self):
        self.nodes = []  
    def get_percentage_of_dominant_path(ants):
        paths = []
        pathsCount = []
        for ant in ants:
            if len(ant.nodes) == 0:
                return 0
            if ant.nodes not in paths:
                paths.append(ant.nodes)
                pathsCount.append(1)
            else:
                pathsCount[paths.index(ant.nodes)] += 1
        percentage = max(pathsCount)/sum(pathsCount)
        return percentage 
    def keyExist(dicti, key): 
        if key in dicti.keys(): 
            return True
        else: 
            return False
    

