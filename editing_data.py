import pandas as pd

# reading the raw data and viewing the summary.
df = pd.read_csv('bmw_global_sales__raw_dataset.csv')
print(df.head())

print("Original columns:", df.columns.tolist())

# Selecting the columns we need.
keep = [
    'year', 'month', 'country', 'model', 'segment', 'engine_type',
    'price_usd', 'units_sold', 'marketing_spend_usd', 'dealership_count'
]

df_clean = df[keep]

print("\nNew shape:", df_clean.shape)
print("Columns kept:", df_clean.columns.tolist())
print("\nFirst few rows:")
print(df_clean.head())

# Calculate profit_% = (marketing spend per unit) / price * 100
df_clean['profit_%'] = (df_clean['marketing_spend_usd'] / df_clean['units_sold']) / df_clean['price_usd'] * 100

# round to 2 decimal places for readability
df_clean['profit_%'] = df_clean['profit_%'].round(2)

print(df_clean.head())

# Creating start-of-month first
df_clean['period_start'] = pd.to_datetime(
    df_clean['year'].astype(str) + '-' +
    df_clean['month'].astype(str) + '-01'
)

# Then shifting to the last day of the month
df_clean['period_end'] = df_clean['period_start'] + pd.offsets.MonthEnd(0)

# creating readable string versions
df_clean['date'] = df_clean['period_end'].dt.strftime('%Y-%m-%d')   # → 2021-01-31


# droping original year & month columns now that we have period_end
df_clean = df_clean.drop(columns=['year', 'month', 'period_start', 'period_end'])

# Inserting 'date' at position 0 (first column)
df_clean.insert(0, 'date', df_clean.pop('date'))

# Creating a mapping dictionary (model → desired segment)
segment_mapping = {
    'X3':      'SUV',
    '3 Series': 'Sedan',
    'i4':      'Sedan',
    'X5':      'SUV',
    '7 Series': 'Sedan',
    'i7':      'Sedan',
    'X1':      'SUV',
    '5 Series': 'Sedan',
    'X7':      'SUV',
    'iX':      'Sedan',
}

# Updating the segment column based on model
df_clean['segment'] = df_clean['model'].map(segment_mapping)

# check which rows didn't match
unmapped = df_clean[df_clean['segment'].isna()]
if not unmapped.empty:
    print("Models that were not mapped:")
    print(unmapped['model'].value_counts())
else:
    print("All models were successfully mapped.")

print(df_clean.head())

# writing cleaned data to a new file
df_clean.to_csv('bmw_sales_cleaned.csv', index=False)
print("\nSaved to: bmw_sales_cleaned.csv")