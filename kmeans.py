from parsing import *
import sys
import random
import pandas as pd
import time
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

def update_step(dataset):

    return dataset

def k_means(k, dataset, epsilon):
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
        distances_to_centroids['Cluster_{}'.format(index)] = (values)

    # Find the minimum distance value in the row
    # and store as a series in the dataframe
    distances_to_centroids['closest_cluster'] = distances_to_centroids.idxmin(axis=1)
    
    # Concatenate the dataset with the original set so that 
    # we can keep keep track of the original points
    # and their cluster assignment
    clusters_and_iris = pd.concat([distances_to_centroids, dataset], axis=1, sort=False)
    
    # Get headers of concatenated dataset
    headers = clusters_and_iris.columns

    # Strip irrelevant clusters from frame
    new_headers = []
    for header in headers:
        if 'Cluster_' not in header:
            new_headers.append(header)
    
    clusters_and_iris = pd.DataFrame(clusters_and_iris, columns=new_headers)

    clusters = clusters_and_iris['closest_cluster'].value_counts().sort_index(axis=0)

    for cluster in clusters.index:
        value_frame = clusters_and_iris.loc[clusters_and_iris['closest_cluster'] == cluster]
        value_frame = value_frame.drop(columns=['closest_cluster'])
        new_centroid = value_frame.mean(axis=0)
        new_centroid = new_centroid.values
        print("New Centroid for Cluster: " + cluster, new_centroid)

    centroids = 0
    print("Finished!")
    # Return centroids
    return new_centroid


if __name__ == "__main__":
    # Location of data file
    data_location = 'iris.arff'
    # Load data in to pandas dataframe
    data = load_pandas_data(data_location)
    # K user input
    k = int(sys.argv[1])
    # Epsilon error tolerance user input
    epsilon = float(sys.argv[2])
    # Number of iterations user input
    number_of_iterations = int(sys.argv[3])
        
    membership_change = float('inf')
    
    dimensions = k * [0]

    # Placeholder objects for the first k centroids to be compared
    # to in the epsilon check
    centers = [data.shape[1] * [float('inf')] for dimension in dimensions]
    # Instantiate while loop break
    # counter 
    x = 0
    while(x < number_of_iterations and membership_change > epsilon):
        start_time = time.time()
        centers = k_means(k, data, epsilon)
        # membership_change = check(centers, )
        time_taken = time.time() - start_time
        x += 1

    print("Time taken: {}".format(time_taken) + "s")
