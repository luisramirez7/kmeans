# Assignment 3 - Data Mining
### Jasmine Boyer and Luis Ramirez

# Getting Started
* Ensure you are have Python3 installed with libraries scipy, numpy, and pandas.

# Included Files
* iris.arff: This is the test data file that the kmeans clustering runs on.
* kmeans.py: This is the file that contains the main script to run the clustering on the iris dataset.
* parsing.py: This is the python file used to read in the data from the arff file.
* Assignment-3-Report.pdf: This is the file that contains our overall report and contribution sheet.

# Usage
* To run the clustering, execute the following command: 
  `python3 kmeans.py <k_value> <epsilon_value> <number_of_iterations>`
  * `k_value` is the number of clusters the program will produce.
  * `epsilon_value` is the change in the sum of the distances from the cluster centers.
  * `number_of_iterations` is the number of iterations the program will go through to find the best clustering.
* To run finding and plotting the optimal k values of the dataset, uncomment line 184 in kmeans.py
