# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qEmAaH6t74lWgOvLYmqmcQGLY9eaWX-j
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')

#1
ds = pd.read_csv('/content/Final Dataset - IPL.csv')
print("Shape: ",ds.shape)
print("Number of Rows: ",ds.shape[0])
print("Number of Columns: ",ds.shape[1])
print("\nTypes of Data")
print(ds.dtypes)
print("\n",ds.info())
print("\n\nMissing Values")
print(ds.isnull().sum())
print("\n\nDuplicate Values")
print(ds.duplicated().sum())

#2
na = ds.isnull().sum()
print(na)
#There are no null values that exists in any of the columns.
dup = ds.duplicated().sum()
print("\n\nDuplicates: ",dup)
#There are no duplicate values that exists in any of the columns.
#"Data is already clean no need to perform any operations

#3
numerical_data = ds.select_dtypes('int','float')
print("Mean\n\n",numerical_data.mean())
print("\nMedian\n",numerical_data.median())
print("\nMode of First Innings Wickets\n",numerical_data['first_ings_wkts'].mode())
ran = numerical_data['first_ings_score'].max() - numerical_data['first_ings_score'].min()
print("\nRange of First Innings Score\n",ran)
print("\nVariance\n",numerical_data.var())
print("\nStandard Deviation\n",numerical_data.std())

#4
ds.plot(kind='scatter', x='second_ings_score', y='second_ings_wkts')
plt.title("Second innings analysis")
plt.grid()
plt.show()

#4

toss = ds.groupby('toss_decision').size()
plt.title("Toss Decision Count")
plt.legend(ds['toss_decision'].unique())
plt.bar(ds['toss_decision'].unique(),ds['toss_decision'].value_counts())
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

#4

pie = ds.groupby('venue').size()
labels = ds['venue'].unique()
plt.pie(pie,labels = labels,autopct="%1.1f%%")
plt.title("Venue wise Matches")
plt.legend(labels = ds['venue'].unique())
plt.show()

#4
ds['second_ings_score'].plot(kind='hist', bins=20, title='Second Innings Score',color="green")
plt.grid()
plt.xlabel("Runs")
plt.show()

#5
num = ds[['first_ings_score','second_ings_score','first_ings_wkts','second_ings_wkts']]
correl = num.corr()
sns.heatmap(correl,annot=True)

#There is a huge positive correlation with the second innings score and the first innings score, when one is increased the other also is increased
#Whereas, there is a strong negative correlation between first innings score and first innings wickets when one goes down the other goes up

#6
sns.boxplot(ds,x='highscore',hue='stage')
#Outliers are detected for highscore values which is over 140 runs in the group stage
#It is best to keep the outlier because it is possible for a player to score 140 runs and it need not be discarded.

#7
trends = ds.groupby('match_winner').agg({'highscore': 'sum'})


trends['highscore'].plot(label='HighScore', color='blue')
plt.show()

#8
best = ds['player_of_the_match'].value_counts().head().plot(kind='bar')

#9
#i)Almost 3/4th of the matches were playes in the venue Ahmedabad and Mumbai
#ii)Kuldeep Yadav has the most number of Player of the match awards
#iii)When the toss is won by the team almost 60% of the time, fielding was chosen
#iv)The highest score is 222 which was achieved in the first innings
#v)The highest score by an individual is 140
#v)Chahal has the most number of best bowling figures 5