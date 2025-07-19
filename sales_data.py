import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# --- 1. Load the Preprocessed Data ---
# We'll reload the CSV and re-run the necessary preprocessing steps
# to ensure we have the DataFrame in the correct state for plotting.
file_path = 'forecast_output.csv'
df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'])

# Re-segment the data into historical and forecast DataFrames
historical_df = df[df['Type'] == 'Historical'].copy()
forecast_df = df[df['Type'] == 'Forecast'].copy()

# --- 2. Time-Series Plot: Historical vs. Forecasted Sales ---
print("--- Generating Time-Series Plot ---")
plt.figure(figsize=(14, 7)) # Set the figure size for better readability
sns.lineplot(x='Date', y='Sales', data=historical_df, label='Historical Sales', marker='o', color='blue')
sns.lineplot(x='Date', y='Sales', data=forecast_df, label='Forecasted Sales', marker='x', linestyle='--', color='red')

# Add a vertical line to mark the separation between historical and forecast
last_historical_date = historical_df['Date'].max()
plt.axvline(x=last_historical_date, color='gray', linestyle=':', label='Forecast Start')

plt.title('Historical vs. Forecasted Monthly Sales', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7) # Add a grid for easier reading
plt.legend(fontsize=10) # Display legend
plt.xticks(rotation=45) # Rotate x-axis labels for better visibility
plt.tight_layout() # Adjust layout to prevent labels from overlapping

# --- CHANGE MADE HERE: Save the plot instead of showing it ---
plot_filename = 'historical_vs_forecast_sales_plot.png'
plt.savefig(plot_filename) # Save the plot to a file
plt.close() # Close the plot to free up memory
print(f"Time-series plot saved as '{plot_filename}'.")

# --- 3. Key Forecast Results and Insights ---
print("\n--- Key Forecast Results ---")

# Calculate total sales for historical and forecast periods
total_historical_sales = historical_df['Sales'].sum()
total_forecast_sales = forecast_df['Sales'].sum()

print(f"Total Historical Sales: ${total_historical_sales:,.2f}")
print(f"Total Forecast Sales: ${total_forecast_sales:,.2f}")

# Calculate average monthly sales for historical and forecast periods
avg_historical_monthly_sales = historical_df['Sales'].mean()
avg_forecast_monthly_sales = forecast_df['Sales'].mean()

print(f"Average Historical Monthly Sales: ${avg_historical_monthly_sales:,.2f}")
print(f"Average Forecast Monthly Sales: ${avg_forecast_monthly_sales:,.2f}")

# Calculate percentage change from historical average to forecast average
if avg_historical_monthly_sales > 0:
    percentage_change = ((avg_forecast_monthly_sales - avg_historical_monthly_sales) / avg_historical_monthly_sales) * 100
    print(f"Percentage Change (Avg. Monthly Sales Historical to Forecast): {percentage_change:,.2f}%")
else:
    print("Cannot calculate percentage change as historical average sales are zero.")

# Identify the highest and lowest sales months in the forecast
highest_forecast_sales_month = forecast_df.loc[forecast_df['Sales'].idxmax()]
lowest_forecast_sales_month = forecast_df.loc[forecast_df['Sales'].idxmin()]

print(f"\nHighest Forecasted Sales Month: {highest_forecast_sales_month['Date'].strftime('%Y-%m')} with ${highest_forecast_sales_month['Sales']:,.2f}")
print(f"Lowest Forecasted Sales Month: {lowest_forecast_sales_month['Date'].strftime('%Y-%m')} with ${lowest_forecast_sales_month['Sales']:,.2f}")

# --- 4. Prepare data for dashboard (similar to previous step, ensuring consistency) ---
# This step is crucial for passing data to your interactive dashboard later.
# We'll save the summarized data to a JSON file.
dashboard_data = {
    'total_historical_sales': round(total_historical_sales, 2),
    'total_forecast_sales': round(total_forecast_sales, 2),
    'avg_historical_monthly_sales': round(avg_historical_monthly_sales, 2),
    'avg_forecast_monthly_sales': round(avg_forecast_monthly_sales, 2),
    'percentage_change_avg_monthly_sales': round(percentage_change, 2) if avg_historical_monthly_sales > 0 else 'N/A',
    'highest_forecast_sales_month': {
        'date': highest_forecast_sales_month['Date'].strftime('%Y-%m-%d'),
        'sales': round(highest_forecast_sales_month['Sales'], 2)
    },
    'lowest_forecast_sales_month': {
        'date': lowest_forecast_sales_month['Date'].strftime('%Y-%m-%d'),
        'sales': round(lowest_forecast_sales_month['Sales'], 2)
    },
    'historical_sales_data': historical_df[['Date', 'Sales']].to_dict(orient='records'),
    'forecast_sales_data': forecast_df[['Date', 'Sales']].to_dict(orient='records')
}

# Convert datetime objects in dictionaries to strings for JSON serialization
for item in dashboard_data['historical_sales_data']:
    item['Date'] = item['Date'].strftime('%Y-%m-%d')
for item in dashboard_data['forecast_sales_data']:
    item['Date'] = item['Date'].strftime('%Y-%m-%d')


with open('sales_forecast_dashboard_insights.json', 'w') as f:
    json.dump(dashboard_data, f, indent=4)

print("\nDetailed forecast insights saved to 'sales_forecast_dashboard_insights.json'.")
