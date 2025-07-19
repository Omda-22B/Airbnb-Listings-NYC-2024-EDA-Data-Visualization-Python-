# Airbnb Listings EDA Project: New York 2024 🏩 

# Project Overview 📌

This project explores Airbnb listings data in New York City using Exploratory Data Analysis (EDA) techniques. The aim is to uncover insights about pricing, availability, room types, and geographic trends to help both guests and hosts make informed decisions.
Libraries used: Pandas, NumPy, Matplotlib, Seaborn
________________________________________

# Objective 🎯

•	Analyze room types, prices, and availability across NYC neighborhoods.

•	Understand host behavior and listing patterns.

•	Detect and handle outliers in pricing.

•	Generate actionable insights and recommendations.

________________________________________
#Dataset Overview 📊

•	Entries: 20,765

•	Features: 22 columns including:

Column	- Description

id	- Unique listing ID

name	- Listing title

host_name - 	Name of the host
neighbourhood_group	Borough (e.g., Manhattan, Brooklyn)
latitude / longitude	Geolocation
room_type	Type of room (entire home, private room…)
price	Price per night
reviews_per_month	Avg. monthly reviews
availability_365	Available days per year
________________________________________


# Steps & Workflow 🔧

# Data Cleaning

•	Removed nulls in key columns: price, neighbourhood, beds.

•	Converted last_review to datetime.

•	Filtered outliers: Capped listings above $1,000 for better visualization.

# Exploratory Data Analysis (EDA)

•	Room Type Distribution:

Entire homes/apartments dominate the listings.

•	Neighborhood Insights:

Manhattan has the highest average prices.

•	Price Distribution:

Most listings fall between $50 - $300.

•	Review Trends:

Listings with high review counts tend to have lower prices.

•	Availability Patterns:

Listings available year-round often offer better value.

# Visualizations

•	Histograms & Boxplots – to analyze price distribution & outliers

•	Scatter Plots – to visualize location & pricing

•	Bar Charts – to show frequency by room type and neighborhood

•	Heatmaps – to identify feature correlations
________________________________________

# Key Findings & Insights

•	Price:
Manhattan is the most expensive borough; Brooklyn offers more affordable options.
•	Room Types:

- Entire homes/apartments are most common, followed by private rooms.

•	Outliers:
- Some listings exceed $10,000—likely luxury properties needing filtering.

•	Host Behavior:
- Some hosts manage multiple listings, indicating a professional presence.

•	Geographic Patterns:

- Listings are highly concentrated in central Manhattan and Brooklyn.
- Staten Island shows the lowest density—possibly due to lower tourist activity.
________________________________________
# Recommendations

For Guests:

- Look for listings with high availability and positive reviews.

- Consider private rooms in Brooklyn for affordable stays.
  
For Hosts:

- Improve availability and responsiveness to boost bookings.

- Manage competitive pricing within each borough.
________________________________________
🚀 How to Run the Project

1.	Clone the repo:
git clone https://github.com/your-username/airbnb-nyc-eda-2024.git
cd airbnb-nyc-eda-2024
2.	Install dependencies:
pip install -r requirements.txt
3.	Launch the notebook:
jupyter notebook airbnb_eda.ipynb
________________________________________

📈 Future Work

- Build machine learning models to predict price based on location and features.

- Perform sentiment analysis on reviews.

- Create interactive dashboards using Plotly or Tableau.
