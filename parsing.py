from scipy.io import arff

# Load data using the scipy.io library to read arff files.
def load_data(filename):
    data = arff.loadarff(filename)
    return data

# Function that converts the test dataset to all numeric attributes.  Class attributes are converted to a binary vector and added to the numeric vector.
def convert_to_numeric_vector(datapoints):
    # binary vector to represent each class 
    versicolor = [0, 0, 1] 
    setosa = [0, 1, 0]
    virginica = [1, 0, 0]
    
    # initialize new array to collect the numeric records 
    numeric_datapoints = []
    for record in datapoints:
        record = list(record.tolist())

        # Strip original data vector of string and replace with binary representation
        if record[-1].decode('UTF-8') == 'Iris-virginica':
            record = record[:-1]
            record = record + virginica
        elif record[-1].decode('UTF-8') == 'Iris-setosa':
            record = record[:-1]
            record = record + setosa
        elif record[-1].decode('UTF-8') == 'Iris-versicolor':
            record = record[:-1]
            record = record + versicolor
        else:
            raise ValueError('Unrecognized class value.')
        numeric_datapoints.append(record)
    return numeric_datapoints

# function to take in the arff file and return the list of all records now in numeric form 
def get_records(filename):
    try:
        data = load_data(filename)
    except FileNotFoundError:
        print('Please input a valid filename or path. \'%s\' is not found' % filename)
        return 1
    records = convert_to_numeric_vector(data[0])
    return records
