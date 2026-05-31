import pandas as pd
import matplotlib.pyplot as plt
#1.
df=pd.read_csv("titanic.csv")
df.columns=df.columns.str.strip()
print(df.head())
#2.
df['Age']=df['Age'].fillna(df['Age'].mean())
df=df.dropna(subset=['Embarked'])
print("Missing values are handled")
#3.
survival_count=df['Survived'].value_counts()
plt.bar(survival_count.index,survival_count.values)
plt.xlabel("Survived")
plt.ylabel("No of Passengers")
plt.title("Survivors vs Non Survivors")
plt.show()
#4.
df=df.drop_duplicates()
for col in df.select_dtypes(include='object').columns:
    df[col]=df[col].str.strip().str.lower()
    
print("Duplicate rows removed and data is clean and consistent")
#5.
df['Age']=df['Age'].astype(float)
df['Survived']=df['Survived'].astype(int)
print("Data Types are converted")
#6.
fig,axes=plt.subplots(1,2,figsize=(10,7))
gender_survival=df.groupby('Sex')['Survived'].mean()
axes[0].bar(gender_survival.index,gender_survival.values)
axes[0].set_title("Survival by Gender")
class_survival=df.groupby("Pclass")['Survived'].mean()
axes[1].bar(class_survival.index,class_survival.values)
axes[1].set_title("Survival by Class")
plt.tight_layout()
plt.show()
#7.
df.to_csv("cleaned_2.csv",index=False)
print("Cleaned data set saved")
#8.
colors=df['Survived']
plt.scatter(df['Age'],df['Fare'],c=colors)
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare")
plt.show()
#9.
df['Sex']=df['Sex'].str.lower()
print("Sex column standardised")
df.to_json("cleaned.json",orient='records')
print("Json File created")
