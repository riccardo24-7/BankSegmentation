import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

FILEPATH = 'dataset.csv'
check_path = os.path.isfile(FILEPATH)

def loadData():
    if check_path:
        df = pd.read_csv(FILEPATH)
        return df.drop(['CUST_ID'],axis = 1)

# print(df.isnull().sum())
# print(df.describe())
# print(df.isna().mean()*100)

def distribution(df):
    for column in df.columns:
        plt.figure(figsize = (30,5))
        sns.histplot(df[column])
        plt.show()
        
def trends(df):
    for column in df.columns:
        plt.figure(figsize = (30,5))
        sns.boxplot(df[column])
        plt.show()