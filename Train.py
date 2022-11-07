## LIBRARIES

import pandas as pd
import pickle
import statsmodels.api as sm
import math
from matplotlib import *
import sys
from pylab import *
import pylab as pl
from matplotlib import figure
from matplotlib import pyplot as plt
from sklearn.feature_extraction import DictVectorizer
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
import numpy as np
from scipy.stats import boxcox 
import pyreadr 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import scale 
import seaborn as sns 
import matplotlib as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import plotly.express as px
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
import xgboost as xgb

## Import datasets

por = pd.read_csv("/Users/alexandervalverde/Library/Mobile Documents/com~apple~CloudDocs/ML_Zoom_Camp/Dataset/student-por.csv")
por
df = pd.DataFrame(por)


## Create 2 list from df_num and df_cat

df_cat2 = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
       'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
       'nursery', 'higher', 'internet', 'romantic']

df_num2 = ['age', 'Fedu', 'traveltime', 'studytime', 'failures', 'famrel',
       'freetime', 'goout', 'Dalc', 'health', 'absences','G2']

y = df["G3"]
dv = DictVectorizer(sparse=False)
## CLEAN train data set
    
grad = df[df_cat2 + df_num2].to_dict(orient='rows')
    
dv = DictVectorizer(sparse=False)
dv.fit(grad)

X = dv.transform(grad)

model = Lasso(alpha=0.01)
model.fit(X, y)

## Save model
with open('/Users/alexandervalverde/Library/Mobile Documents/com~apple~CloudDocs/ML_Zoom_Camp/model.bin','wb') as f_out:
 pickle.dump((dv,model), f_out)