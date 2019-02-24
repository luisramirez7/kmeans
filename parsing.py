from scipy.io import arff

def load_data(filename):
    data = arff.loadarff(filename)
    return data

data = load_data('iris.arff')
