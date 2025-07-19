Automated Sales Forecasting Dashboard
Project Overview
This project demonstrates an end-to-end data analysis and visualization pipeline for sales forecasting. Leveraging historical sales data, a predictive model is used to generate future sales projections. These projections are then integrated into an interactive and insightful dashboard, designed to help business managers and analytical teams understand past performance, anticipate future revenue, and make data-driven strategic decisions.

The dashboard provides a clear, at-a-glance view of sales trends and key forecast metrics, making complex data accessible for actionable insights.

Deployment
The live dashboard can be viewed here:
http://praveenchalla.me/automated-sales-forecasting/

Data Source
The project utilizes past year sales data as its foundation. This historical data serves as the input for the forecasting model.

Methodology
Data Generation (Forecasting):

Historical sales data was fed into a predictive model (developed within a GitHub Codespace environment).

The model processed this historical data to generate future sales forecasts.

The output, combining both historical and forecasted sales, was provided in a CSV format (forecast_output.csv).

Data Cleaning & Preprocessing (Python):

The raw forecast_output.csv file underwent a rigorous cleaning and preprocessing stage using Python.

Key steps included:

Loading and initial inspection of the dataset.

Converting the 'Date' column to datetime objects for time-series analysis.

Checking for and handling (though none were found in this specific dataset) duplicate entries.

Checking for and demonstrating how to handle missing values.

Feature Engineering: Extracting useful time-based features such as Year, Month, Day, Day of Week, and Week of Year to enable richer analysis.

Segmenting the data into distinct 'Historical' and 'Forecast' datasets.

Results & Insights Derivation (Python):

Following preprocessing, key analytical results and insights were derived from both the historical and forecasted datasets.

These insights were structured and saved into a JSON file (sales_forecast_dashboard_insights.json), ready for consumption by the web dashboard.

Dashboard Development (HTML, CSS, JavaScript):

An interactive web dashboard was built using HTML for structure, Tailwind CSS for modern styling and responsiveness, and JavaScript to dynamically load and display the insights.

The dashboard directly embeds the JSON data, ensuring reliable loading without external file fetching issues.

The static sales forecast plot, generated during the Python analysis phase, is integrated directly into the dashboard for visual representation.

Key Results & Insights Provided by the Dashboard
The dashboard provides critical metrics and visualizations for strategic decision-making:

Total Historical Sales: The aggregate revenue generated in the past.

Total Forecast Sales: The projected total revenue for the upcoming period.

Average Monthly Sales Change: A percentage indicating the anticipated growth or decline in average monthly sales from the historical period to the forecast period.

Highest Forecast Month: Identifies the month with the highest projected sales, crucial for anticipating peak demand.

Lowest Forecast Month: Highlights the month with the lowest projected sales, useful for planning promotions or resource allocation during slower periods.

Forecast Period: Clearly defines the timeline covered by the sales predictions.

Visual Sales Trend: A clear plot illustrating both historical sales performance and future sales forecasts, allowing for easy identification of trends and expected shifts.

Strategic Implications & Recommendations: Actionable insights derived from the forecast, guiding business managers on potential operational, inventory, and marketing strategies.

Technologies Used
Python: For data cleaning, preprocessing, and deriving key insights.

pandas: For data manipulation and analysis.

matplotlib & seaborn: (Used for generating the static plot).

HTML: For the dashboard's structure.

CSS (Tailwind CSS): For responsive and modern styling.

JavaScript: For dynamic content loading and populating insights.

How to Run/View Locally
Clone the Repository:

git clone <your-repository-url>
cd automated-sales-forecasting

Ensure Files are Present: Make sure the following files are in the root directory:

index.html

sales_forecast_dashboard_insights.json

historical_vs_forecast_sales_plot.png

Open with a Live Server:

Install a local web server extension (e.g., "Live Server" for VS Code).

Right-click on index.html and select "Open with Live Server" or "Go Live".

Alternatively, simply open index.html in your web browser.
