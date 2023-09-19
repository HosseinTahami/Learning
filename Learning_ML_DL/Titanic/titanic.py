import pandas as pd
import numpy as np


import matplotlib.pyplot as mpl
from sklearn.linear_model import LogisticRegression


data = pd.read_csv("titanic.csv")
mpl.scatter(data["Age"], data["Survived"])
