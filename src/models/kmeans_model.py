#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by Cayson Seipel
# November 23, 2022
# OLA 4
# This project builds the K-means clustering algorithm. It takes in three arguments: the number of clusters, 
# a training set, and a testing set. The program performs K-means clustering and then
# assigns a class label to each cluster. Finally, the program validates the clusters on the test set.
# The number of correct predictions is output.
# Some code is modified from code given by Dr. Phillips for use in this assignment.

import sys, math
import numpy as np
import pandas as pd
from collections import Counter
import random as r

# Determines the new clusters from the input cluster list 
def newClusters(clusterList, data):
    closest = [[0, [0 for _ in data[0][:-1]]] for _ in clusterList]
    newClusters = [[] for cluster in clusterList]
    clusters = [[] for _ in clusterList]
    
    # Iterate through each row of the data
    for row in data:
        least = [np.inf, 0] # The closest cluster to the row
        
        # Iterate through the clusters
        for cluster in range(len(clusterList)):    
            # Determine the distance between the row and the current cluster
            compare = [(clusterList[cluster][loc] - row[loc])**2 for loc in range(len(clusterList[cluster]))]
            distance = sum(compare)**0.5
            
            # The distance is less than the currently closest cluster
            if distance < least[0]:
                least = [distance, cluster]
            elif distance == least[0] and closest[cluster][0] == 0:
                # Prioritize empty clusters if the distance is the same
                least = [distance, cluster]
            
        clusters[least[1]].append(row[-1]) # Class value for each node assigned to each cluster
        closest[least[1]][0] += 1 # Total rows closest to this cluster
        # Add row value to the list to help find new location
        closest[least[1]][1] = [closest[least[1]][1][x] + row[x] for x in range(len(row)-1)]
    
    # Find the new cluster locations
    for cluster in range(len(closest)):
        # The cluster has data assigned to it
        if closest[cluster][0] > 0:
            # Average the data to find new cluster
            newClusters[cluster] = [closest[cluster][1][x] / closest[cluster][0] for x in range(len(closest[cluster][1]))]
        else:
            # No data is assigned to the data so keep the cluster the same
            newClusters[cluster] = clusterList[cluster]
    
    return newClusters, clusters

# Assign a class value to each cluster
def assignClass(numClusters, classes, clusterList):
    # Assumes the classes are integers starting at zero
    classAssigned = clusterList.copy()
    
    for row in range(len(classes)):
        # Count the number occurances for each class
        counts = Counter(classes[row]).most_common()
        
        # Data exists that is closest to this cluster
        if len(counts) > 0:
            leastIndex = counts[0][1]
        else:
            # There is no data closest to this cluster
            # Assign a random class value to this cluster
            counts = [(0.0, r.randrange(0, numClusters))]
            leastIndex = counts[0][1]
        
        # Find the class value by majority vote
        for num in counts: 
            if num[1] != counts[0][1]:
                break
            elif num[0] < leastIndex: # Keep going to find the most occuring class but lowest class vaue
                leastIndex = num[0]
    
        # Assign the class value
        classAssigned[row].append(leastIndex)
    
    return classAssigned

# Test the clusters on the test data
def validate(clusterList, data):
    numCorrect = 0 # Number of items correct
    
    # Find the cluster the data is closest to
    for row in data:
        closest = [np.inf, 0]
        
        for cluster in range(len(clusterList)):
            compare = [(clusterList[cluster][loc] - row[loc])**2 for loc in range(len(clusterList[cluster]) - 1)]
            distance = sum(compare)**0.5
            
            # Tie is broken by cluster order
            if distance < closest[0]:
                closest = [distance, cluster]
        
        # If the predicted value matches, increase the number correct
        if row[-1] == clusterList[closest[1]][-1]:
            numCorrect += 1
        
    return numCorrect

def main():
    # get the training and test datasets
    if len(sys.argv) != 4:
        print("Error in ", sys.argv[0])
        sys.exit(1)
    else:
        num_clusters = int(sys.argv[1])
        train = np.loadtxt(sys.argv[2])
        test = np.loadtxt(sys.argv[3])
    
    # Initialize the clusters by taking the first k rows
    oldClusterList = [train[clust][:-1].copy() for clust in range(num_clusters)]
    # Priming new clusters for the while loop
    newClusterList, assignment = newClusters(oldClusterList, train)
    
    # Continue finding new clusters until they no longer change value
    while not np.array_equal(oldClusterList, newClusterList):
        oldClusterList = newClusterList 
        newClusterList, assignment = newClusters(oldClusterList, train)
    
    # Assign class values to the final clsuters 
    finalClusters = assignClass(num_clusters, assignment, newClusterList)
    
    # Print the number of predictions correct from the test data
    print(validate(finalClusters, test))
    
    return 0
    
if __name__ == "__main__":
    main()