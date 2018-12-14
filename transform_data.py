import os
import numpy as np
import pandas as pd
from numpy import array, argsort

from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedShuffleSplit

# load training data in pandas dataframe
file_name = 'adult.data.csv'
data = pd.read_csv(file_name)
data_obj = data.select_dtypes(['object'])
data[data_obj.columns] = data_obj.apply(lambda x: x.str.strip())

# recode the class variable
data['class'] = data['class'].map({'<=50K': '1', '>50K': '0'})

column_list = list(data.columns)

# this column is removed it adds no meaning to the data
column_list.remove('fnlwgt')
data = data[column_list]
LABEL = 0

tmp = data[data['class'] == LABEL]
print('minority class data size: ' + str(len(tmp)))

f = open('feature_paragraph.txt','w')
tmp = pd.get_dummies(data[data['class'] == LABEL], columns=data.columns)
for i in range(len(tmp)):
    f.write(' '.join(tmp.columns[(tmp.iloc[i:i+1]).any().tolist()]) + ' \n')
f.close()
