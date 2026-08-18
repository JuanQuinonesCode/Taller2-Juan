import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("BikePrices.csv")

print(df.head())

df.dropna(axis='columns')

print(df['Brand'].value_counts())

print("Correlación entre Year y KM_Driven:", df['Year'].corr(df['KM_Driven']))
print("Correlación entre KM_Driven y Price:", df['KM_Driven'].corr(df['Selling_Price']))
print("Correlación entre Year y Ex_Showroom_Price:", df['Year'].corr(df['Ex_Showroom_Price']))

print("Correlación entre Ex_Showroom_Price y Selling_Price:", df['Ex_Showroom_Price'].corr(df['Selling_Price']))

sns.violinplot(x=df['Year'])
plt.show()