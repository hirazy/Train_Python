import pandas as pd

# Source: Kaggle(https://www.kaggle.com/code/residentmario/indexing-selecting-assigning)

# Native accessors
# Native Python objects provide good ways of indexing data.
# Pandas carries all of these over, which helps make it easy to start with.

reviews = pd.DataFrame({'country': ['Italy', 'Portugal', 'France', 'France'],
                        'description': ['Aromas include tropical fruit, broom, brimston',
                                        'This is ripe and fruity, a wine that is smooth',
                                        'A dry style of Pinot Gris, this is crisp with',
                                        'Big, rich and off-dry, this is powered by inte'],
                        'designation': ['Vulkà Bianco', 'Avidagos', 'NaN', 'Lieu-dit Harth Cuvée Caroline', ],
                        'points': [87, 87, 90, 90],
                        'price': [None, 15.0, 32.0, 21.0],
                        'province': ['Sicily & Sardinia', 'Douro', 'Alsace', 'Alsace'],
                        'region_1': ['Etna', None, 'Alsace', 'Alsace'],
                        'region_2': [None, None, None, None],
                        'taster_name': ['Kerin O’Keefe', 'Roger Voss', 'Roger Voss', 'Roger Voss'],
                        'taster_twitter_handle': ['@kerinokeefe', '	@vossroger', '@vossroger', '@vossroger'],
                        'title': ['Nicosia 2013 Vulkà Bianco (Etna)', 'Quinta dos Avidagos 2011 Avidagos Red (Douro)',
                                  'Domaine Marcel Deiss 2012 Pinot Gris (Alsace)',
                                  'Domaine Schoffit 2012 Lieu-dit Harth Cuvée Car'],
                        'variety': ['White Blend', 'Portuguese Red', 'Pinot Gris', 'Gewürztraminer'],
                        'winery': ['Nicosia', 'Quinta dos Avidagos',
                                   'Domaine Marcel Deiss', 'Domaine Schoffit']
                        })

print("Data Frame " + str(reviews.head()))

# In Python, we can access the property of an object by accessing it as an attribute.
# A book object, for example, might have a title property,
# which we can access by calling book.title. Columns in a pandas DataFrame work in much the same way.

print(reviews.country)

# If we have a Python dictionary, we can access its values using the indexing ([]) operator.
# We can do the same with columns in a DataFrame:

print(reviews["country"])

# These are the two ways of selecting a specific Series out of a DataFrame.
# Neither of them is more or less syntactically valid than the other,
# but the indexing operator [] does have the advantage that it can handle column names with reserved characters in them (e.g. if we had a country providence column, reviews.country providence wouldn't work).

# Doesn't a pandas Series look kind of like a fancy dictionary? It pretty much is,'
# so it's no surprise that, to drill down to a single specific value,
# we need only use the indexing operator [] once more:
print(reviews['country'][0])

# Indexing in Panda
# The indexing operator and attribute selection are nice because they work just like they do in the rest of the Python ecosystem.
# As a novice, this makes them easy to pick up and use. However, pandas has its own accessor operators, loc and iloc.
# For more advanced operations, these are the ones you're supposed to be using.

# Get Object ad index selection of DataFrame
# Index-based selection
# Pandas indexing works in one of two paradigms. The first is index-based selection:
# selecting data based on its numerical position in the data. iloc follows this paradigm.
print("\nIloc \n" + str(reviews.iloc[0]))

# Retrieve first column
# Both loc and iloc are row-first, column-second.
# This is the opposite of what we do in native Python, which is column-first, row-second.
#
# This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns.
# To get a column with iloc, we can do the following:
print('\nRetrieve first column\n' + str(reviews.iloc[:, 0]))

# On its own, the : operator, which also comes from native Python, means "everything".
# When combined with other selectors, however, it can be used to indicate a range of values.
# For example, to select the country column from just the first, second, and third row, we would do:
# From Row 1 -> 3, Column 0
print('\nRetrieve 3rd row\n' + str(reviews.iloc[:3, 0]))

# Or, to select just the second and third entries, we would do:
print('\nRetrieve 2-3rd row\n' + str(reviews.iloc[1:3, 0]))

# It's also possible to pass a list:
print('\nRetrieve 0, 2, 3 row\n' + str(reviews.iloc[[0, 2, 3], 0]))

