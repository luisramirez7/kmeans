from scipy.io import arff
import pandas as pd

def load_pandas_data(filename):
    data = arff.loadarff(filename)
    df = pd.DataFrame(data[0])

    # Drop categorical values
    # Since Kmeans is an unsupervised algorithm
    # we don't have to assign class labels
    df = df.drop(columns=['class'])
    
    return df