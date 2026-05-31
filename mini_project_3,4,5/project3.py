import pandas as pd
df=pd.read_csv("titanic.csv")
print(df.head())
#1.
grp_data=df.groupby('Pclass').agg({'Age':'mean','Survived':'mean'})
print(grp_data)
#2.
df['Age_MinMax'] = (
    (df['Age'] - df['Age'].min())/
    (df['Age'].max() - df['Age'].min())
)
df['Avg_zscore']=((df['Age']-df['Age'].mean())/df['Age'].std())
print("Normalisation Completed")
print(df[['Age','Age_MinMax','Avg_zscore']].head())
#3.
df['Age']=df['Age'].fillna(df['Age'].mean())
print("Missing Age values are filled")
#4.
df['SexCode']=df['Sex'].map({'male':0,'female':1})
sexcode_survival=df.groupby('SexCode')['Survived'].sum()
print("Total No.of Survivors of each group in SexCode:\n",sexcode_survival)
#5.
def age_grp(age):
    if pd.isna(age): return "Unknown"
    elif age<18: return "Child"
    elif age>=18: return "Adult"
df['Age_group']=df['Age'].apply(age_grp)
print("Age Group column added\n",df[['Age','Age_group']].head())
#6.
pivot_table = df.pivot_table(
    values='Survived',
    index='Pclass',
    columns='SexCode',
    aggfunc='mean'
)
print("\nPivot Table:")
print(pivot_table)
