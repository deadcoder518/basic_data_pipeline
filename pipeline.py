import sys
import pandas as pd

filter_category = sys.argv[1]

df = pd.DataFrame({
    'category': ['A', 'B', 'A', 'C', 'B'],
    'value': [10, 20, 30, 40, 50]
})

filtered_df = df[df['category'] == filter_category]

print(filtered_df)
