import train_pandas as pd

# Source: Kaggle(https://www.kaggle.com/code/residentmario/creating-reading-and-writing)

# Create Data Frame
# DataFrame¶
# A DataFrame is a table. It contains an array of individual entries,
# each of which has a certain value. Each entry corresponds to a row (or record) and a column.
data = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

data.to_csv('cows_and_goats.csv')

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

# A Series, by contrast, is a sequence of data values. If a DataFrame is    a table, a Series is a list.
# And in fact you can create one with nothing more than a list
pd.Series([1, 2, 3, 4, 5])
pd.Series([30, 35, 40],
          index=['2015 Sales', '2016 Sales', '2017 Sales'],
          name='Product A')

# Reading data files
# Data can be stored in any of a number of different forms and formats.
# By far the most basic of these is the humble CSV file.
# Format Open
# Product A,Product B,Product C,
# 30,21,9,
# 35,34,1,
# 41,11,11

# Read File
# We'll use the pd.read_csv() function to read the data into a DataFrame.
wine_reviews = pd.read_csv("data/salary_data.csv")

# We can use the shape attribute to check how large the resulting DataFrame is:
print("Shape " + str(wine_reviews.shape))

# Head of File
print("Head " + str(wine_reviews.head()))

# The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify.
# For example, you can see in this dataset that the CSV file has a built-in index,
# which train_pandas did not pick up on automatically. To make train_pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.
wine_reviews = pd.read_csv(".data/salary_data.csv", index_col=0)
# index_col Column Start
print("Head " + str(wine_reviews.head()))