# => First is Row, Second is Column

# Finally, it's worth knowing that negative numbers can be used in selection.
# This will start counting forwards from the end of the values.
# So for example here are the last five elements of the dataset

print('\nRetrieve 2, 1, 0 row\n' + str(reviews.iloc[-3:, 0]))

# Label-based selection

# The second paradigm for attribute selection is the one followed by the loc operator: label-based selection.
# In this paradigm, it's the data index value, not its position, which matters.

print('\nRetrieve by attribute selection\n', str(reviews.loc[0, 'country']))

# iloc is conceptually simpler than loc because it ignores the dataset's indices.
# When we use iloc we treat the dataset like a big matrix (a list of lists), one that we have to index into by
# while position: loc, by contrast, uses the information in the indices to do its work.
# Since your dataset usually has meaningful indices, it's usually easier to do things using loc instead.
# For example, here's one operation that's much easier using loc:
print('\nRetrieve by attribute selection\n', str(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]))

# Choosing between loc and iloc
# When choosing or transitioning between loc and iloc, there is one "gotcha" worth keeping in mind,
# which is that the two methods use slightly different indexing schemes.
# iloc uses the Python stdlib indexing scheme,
# where the first element of the range is included and the last one excluded.
# So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.
# Why the change? Remember that loc can index any stdlib type: strings, for example.
# If we have a DataFrame with index values Apples, ..., Potatoes, ...,
# and we want to select "all the alphabetical fruit choices between Apples and Potatoes",
# then it's a lot more convenient to index df.loc['Apples':'Potatoes']
# than it is to index something like df.loc['Apples', 'Potatoet'] (t coming after s in the alphabet).
# This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000.
# In this case df.iloc[0:1000] will return 1000 entries, while df.loc[0:1000] return 1001 of them!
# To get 1000 elements using loc, you will need to go one lower and ask for df.loc[0:999].
# Otherwise, the semantics of using loc are the same as those for iloc.

# Manipulating the index

# Label-based selection derives its power from the labels in the index.
# Critically, the index we use is not immutable. We can manipulate the index in any way we see fit.

# The set_index() method can be used to do the job.
# Here is what happens when we set_index to the title field:
reviews.set_index("title")

print('\nRetrieve\n' + str(reviews.head()))

# Conditional selection
# So far we've been indexing various strides of data, using structural properties of the DataFrame itself.
# To do interesting things with the data, however, we often need to ask questions based on conditions.

print('\nRetrieve\n' + str(reviews.country == 'Italy'))

# This operation produced a Series of True/False booleans based on the country of each record.
# This result can then be used inside of loc to select the relevant data:

print('\nRetrieve\n' + str(reviews.loc[reviews.country == 'Italy']))

# We also wanted to know which ones are better than average.
# Wines are reviewed on a 80-to-100 point scale, so this could mean wines that accrued at least 90 points.
print('\nRetrieve\n' + str(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]))

print('\nRetrieve\n' + str(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]))

# The first is isin. isin is lets you select data whose value "is in" a list of values.
# For example, here's how we can use it to select wines only from Italy or France:
print('\nRetrieve\n' + str(reviews.loc[reviews.country.isin(['Italy', 'France'])]))

# The second is isnull (and its companion notnull).
# These methods let you highlight values which are (or are not) empty (NaN).
# For example, to filter out wines lacking a price tag in the dataset, here's what we would do:
print('\nRetrieve\n' + str(reviews.loc[reviews.price.notnull()]))

# Assigning data

reviews['critic'] = 'everyone'
print('\nRetrieve\n' + str(reviews.head()))

# Or with an iterable of values:
reviews['index_backwards'] = range(len(reviews), 0, -1)
print('\nRetrieve\n' + str(reviews.head()))

# reviews.loc[:9, "description"]

# df = reviews.loc[[0, 1, 10, 100], ["country", "province", "region_1", "region_2"]]
# Label 0, 1, 10, 100, Column: country, province, region_1, region_2

# Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
italian_wines = reviews.loc[(reviews.country == 'Italy')]

# Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100)
# for wines from Australia or New Zealand.
top_oceania_wines = reviews.loc[(reviews.points >= 95) & (reviews.country.isin(['Australia','New Zealand']))]