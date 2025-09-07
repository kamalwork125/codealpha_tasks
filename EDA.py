import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("titanic.csv")
#show first rows
print(df.head())
#check dataset info
print(df.info())
#missing values
print("NULL VALUES:", df.isnull().sum())
#survival count
sns.countplot(x="Survived",data=df)
plt.title("survival count")
plt.show()
#Survival by gender
sns.countplot(x="Survived",hue="Sex",data=df)
plt.title("Survival by gender")
plt.show()
#Age distribution
sns.histplot(df["Age"].dropna(),bins=20,kde=True)
plt.title("Age Distribution")
plt.show()
