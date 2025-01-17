# -*- coding: utf-8 -*-
"""SONAR_PROJ.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w2qjTTyMThHrtd4InJgF1gymis-KPA-w
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

s_data= pd.read_csv('/content/sonar.csv', header=None)

s_data.shape

s_data.describe()

s_data[60].value_counts()

s_data.groupby(60).mean()

a=s_data.drop(columns=60,axis=1)
b=s_data[60]

print(a)
print(b)

x_train,x_test,y_train,y_test=train_test_split(a,b,test_size=0.1,stratify=b,random_state=1)

print(a.shape,x_train.shape,x_test.shape)

model=LogisticRegression()

model.fit(x_train, y_train)

x_train_prediction=model.predict(x_train)
training_data_accuracy=accuracy_score(x_train_prediction,y_train)

print('accuracy on training data : ',training_data_accuracy)

input_data=(0.0100,0.0171,0.0623,0.0205,0.0205,0.0368,0.1098,0.1276,0.0598,0.1264,0.0881,0.1992,0.0184,0.2261,0.1729,0.2131,0.0693,0.2281,0.4060,0.3973,0.2741,0.3690,0.5556,0.4846,0.3140,0.5334,0.5256,0.2520,0.2090,0.3559,0.6260,0.7340,0.6120,0.3497,0.3953,0.3012,0.5408,0.8814,0.9857,0.9167,0.6121,0.5006,0.3210,0.3202,0.4295,0.3654,0.2655,0.1576,0.0681,0.0294,0.0241,0.0121,0.0036,0.0150,0.0085,0.0073,0.0050,0.0044,0.0040,0.0117)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)
prediction=model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]=='R'):
  print('the object is wrong')
else:
    print('the object is mine')

