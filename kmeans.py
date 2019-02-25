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


def k_means(k, dataset, old_centers):
    # Make a list of those centroids values
    # i.e., k = 3, therefore centroids len = 3
    # vector elements
    centroids = list(old_centers)
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
    distances_to_centroids['closest_cluster'] = distances_to_centroids.idxmin(
        axis=1)

    # Concatenate the dataset with the original set so that
    # we can keep keep track of the original points
    # and their cluster assignment
    clusters_and_iris = pd.concat(
        [distances_to_centroids, dataset], axis=1, sort=False)

    # Get headers of concatenated dataset
    headers = clusters_and_iris.columns

    # Strip irrelevant clusters from frame
    # and store in new_headers
    new_headers = []
    for header in headers:
        if 'Cluster_' not in header:
            new_headers.append(header)

    # Create a dataframe out of the newly
    # stripped headers
    clusters_and_iris = pd.DataFrame(clusters_and_iris, columns=new_headers)

    # Assign the possible cluster membership classes
    # to clusters so that we may query the clusters and iris
    # dataframe to find new cluster centroids
    clusters = clusters_and_iris['closest_cluster'].value_counts(
    ).sort_index(axis=0)

    # New placeholder list to hold new centroid calculations
    new_centroids = list()

    # For each cluster class found
    # in clusters, find the mean of the
    # poitns that were assigned to that cluster
    for cluster in clusters.index:
        value_frame = clusters_and_iris.loc[clusters_and_iris['closest_cluster'] == cluster]
        value_frame = value_frame.drop(columns=['closest_cluster'])
        # Enforce that the mean is taken row-wise
        # with parameter axis set to 'index'
        centroid = value_frame.mean(axis='index')
        # Add the point to the new centroids list
        new_centroids.append(centroid.values)

    # Return new centroids
    return new_centroids


def main():
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
    # Membership change initialization
    # for comparison in while loop
    membership_change = float('inf')
    
    # Sample first k random centroid centers
    old_centers = data.sample(n=k).values

    # Instantiate while loop break counter
    x = 0
    # While the number of iterations has not been met
    # AND the membership change is greater than epsilon,
    # i.e., the change in clustering is minimal
    # run the k-means algorithm
    start_time = time.time()

    while(x < number_of_iterations and membership_change > epsilon):
        new_centers = k_means(k, data, old_centers)
        new_centers = np.array(new_centers)
        old_centers = np.array(old_centers)
        value = new_centers - old_centers
        membership_change = np.sum((value)**2)
        old_centers = new_centers

        print("Iteration: {}".format(x))
        for index, cluster_ in enumerate(old_centers):
            print("Cluster {} centroid at".format(index), old_centers[index])

        print("Membership change since last iteration: {} \n".format(
            membership_change))

        x += 1

    time_taken = time.time() - start_time
    print("Total time taken: {}".format(time_taken) + "s")


if __name__ == "__main__":
    main()
