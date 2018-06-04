# Load the csv file
import numpy as np
import pandas as pd 
from sklearn import svm 

#apparently pandas as pd is useful somehow 

dataFile = pd.DataFrame.from_csv("../scan_files.csv")
# download the file
raw_data = dataFile
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
print(dataset.shape)
# separate the data from the target attributes
