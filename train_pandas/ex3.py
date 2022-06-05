import pandas as pd

# Source: Kaggle(https://www.kaggle.com/code/lcnng123/exercise-summary-functions-and-maps/edit)

reviews = pd.read_csv('../data/pandas_data.csv')

# Get Mean of points
mean_points = reviews.points.mean()

# Get Median of points
median_points = reviews.points.median()

# Get Unique Countries
countries = reviews.country.unique()

# How often does each country appear in the dataset?
# Create a Series reviews_per_country mapping countries to the count of reviews of wines from that country.
reviews_per_country = pd.Series(reviews.country.value_counts())

# I'm an economical wine buyer. Which wine is the "best bargain"?
# Create a variable bargain_wine with the title of the wine with the highest points-to-price ratio in the dataset.
