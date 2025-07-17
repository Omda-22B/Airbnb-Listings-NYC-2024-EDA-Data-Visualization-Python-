#!/usr/bin/env python
# coding: utf-8

# # Python Project EDA & Data Viz - AirBnB Listing 2024(New York)
# 

# Task 1. Importing All Dependencies
# 
# 

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Load the dataset from the specified path, ignoring encoding errors

data = pd.read_csv("D:/Python/datasets.csv",encoding_errors='ignore')


# In[3]:


# Display the first 5 rows of the dataset to inspect the columns and values

data.head()


# In[4]:


# Get the number of rows and columns in the dataset

data.shape


# In[5]:


# Display summary information about the dataset including column types and non-null counts

data.info()


# In[6]:


# Statistical Summary

data.describe()


# # Task 4: Data Cleaning
# 

# In[7]:


# Check and count missing (null) values in each column of the DataFrame
data.isnull().sum()


# In[8]:


# Drop all rows with any missing (null) values from the DataFrame
data.dropna(inplace=True)

# Check again for any remaining missing values in each column
data.isnull().sum()


# In[9]:


# Count the number of duplicate rows in the DataFrame

data.duplicated().sum()


# In[10]:


# Display all duplicate rows in the DataFrame
data[data.duplicated()]


# In[11]:


# Remove all duplicate rows from the DataFrame
data.drop_duplicates(inplace=True)

# Verify that no duplicate rows remain
data.duplicated().sum()


# In[12]:


# Display the data type of each column in the DataFrame

data.dtypes


# In[13]:


# Convert the 'id' column to data type 'object'
data['id'] = data['id'].astype(object)

# Convert the 'host_id' column to data type 'object'
data['host_id'] = data['host_id'].astype(object)

# Display the updated data types of all columns
data.dtypes


# # EDA
# 
# # Task 5: Data Analysis
# 
# # Univariate Analysis
# 
# 

# In[58]:


# Filter the data to include only listings with price less than 1500
df = data[data['price'] < 1500]

# Create a boxplot to visualize the distribution of prices
sns.boxplot(data=df, x='price')

# Add a title and axis labels
plt.title("Distribution of Prices Under $1500")
plt.xlabel("Price (USD)")
plt.ylabel("Frequency")
plt.show()


# In[59]:


plt.figure(figsize=(12, 6))

# Create a histogram to show the distribution of prices
sns.histplot(data=df, x='price', bins=50, color='skyblue')

# Add title and axis labels
plt.title('Price Distribution')
plt.xlabel("Price (USD)")
plt.ylabel("Frequency")

plt.show()


# In[60]:


# Availability distribution
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='availability_365', bins=30, kde=False, color='skyblue')
plt.title('Availability_365 Distribution')
plt.xlabel("Availability (days per year)")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


# In[61]:


# Display the data type of each column in the DataFrame
df.dtypes


# In[62]:


# Calculate the average price for each neighbourhood group
df.groupby('neighbourhood_group')['price'].mean()


# In[23]:


# Create a new column 'price per bed' by dividing 'price' by 'beds'
df['price per bed'] = df['price'] / df['beds']

# Display the first 5 rows of the DataFrame
df.head()


# In[25]:


# Calculate the average 'price per bed' for each neighbourhood group

df.groupby('neighbourhood_group')['price per bed'].mean()


# 
# # Bi Variable Analysis One variable depenency in another variable

# In[26]:


df.columns


# In[35]:


# Set the figure size before plotting
plt.figure(figsize=(10,6))

# Create a bar plot showing the average price for each neighbourhood group,
# with room types distinguished by color
sns.barplot(data=df, x='neighbourhood_group', y='price', hue='room_type')
plt.title("Average Price by Neighbourhood Group and Room Type")


# In[43]:


# Set the figure size before plotting
plt.figure(figsize=(10, 6))

# Create a scatter plot showing the relationship between number of reviews and price,
# with room types distinguished by color
sns.scatterplot(data=df, x='number_of_reviews', y='price', hue='room_type')

# Add a title to the scatter plot
plt.title("Price vs. Number of Reviews by Room Type")

# Label the x-axis
plt.xlabel("Number of Reviews")

# Label the y-axis
plt.ylabel("Price (USD)")

# Display the plot
plt.show()


# # ✅ Key Insights:
# Most bookings are priced under $500
# 
# The majority of data points are concentrated in the price range of $0–$500, indicating that most listings fall within this affordable range.
# 
# Inverse relationship between price and number of reviews
# Properties with higher prices tend to have fewer reviews, suggesting they may be less frequently booked.
# On the other hand, listings with a high number of reviews tend to have lower prices, which may indicate they are more popular or offer better value for money.
# 
# Room type distribution
# 
# Entire home/apt (orange) is the most common room type across almost all price ranges.
# 
# Private rooms (blue) are the second most common, appearing frequently, especially at lower price points.
# 
# Hotel rooms (green) and Shared rooms (red) appear less frequently, suggesting they are less popular or less available.
# 
# Presence of outliers
# Some listings have very high prices (above $1000) but relatively low numbers of reviews — these are likely luxury or rare properties.

# In[49]:


import seaborn as sns
import matplotlib.pyplot as plt

# Get unique room types
room_types = df['room_type'].unique()
num_types = len(room_types)

# Set overall figure size
plt.figure(figsize=(14, 4 * num_types))

# Loop through each room type and create a subplot
for i, room in enumerate(room_types):
    plt.subplot(num_types, 1, i + 1)
    
    # Filter data for current room type
    data_subset = df[df['room_type'] == room]
    
    # Plot the scatter plot
    sns.scatterplot(data=data_subset, x='number_of_reviews', y='price')
    
    # Set title and axis labels
    plt.title(f'Price vs. Number of Reviews — Room Type: {room}', fontsize=12)
    plt.xlabel('Number of Reviews')
    plt.ylabel('Price (USD)')

# Adjust layout and add main title
plt.suptitle('Price vs. Number of Reviews by Room Type', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()


# In[51]:


sns.pairplot(data=df, vars=['price', 'minimum_nights', 'number_of_reviews', 'availability_365'], hue='room_type')


# In[52]:





# In[57]:


# Set the figure size
plt.figure(figsize=(10, 7))

# Create the scatter plot of listings by location
sns.scatterplot(data=df, x='longitude', y='latitude', hue='room_type')

# Set the title and axis labels
plt.title("Geographic Distribution of Listings by Room Type", fontsize=14)
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Show the plot
plt.show()


# # 🗺️ Geographic Distribution Analysis of Listings
# The spatial distribution of listings across the city reveals several key patterns:
# 
# 1- High Concentration in Manhattan and Brooklyn
# 
# The majority of listings are densely clustered in Manhattan and Brooklyn, particularly in central, high-traffic neighborhoods. This indicates strong tourist activity and a high demand for short-term rentals in these boroughs.
# 
# 2- Dominance of Entire Homes and Private Rooms
# 
# Across all boroughs, Entire home/apartment and Private room listings are the most prevalent. Their widespread availability suggests they are the preferred accommodation types for both hosts and guests.
# 
# 3- Limited Presence of Hotel and Shared Rooms
# 
# Hotel rooms and Shared rooms appear infrequently on the map, reflecting either lower supply or reduced demand for these options in the short-term rental market.
# 
# 4- Low Listing Density in Staten Island
# 
# Staten Island shows noticeably fewer listings compared to other areas. This could be attributed to its geographical distance from central Manhattan and its lower popularity among tourists.
# 
# 

# In[ ]:




