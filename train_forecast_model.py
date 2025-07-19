import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings

# Ignore warnings from the ARIMA model for a cleaner output
warnings.filterwarnings("ignore")

print("--- Starting Model Training Script ---")

# --- 1. Load and Clean Data ---
try:
    df = pd.read_excel('Online Retail.xlsx')
    print("Dataset loaded.")
except FileNotFoundError:
    print("Error: 'Online Retail.xlsx' not found.")
    exit()

# Basic cleaning
df.dropna(subset=['CustomerID'], inplace=True)
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print("Data cleaning complete.")

# --- 2. Prepare Time Series Data ---
# Aggregate sales by month
monthly_sales = df.set_index('InvoiceDate')['TotalPrice'].resample('M').sum()
# The last month's data is incomplete, so we'll drop it for a more stable forecast
monthly_sales = monthly_sales[:-1]
print("Monthly sales data prepared.")

# --- 3. Train Forecasting Model (ARIMA) ---
# ARIMA is a standard model for time series forecasting.
# The (p,d,q) order is a simple starting point.
model = ARIMA(monthly_sales, order=(5, 1, 0))
model_fit = model.fit()
print("ARIMA model trained.")

# --- 4. Generate Forecast ---
# Forecast the next 6 months
forecast = model_fit.forecast(steps=6)
print("Sales forecast generated for the next 6 months.")

# --- 5. Prepare and Save Output ---
# Create a DataFrame for the forecast
forecast_dates = pd.date_range(start=monthly_sales.index[-1] + pd.DateOffset(months=1), periods=6, freq='M')
forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecast': forecast})

# Create a DataFrame for historical data
history_df = pd.DataFrame({'Date': monthly_sales.index, 'Sales': monthly_sales.values})

# Combine them
output_df = pd.concat([history_df.assign(Type='Historical'), forecast_df.rename(columns={'Forecast': 'Sales'}).assign(Type='Forecast')])

# Save to CSV
output_df.to_csv('forecast_output.csv', index=False)
print("Saved historical sales and forecast to 'forecast_output.csv'.")
print("--- Script Finished Successfully ---")