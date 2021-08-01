import numpy as np
import pandas as pd 
from sklearn import svm
import pickle
from pandas import read_csv
df = read_csv('Fish.csv')
df.rename(columns={'Length1':'Vertical_length(cm)', 'Length2':'Length(cm)', 'Length3':'Diagonal_length(cm)', 'Weight' : 'Weight(gr)', 'Height' : 'Height(Vertical_length without fins)(cm)' , 'Width' : 'Width(without gills)(cm)'}, inplace=True)
X= df[['Weight(gr)','Vertical_length(cm)','Length(cm)','Diagonal_length(cm)','Height(cm)','Width(cm)']]
y= df[['Species']]
model = svm.SVC(kernel='linear',C=30,gamma= 'auto',degree=3)
model.fit(X,y)
with open ('species_pickle','wb') as f:
    pickle.dump(model,f)
with open ('species_pickle' , 'rb') as f:
    MODEL=pickle.load(f)
