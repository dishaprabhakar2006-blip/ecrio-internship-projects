import pandas as pd
df=pd.read_csv("titanic.csv")
print(df.head()) #prints first five rows
#1.
survived=df['Survived'].sum()
print("Survived Count:",survived)
print("Survival Percentage:",((survived/len(df))*100),'%')
#2.
avg_age=df.groupby('Pclass')[['Age']].mean()
print("Average Age in each Class:")
print(avg_age)
#3.
gender=df.groupby(["Pclass","Sex"]).size()
print("Males and Females Count in each class")
print(gender)
#4.
female_count=df[df['Sex']=='female']
female_percentage=(female_count['Survived'].sum())/len(female_count)*100
print("Percentage of Female Travellers who survived")
print(female_percentage,"%")
#5.
gender_count=df.groupby('Sex')['Survived'].mean()*100
print("Survival Rate by Gender:")
print(gender_count)
#6.
gender_median=df.groupby('Sex')['Age'].median()
print("Median Age of Male and Female Passengers:")
print(gender_median)
#7.
survivors_age=df.groupby('Survived')['Age'].mean()
print("Survivors and Non Survivors Average Age:\n",survivors_age)
#8.
age_40=df[df['Age']>40]
age_40_avg=age_40['Age'].mean()
print("Passengers above 40 years of age:")
print(age_40)
print("Average Age of Passergers above 40 years of Age:\n",age_40_avg)
#9.
def age_group(age):
    if pd.isna(age): return "Unknown"
    elif age<18: return "Child"
    elif age>18 and age<60: return "Adult"
    else: return "Senior" 
df['AgeGroup']=df['Age'].apply(age_group)
print("Age Group Column Added:")
print(df[['Age','AgeGroup']].head())
#10.
first_class=df[df['Pclass']==1]
first_fare_survivors=first_class[first_class['Survived']==1]
avg_fare=first_fare_survivors['Fare'].mean()
print("Average Fare of First Class Survivors:",avg_fare)
#11.
df.to_csv("cleaned.csv",index=False)
print("Cleaned dataset saved Successfully!")
#Unique Feature
def survival_summary(df):
    print("=== TITANIC SURVIVAL SUMMARY ===")
    print(f"Total Passengers: {len(df)}")
    print(f"Survived: {df['Survived'].sum()}")
    print(f"Survival Rate: {df['Survived'].mean()*100}%")
    print(f"Average Age: {df['Age'].mean()}")

survival_summary(df)
