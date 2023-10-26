#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv(r"C:\Users\Dell\Documents\Data Cleaning and Preprocessing.xlsx")

# Step 2: Handling Missing Values
# Example: Fill missing values in 'column_name' with the median
df['column_name'].fillna(df['column_name'].median(), inplace=True)

# Step 3: Handling Duplicates
df = df.drop_duplicates()

# Step 4: Handling Outliers
# Example: Remove outliers in 'numerical_column' using IQR
Q1 = df['numerical_column'].quantile(0.25)
Q3 = df['numerical_column'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['numerical_column'] >= lower_bound) & (df['numerical_column'] <= upper_bound)]

# Step 5: Data Validation
# Example: Convert 'date_column' to datetime and 'categorical_column' to the category data type
df['date_column'] = pd.to_datetime(df['date_column'])
df['categorical_column'] = df['categorical_column'].astype('category')

# Step 6: Save Cleaned Data
df.to_csv('cleaned_dataset.csv', index=False)

# Step 7: Exploratory Data Analysis (EDA)
# Example EDA using Pandas and Matplotlib
summary_stats = df.describe()  # Summary statistics
histogram = df['numerical_column'].hist()  # Histogram
scatter_plot = plt.scatter(df['x'], df['y'])  # Scatter plot
plt.show()


# In[ ]:




