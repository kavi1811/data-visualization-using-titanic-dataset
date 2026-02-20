<<<<<<< HEAD


# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import plotly.express as px

df = pd.read_csv(r"E:\mini project\New folder\data analysis with titanic dataset\data analysis using titanic dataset\Titanic-Dataset.csv")

# Show first 5 rows
df.head()

df['Age'].fillna(df['Age'].mean(), inplace=True)
df.drop(columns=['Cabin'], inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=[0, 12, 18, 30, 50, 80],
    labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']
)
df['FamilySize'] = df['SibSp'] + df['Parch']

fig = px.histogram(df, x="Age", nbins=30, title="Age Distribution")
fig.show()

fig = px.bar(df, x="AgeGroup", y="Survived",
             title="Survival Rate by Age Group",
             color="AgeGroup")
fig.show()

fig = px.bar(df, x="Embarked", y="Survived",
             title="Survival Rate by Embarkation Port",
             color="Embarked")
fig.show()

fig = px.bar(df, x="FamilySize", y="Survived",
             title="Survival Rate by Family Size",
             color="FamilySize")
fig.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print(df.groupby('AgeGroup')['Survived'].mean())
print(df.groupby('Embarked')['Survived'].mean())
print(df.groupby('FamilySize')['Survived'].mean())

fig = px.scatter(df,
                 x="Age",
                 y="Fare",
                 color="Survived",
                 size="FamilySize",
                 hover_data=["Sex", "Pclass"],
                 title="Interactive Titanic Dashboard")

fig.show()
=======


# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import plotly.express as px

df = pd.read_csv(r"E:\mini project\New folder\data analysis with titanic dataset\data analysis using titanic dataset\Titanic-Dataset.csv")

# Show first 5 rows
df.head()

df['Age'].fillna(df['Age'].mean(), inplace=True)
df.drop(columns=['Cabin'], inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=[0, 12, 18, 30, 50, 80],
    labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']
)
df['FamilySize'] = df['SibSp'] + df['Parch']

fig = px.histogram(df, x="Age", nbins=30, title="Age Distribution")
fig.show()

fig = px.bar(df, x="AgeGroup", y="Survived",
             title="Survival Rate by Age Group",
             color="AgeGroup")
fig.show()

fig = px.bar(df, x="Embarked", y="Survived",
             title="Survival Rate by Embarkation Port",
             color="Embarked")
fig.show()

fig = px.bar(df, x="FamilySize", y="Survived",
             title="Survival Rate by Family Size",
             color="FamilySize")
fig.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print(df.groupby('AgeGroup')['Survived'].mean())
print(df.groupby('Embarked')['Survived'].mean())
print(df.groupby('FamilySize')['Survived'].mean())

fig = px.scatter(df,
                 x="Age",
                 y="Fare",
                 color="Survived",
                 size="FamilySize",
                 hover_data=["Sex", "Pclass"],
                 title="Interactive Titanic Dashboard")

fig.show()
>>>>>>> 58cdf8004c369e70bcab141e3f1da1a811498411
