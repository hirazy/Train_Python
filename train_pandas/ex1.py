import pandas as pd
pd.set_option('max_rows', 5)
# from learntools.core import binder; binder.bind(globals())
# from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")



ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'],
          index=['Flour', 'Milk', 'Eggs', 'Spam'],
          name='Dinner')
# Flour     4 cups
# Milk       1 cup
# Eggs     2 large
# Spam       1 can
# Name: Dinner, dtype: object