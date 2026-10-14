#Week3 Pandas Tasks
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Read cars CSV file and transfer it into DataFrame
file_path = r"/Users/lumun/Developer/compact_programming_course/compact_programming_course/week_3/Cars93_missing.csv"  
cars_df = pd.read_csv(file_path)
print("1. DataFrame Loaded successfully. Shape:", cars_df.shape)

# 2. Transfer object Series into index column of the DataFrame
cars_df_indexed = cars_df.set_index('Model')
print("\n2. Transformed 'Model' column into Index:\n", cars_df_indexed.head(2))

# 3. Change the data in a column according to a condition
cars_df_modified = cars_df.copy()
# Condition: Set 'MPG.city' to 0 if it is less than 20
cars_df_modified.loc[cars_df_modified['MPG.city'] < 20, 'MPG.city'] = 0
print("\n3. Applied condition on 'MPG.city':\n", cars_df_modified[['Manufacturer', 'MPG.city']].head(5))

# 4. Get names of DataFrame columns and sum of missing (lost) values
column_names = cars_df.columns.tolist()
missing_values = cars_df.isnull().sum()
print("\n4. Column Names:", column_names)
print("\nSum of missing values per column:\n", missing_values[missing_values > 0])

# 5. Exchange 2 columns using a function & sort columns by name
def swap_columns(cars_df_in, col1, col2):
    cols = list(cars_df_in.columns)
    idx1, idx2 = cols.index(col1), cols.index(col2)
    cols[idx1], cols[idx2] = cols[idx2], cols[idx1]
    return cars_df_in[cols]

cars_df_swapped = swap_columns(cars_df, 'Manufacturer', 'Model')
cars_df_sorted_cols = cars_df.reindex(sorted(cars_df.columns), axis=1)
print("\n5. Sorted DataFrame columns alphabetically:\n", cars_df_sorted_cols.columns[:5])

# 6. Delete upper and lower 5% in object DataFrame
numeric_cars_df = cars_df.select_dtypes(include=[np.number])
q_low = numeric_cars_df.quantile(0.05)
q_high = numeric_cars_df.quantile(0.95)

# Filter rows within 5th and 95th percentiles
cars_df_trimmed = numeric_cars_df[~((numeric_cars_df < q_low) | (numeric_cars_df > q_high)).any(axis=1)]
print(f"\n6. Trimmed cars_df shape (after removing top/bottom 5%): {cars_df_trimmed.shape}")

# 7. Replace (Apply) missing values in the column with average values
cars_df_imputed = cars_df.copy()
numeric_cols = cars_df_imputed.select_dtypes(include=[np.number]).columns
cars_df_imputed[numeric_cols] = cars_df_imputed[numeric_cols].fillna(cars_df_imputed[numeric_cols].mean())
print("\n7. Missing values filled with column means. Nulls remaining:", cars_df_imputed[numeric_cols].isnull().sum().sum())

# 8. Create two DataFrames using two dicts, merge them, and append second cars_df as new column
dict1 = {'ID': [101, 102, 103], 'City': ['Dortmund', 'Bochum', 'Essen']}
dict2 = {'ID': [101, 102, 103], 'Students': [35000, 42000, 40000]}

cars_df1 = pd.DataFrame(dict1)
cars_df2 = pd.DataFrame(dict2)

# Merge
cars_df_merged = pd.merge(cars_df1, cars_df2, on='ID')

# Append as new column
cars_df1['Students_Count'] = cars_df2['Students']
print("\n8. Merged & Appended DataFrame:\n", cars_df1)

# 9. For any column create histogram
plt.figure(figsize=(6, 4))
cars_df['Price'].dropna().hist(bins=15, color='teal', edgecolor='black')
plt.title('Histogram of Price Column')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('price_histogram.png')
plt.close()
print("\n9. Histogram created and saved as 'price_histogram.png'")

# 10. Create Correlation Matrix for numeric columns
corr_matrix = numeric_cars_df.corr()
print("\n10. Correlation Matrix (preview 4x4):\n", corr_matrix.iloc[:4, :4])