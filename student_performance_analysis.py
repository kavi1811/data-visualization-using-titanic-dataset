#!/usr/bin/env python
# coding: utf-8

# # import neccessary library and load dataset
# 

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


df=pd.read_csv(r"C:\Users\kavi\Downloads\archive (14)\student-por.csv")
df.head()


# In[ ]:


df.shape


# In[ ]:


df.isnull().sum()


# # calculating average grade, student scored above 15,calculating correlation and gender performance 

# In[ ]:


average_g3 = df["G3"].mean()
print("Average final grade (G3):", average_g3)

above_15 = df[df["G3"] > 15].shape[0]
print("Students scored above 15:", above_15)

correlation = df["studytime"].corr(df["G3"])
print("Correlation between study time and G3:", correlation)

gender_performance = df.groupby("sex")["G3"].mean()
print(gender_performance)




# # visualization in plots
# 

# In[ ]:


# Histogram
plt.figure()
plt.hist(df["G3"])
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.title("Histogram of Final Grades")
plt.savefig("charts/Histogram of Final Grades.png", dpi=150, bbox_inches='tight')
plt.show()

# Scatter plot
plt.figure()
plt.scatter(df["studytime"], df["G3"])
plt.xlabel("Study Time")
plt.ylabel("Final Grade (G3)")
plt.title("Study Time vs Final Grade")
plt.savefig("charts/Study Time vs Final Grade.png", dpi=150, bbox_inches='tight')
plt.show()

# Bar chart
avg_gender = df.groupby("sex")["G3"].mean()
plt.figure()
avg_gender.plot(kind="bar")
plt.xlabel("Gender")
plt.ylabel("Average Final Grade (G3)")
plt.title("Average Grade by Gender")
plt.savefig("charts/Average Grade by Gender.png", dpi=150, bbox_inches='tight')
plt.show()

