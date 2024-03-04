import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
data_train = pd.read_csv("01_import_data/output/train.csv")
data_test = pd.read_csv("01_import_data/output/test.csv")
data_train.head()
data_train.info()

'''
#   Column                          Non-Null Count  Dtype  
---  ------                          --------------  -----  
 6   FAVC                            20758 non-null  object # One hot ecoding yes, no (Frequent consumption of high caloric food)
 7   FCVC                            20758 non-null  float64 # Frequency of consumption of vegetables
 8   NCP                             20758 non-null  float64 # Number of main meals
 9   CAEC                            20758 non-null  object # One hot encoding 'Sometimes', 'Frequently', 'no', 'Always' (Consumption of food between meals)
 11  CH2O                            20758 non-null  float64 (Consumption of water daily)
 12  SCC                             20758 non-null  object # One hot ecoding yes, no (Calories consumption monitoring)
 13  FAF                             20758 non-null  float64 # (Physical activity frequency)
 14  TUE                             20758 non-null  float64 # (Time using technology devices)
 15  CALC                            20758 non-null  object # one hot encoding 'Sometimes', 'no', 'Frequently' (Consumption of alcohol)
 16  MTRANS                          20758 non-null  object # One hot encoding 'Public_Transportation', 'Automobile', 'Walking', 'Motorbike', 'Bike' (Transportation used)
 17  NObeyesdad                      20758 non-null  object # One hot encoding 'Overweight_Level_II', 'Normal_Weight', 'Insufficient_Weight', 'Obesity_Type_III', 'Obesity_Type_II', 
 'Overweight_Level_I', 'Obesity_Type_I'
dtypes: float64(8), int64(1), object(9)
'''
data_train['NObeyesdad'].unique() # 7 valores para predecir 


variables_cat = ['CAEC', 'CALC', 'MTRANS']
variables_bin = ['Gender', 'family_history_with_overweight', 'FAVC', 'SMOKE', 'SCC']
le = LabelEncoder()

data_train = pd.get_dummies(data_train, columns=variables_cat)
data_test = pd.get_dummies(data_test, columns=variables_cat)

for i in range(len(variables_bin)):

    data_train[variables_bin[i]] = le.fit_transform(data_train[variables_bin[i]])
    data_test[variables_bin[i]] = le.fit_transform(data_test[variables_bin[i]])


data_train.to_csv("02_prepare_data/output/train.csv", index=False)
data_test.to_csv("02_prepare_data/output/test.csv", index=False)



