#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A utility class, which stores the information of all points and utilities of ants.
class Node:
    # Location, pheromone of the ant
    def __init__(self, coordinates, pheromone = 0):
        self.coordinates = coordinates #(x, y)
        self.pheromone = pheromone
        self.connected_nodes = []
        #Add a node, which is connected to the point. neighbour points
    def add_connected_node(self, node):
        if node not in self.connected_nodes:
            self.connected_nodes.append(node)
        # Add or set paeromone at that point. 
    def set_pheromone(self, pheromone):
        self.pheromone = pheromone
        # Evaporate phermonone from that point.
    def evaporate_pheromone(self, rho):
        self.pheromone = (1-rho) * self.pheromone
        # add pheromone at the point.
    def deposit_pheromone(self, ants):
        totalDeposition = 0
        for ant in ants:
            if self in ant.nodes:
                totalDeposition += (1/ant.get_path_length())
        self.pheromone += totalDeposition    


