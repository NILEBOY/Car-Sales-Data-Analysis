#!/usr/bin/env python
# coding: utf-8

# # DATA ANALYSIS ON CAR SALES DATASET

# In[1]:


import pandas as pd
data = pd.read_csv("Car Sales.xlsx - car_data.csv")
data


# # QUESTIONS TO BE ANSWERED
# 

# In[2]:


#1 What is the distribution of genders among the customers in the dataset?
#2 How is the annual income distributed among the customers?
#3 What are the unique car models and their respective companies present in the dataset?
#4 Provide a summary of the different body styles of cars available.
#5 Explore the distribution of car colors in the dataset.
#6 Who are the top customers based on the number of purchases?
#7 Identify the top dealers based on the number of transactions.
#8 Explore the regional distribution of dealers.
#9 What is the average price of cars in the dataset?
#10 Analyze the relationship between annual income and the price of cars.
#11 Identify the most expensive and least expensive car models.
#12 Explore any correlations between transmission types and car prices.


# In[2]:


#describing data
data.head()


# In[3]:


data.info() #Display information about the Dataframe


# In[4]:


data.describe() #Generate descriptive statistics


# In[5]:


#handling missing data
data.dropna() #Drop rows with missing values


# # 1. What is the distribution of genders among the customers in the dataset?

# In[7]:


data['Gender'].value_counts()


# # 2. How is the annual income distributed among the customers?

# In[8]:


print("Mean : ",data['Annual_Income'].mean())
print("Median : ",data['Annual_Income'].median())
print("Minimum : ",data['Annual_Income'].min())
print("Maximum : ",data['Annual_Income'].max())


# # 3. What are the unique car models and their respective companies present in the dataset?

# In[9]:


data.groupby(['Company','Model'])['Model'].count()


# # 4. Provide a summary of the different body styles of cars available.

# In[10]:


data['Body_Style'].value_counts()


# # 5. Explore the distribution of car colors in the dataset.

# In[11]:


data['Color'].value_counts()


# # 6 Who are the top customers based on the number of purchases?

# In[12]:


data.sort_values(by='Price',ascending = False).head(10)


# # 7. Identify the top dealers based on the number of transactions.

# In[13]:


data['Dealer_Name'].value_counts()


# # 8. Explore the regional distribution of dealers.

# In[14]:


data['Dealer_Region'].value_counts()


# # 9. What is the average price of cars in the dataset?

# In[15]:


print("Mean : ",data['Price'].mean())


# # 10. Analyze the relationship between annual income and the price of cars.

# In[16]:


correlation = data['Annual_Income'].corr(data['Price'])
print("Correlation : ",correlation)


# # 11. Identify the most expensive and least expensive car models.

# In[18]:


expensive = data.loc[data['Price'].idxmax()] # finding expensive model based on price ,and using its index value to show the details
cheap = data.loc[data['Price'].idxmin()]  # finding cheap model based on price ,and using its index value to show the details
print("Expensive : ",expensive)
print("\nCheap : ",cheap)


# # 12. Explore any correlations between transmission types and car prices.

# In[20]:


mean_p_t = data.groupby('Transmission')['Price'].mean()

print("Mean price for each transmission type:")
print(mean_p_t)

# Alternatively, you can calculate correlations between categorical and numerical variables
correlation = data.groupby('Transmission')['Price'].mean().corr(data.groupby('Transmission')['Price'].count())

print("\nCorrelation between transmission types and car prices:")
print(correlation)


# In[ ]:




