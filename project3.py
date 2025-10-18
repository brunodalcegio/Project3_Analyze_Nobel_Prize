# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Start coding here!
dt = pd.read_csv("nobel.csv")

# Load the dataset and find the most common gender and birth country
top_country = dt['birth_country'].value_counts(sort=True).index[0]
print("Most commonly awarded by country:", top_country)
top_gender = dt['sex'].value_counts(sort=True).index[0]
print("Most commonly awarded by sex:", top_gender)


# Create the US-born winners column
dt['countryflag'] = dt['birth_country'] == top_country
# Create the decade column
dt['decade'] = np.floor(dt['year'] / 10) 
dt['decade'] = np.floor(dt['decade'] * 10).astype(int)

# Finding the ratio. as_index=False saves in a new df
dfdecade = dt.groupby(['decade'], as_index=False).agg({"countryflag":"mean"})

# Identify the decade with the highest ratio of US-born winners
max_decade_usa = dfdecade[dfdecade['countryflag'] == dfdecade['countryflag'].max()]
max_decade_usa = max_decade_usa['decade'].values[0].astype(int)
print("the decade with the highest ratio of US-born winners:", max_decade_usa)


# Filtering for female winners where the value is True when sex is "Female"
dt['female_winner'] = dt['sex'] == "Female"

# Group by two columns then isolate the female_winner column and take the mean
dffemwin = dt.groupby(['decade','category'], as_index=False).agg({'female_winner':'mean' })

# Find the decade and category with the highest female winners
dffemwin = dffemwin[dffemwin['female_winner'] == dffemwin['female_winner'].max() ]

# Create a dictionary to extract the decade and category from the values you just saved
max_female_dict = {dffemwin['decade'].values[0] : dffemwin['category'].values[0]}
print("the decade and category with the highest female winners: ", max_female_dict)


# Filter the DataFrame for the rows with Female winners and find the earliest year and corresponding category in this subset.
female_winner = dt[dt['female_winner']] 
first_row = female_winner[female_winner['year'] == female_winner['year'].min()]
first_woman_name = first_row['full_name'].values[0]
first_woman_category = first_row['category'].values[0]
print("the first woman to receive a Nobel Prize was:", first_woman_name, "and the category was:", first_woman_category)


# Count the number of times each winner has won, then select those with counts of two or more, saving the full names as a list called repeats
winners = dt['full_name'].value_counts(sort=True)
repeat_list = list(winners[winners >= 2].index)
print("individuals or organizations have won more than one Nobel Prize throughout the years:", repeat_list)
