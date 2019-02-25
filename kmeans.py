from parsing import *
import sys
import random
import pandas as pd
import numpy as np
# Take distance measure of each transaction  
def take_distance(centroid, record):
    # Instantite distance placeholder object
    # to store results of euclidean distance
    distance = []
    # For each vector in the record set
    # compute the euclidean distance
    # and stor it in the list of distances
    for vector in record:
        euclidean_distance = np.linalg.norm(vector-centroid)
        distance.append(euclidean_distance)
    
    # Return a series to be stored in distances frame
    return distance 

def k_means(k, dataset):
    # Sample K centroids at random from the dataframe
    random_centers = dataset.sample(n=k)
    # Make a list of those centroids values
    # i.e., k = 3, therefore centroids len = 3 
    # vector elements
    centroids = list(random_centers.values)
    # Instantiate an empty dataframe to store
    # the distances for each point from the starting
    # random centroids
    distances_to_centroids = pd.DataFrame()

    # For each centroid find the euclidean distance 
    # between the centroid and the point in question
    # Return this value as a series and store it in 
    # the column that is repectably named
    # i.e., Centroid 0 : distances from points to centroid
    for index, centroid in enumerate(centroids):
        values = take_distance(centroid, dataset.values)
        distances_to_centroids['Distance to Centroid_{}'.format(index)] = (values)


    distances_to_centroids['closest_cluster'] = distances_to_centroids.min(axis=1)
    
    distances_and_iris = pd.concat([distances_to_centroids, dataset],axis=1,sort=False)
    
    changed = False
    while changed:
        pass

if __name__ == "__main__":
    data_location = 'iris.arff'
    data = load_pandas_data(data_location)
    k = int(sys.argv[1])
    epsilon = float(sys.argv[2])
    k_means(k, data)
