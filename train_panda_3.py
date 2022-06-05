import pandas as pd

reviews = pd.read_csv('data/pandas_data.csv')

# Summary functions
# Pandas provides many simple "summary functions" (not an official name)
# which restructure the data in some useful way. For example, consider the describe() method:
# points
reviews.points.describe()

# This method generates a high-level summary of the attributes of the given column.
# It is type-aware, meaning that its output changes based on the data type of the input.
# The output above only makes sense for numerical data; for string data here's what we get:

reviews.taster_name.describe()

# If you want to get some particular simple summary statistic about a column in a DataFrame or a Series,
# there is usually a helpful pandas function that makes it happen.
#
# For example, to see the mean of the points allotted (e.g. how well an averagely rated wine does),
# we can use the mean() function:

reviews.points.mean()

# To see a list of unique values we can use the unique() function:
reviews.taster_name.unique()

# To see a list of unique values and how often they occur in the dataset,
# we can use the value_counts() method:
# Count frequencies of one value attribute: taster_name
reviews.taster_name.value_counts()

# Maps
# A map is a term, borrowed from mathematics,
# for a function that takes one set of values and "maps" them to another set of values.
# In data science we often have a need for creating new representations from existing data,
# or for transforming data from the format it is in now to the format that we want it to be in later.
# Maps are what handle this work, making them extremely important for getting your work done!
review_points_mean = reviews.points.mean()

# map() is the first, and slightly simpler one.
# For example, suppose that we wanted to remean the scores the wines received to 0. We can do this as follows:
# For each point
reviews.points.map(lambda p: p - review_points_mean)

# The function you pass to map() should expect a single value from the Series (a point value, in the above example),
# and return a transformed version of that value.
# map() returns a new Series where all the values have been transformed by your function.

# apply() is the equivalent method if we want to transform a whole DataFrame
# by calling a custom method on each row.

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

# If we had called reviews.apply() with axis='index',
# then instead of passing a function to transform each row,
# we would need to give a function to transform each column.
reviews.head(1)