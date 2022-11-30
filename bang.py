import math 
import pandas as pd
import numpy as np
import scipy.spatial as sp
import sklearn as sk
from sklearn.neighbors import NearestNeighbors
from scipy.spatial import distance
import matplotlib.pyplot as plt

merc = pd.read_csv('bang2.csv')

fas = merc.iloc[1]
fes = merc.iloc[2]
names = merc['ATUN'].iloc[2];
print(names)