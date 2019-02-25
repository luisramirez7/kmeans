from parsing import *
import sys
import random
import pandas as pd
import numpy as np
# Take distance measure of each transaction  
def take_distance(centroid, record):
    distance = []
    for vector in record:
        euclidean_distance = np.linalg.norm(vector-centroid)
        distance.append(euclidean_distance)
    
    return distance 

def k_means(k, dataset):
    random_centers = dataset.sample(n=k)
    
    centroids = list(random_centers.values)
    df = pd.DataFrame()
    # distance_frame = dataset.values - random_centers.values
    for index, centroid in enumerate(centroids):
        values = take_distance(centroid, dataset.values)
        df['Distance to Centroid_{}'.format(index)] = (values)
    
    
    # distances_to_centroids = pd.DataFrame()
    # distance = take_distance(random_centers[i], dataset)

    changed = False
    while changed:
        pass

if __name__ == "__main__":
    data_location = 'iris.arff'
    data = load_pandas_data(data_location)
    k = int(sys.argv[1])
    epsilon = float(sys.argv[2])
    k_means(k, data)
