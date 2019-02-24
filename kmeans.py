from parsing import get_records
import sys
import random

# Take distance measure of each transaction  
def take_distance():
    return

def k_means(k, dataset):
    records = dataset
    random_centers = random.sample(records, k)

    changed = False
    while changed:
        pass

if __name__ == "__main__":
    data_location = 'iris.arff'
    data = get_records(data_location)
    k = int(sys.argv[1])
    k_means(k, data)
