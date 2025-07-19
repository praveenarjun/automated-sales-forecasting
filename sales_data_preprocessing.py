import pandas as pd

# --- 1. Load the Dataset ---
# Load the CSV file into a pandas DataFrame.
# It's good practice to specify the file path.
file_path = 'forecast_output.csv'
try:
    df = pd.read_csv(file_path)
    print(f"Successfully loaded data from '{file_path}'\n")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure it's in the correct directory.")
    exit() # Exit if the file isn't found

# --- 2. Initial Data Inspection ---
# Get a quick overview of the DataFrame:
# - .head() shows the first few rows to understand the data structure.
# - .info() provides a summary including column names, non-null counts, and data types.
# - .describe() generates descriptive statistics for numerical columns.
# - .isnull().sum() counts missing values per column.

print("--- Initial Data Overview ---")
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataFrame Information:")
df.info()

print("\nDescriptive Statistics for Numerical Columns:")
print(df.describe())

print("\nMissing Values (Count per Column):")
print(df.isnull().sum())

# --- 3. Data Type Conversion ---
# The 'Date' column is currently an 'object' (string). It needs to be converted
# to a datetime object for time-series analysis and plotting.
print("\n--- Data Type Conversion ---")
df['Date'] = pd.to_datetime(df['Date'])
print("Converted 'Date' column to datetime objects.")
df.info() # Verify the change

# --- 4. Handling Duplicates (if any) ---
# Check for duplicate rows. If duplicates exist, you might choose to remove them
# depending on the context. For time-series data, exact duplicates are rare
# unless there's a data entry error.
print("\n--- Handling Duplicates ---")
initial_rows = df.shape[0]
df.drop_duplicates(inplace=True)
rows_after_duplicates = df.shape[0]

if initial_rows > rows_after_duplicates:
    print(f"Removed {initial_rows - rows_after_duplicates} duplicate rows.")
else:
    print("No duplicate rows found.")

# --- 5. Handling Missing Values (Imputation/Removal) ---
# Although df.isnull().sum() showed no missing values in this specific dataset,
# it's crucial to demonstrate how you would handle them.
# Common strategies include:
# - Removal: df.dropna() - removes rows with any missing values.
# - Imputation:
#   - Numerical: df['Column'].fillna(df['Column'].mean()) or .median()
#   - Categorical: df['Column'].fillna(df['Column'].mode()[0])
#   - Time-series: df['Column'].fillna(method='ffill') (forward fill) or 'bfill' (backward fill)

print("\n--- Handling Missing Values (Demonstration) ---")
if df.isnull().sum().sum() > 0:
    print("Missing values detected. Here's a placeholder for imputation strategy:")
    # Example: If 'Sales' had missing values, you might fill them with the mean
    # df['Sales'].fillna(df['Sales'].mean(), inplace=True)
    # print("Filled missing 'Sales' values with the mean.")
else:
    print("No missing values to handle in this dataset.")

# --- 6. Feature Engineering (Creating new, useful features) ---
# For time-series data, extracting components like year, month, day, or day of week
# can be very useful for further analysis (e.g., seasonal trends).
print("\n--- Feature Engineering ---")
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['DayOfWeek'] = df['Date'].dt.dayofweek # Monday=0, Sunday=6
df['WeekOfYear'] = df['Date'].dt.isocalendar().week.astype(int) # ISO week number
print("Added 'Year', 'Month', 'Day', 'DayOfWeek', and 'WeekOfYear' columns.")
print(df.head())

# --- 7. Data Segmentation (Separating Historical and Forecast) ---
# As identified, the 'Type' column allows for clear segmentation.
print("\n--- Data Segmentation ---")
historical_df = df[df['Type'] == 'Historical'].copy()
forecast_df = df[df['Type'] == 'Forecast'].copy()

print(f"Historical data points: {historical_df.shape[0]}")
print(f"Forecast data points: {forecast_df.shape[0]}")

print("\nFirst 5 rows of Historical Data:")
print(historical_df.head())

print("\nFirst 5 rows of Forecast Data:")
print(forecast_df.head())

# --- 8. Consistency Checks / Outlier Detection (Conceptual) ---
# For sales data, you might check for:
# - Negative sales values (if not allowed)
# - Unusually high or low sales values (outliers)
# While this dataset looks clean, demonstrating the thought process is key.
print("\n--- Consistency Checks (Conceptual) ---")
if (df['Sales'] < 0).any():
    print("Warning: Negative sales values found. Investigate data quality.")
else:
    print("No negative sales values detected.")

# Outlier detection (example using Z-score for numerical data):
# from scipy.stats import zscore
# df['Sales_Zscore'] = zscore(df['Sales'])
# outliers = df[(df['Sales_Zscore'] > 3) | (df['Sales_Zscore'] < -3)]
# if not outliers.empty:
#     print(f"Potential outliers detected in 'Sales' (Z-score > 3 or < -3):\n{outliers[['Date', 'Sales', 'Sales_Zscore']]}")
# else:
#     print("No significant outliers detected in 'Sales' based on Z-score method.")

print("\nData preprocessing complete. The data is now clean and ready for analysis and visualization.")
