# Automated Sales Forecasting Dashboard

## Project Overview

This project demonstrates an end-to-end data analysis and visualization pipeline focused on sales forecasting. It leverages historical sales data to train a predictive model, which then generates future sales projections. These projections are integrated into an interactive and insightful dashboard, specifically designed to empower business managers and analytical teams. The goal is to provide a clear understanding of past performance, anticipate future revenue, and facilitate data-driven strategic decisions across areas like inventory management, marketing campaigns, and resource allocation.

The dashboard offers a concise, at-a-glance view of critical sales trends and key forecast metrics, transforming complex data into accessible and actionable insights.

## Live Deployment

The interactive dashboard is publicly deployed and can be viewed live at:
http://praveenchalla.me/automated-sales-forecasting/

## Data Source

The foundation of this project is **past year sales data**. This historical dataset serves as the essential input for the predictive forecasting model.

## Methodology: An End-to-End Pipeline

The project follows a structured methodology, encompassing data generation, rigorous preprocessing, insightful analysis, and dynamic visualization:

### 1. Data Generation (Forecasting)

* **Model Application:** Historical sales data was fed into a predictive model, which was developed and iterated upon within a GitHub Codespace environment.

* **Future Projections:** The model processed the historical trends and patterns to generate comprehensive **future sales forecasts**.

* **Output Format:** The combined dataset, including both historical and newly forecasted sales, was outputted in a **CSV format** (`forecast_output.csv`) for subsequent stages.

### 2. Data Cleaning & Preprocessing (Python)

The raw `forecast_output.csv` underwent a meticulous cleaning and preprocessing phase using **Python**, ensuring data quality and readiness for analysis:

* **Data Loading & Initial Inspection:** The dataset was loaded, and its structure, data types, and initial statistics were thoroughly examined.

* **Type Conversion:** The 'Date' column was converted to appropriate datetime objects, crucial for accurate time-series analysis.

* **Duplicate Handling:** Although no exact duplicates were found in this dataset, the process included checks for and demonstrated the standard approach to removing redundant entries.

* **Missing Value Management:** Comprehensive checks for missing values were performed, and the methodology for imputation or removal was established (though not required for this clean dataset).

* **Feature Engineering:** New, highly relevant time-based features were extracted from the 'Date' column, including:

    * `Year`

    * `Month`

    * `Day`

    * `Day of Week`

    * `Week of Year`
        These features enable deeper analysis into seasonal and temporal patterns.

* **Data Segmentation:** The dataset was logically segmented into distinct 'Historical' and 'Forecast' subsets based on the 'Type' column, facilitating separate and combined analysis.

### 3. Results & Insights Derivation (Python)

Following the preprocessing, key analytical results and actionable insights were extracted from both the historical and forecasted datasets. These insights were then structured and saved into a **JSON file** (`sales_forecast_dashboard_insights.json`), serving as the data source for the web dashboard.

### 4. Dashboard Development (HTML, CSS, JavaScript)

An intuitive and interactive web dashboard was constructed to visualize the derived insights:

* **Structure (HTML):** The dashboard's layout and content were built using clean and semantic HTML.

* **Styling (Tailwind CSS):** Tailwind CSS was utilized to apply modern, responsive, and professional styling, ensuring optimal viewing across various devices.

* **Interactivity (JavaScript):** JavaScript was employed to dynamically load the processed data from the embedded JSON, populate the key metrics, and render the sales trend visualization.

* **Data Integration:** The `sales_forecast_dashboard_insights.json` data is directly embedded within the HTML, ensuring reliable and immediate loading without external file fetching issues, especially in sandboxed environments.

* **Visualization:** The static sales forecast plot, generated during the Python analysis phase, is seamlessly integrated into the dashboard, providing a clear visual representation of sales performance and future projections.

## Key Results & Actionable Insights

<img width="1400" height="700" alt="historical_vs_forecast_sales_plot" src="https://github.com/user-attachments/assets/778f3276-2ae8-4cf1-bf95-67f1ec2c1cef" />


The dashboard delivers critical metrics and visualizations, empowering stakeholders with a clear understanding of sales dynamics:

* **Total Historical Sales:** The aggregate revenue generated over the past period, serving as a foundational benchmark.

* **Total Forecast Sales:** The projected total revenue for the upcoming period, enabling forward-looking financial planning.

* **Average Monthly Sales Change:** A quantifiable percentage indicating the anticipated growth or decline in average monthly sales from the historical period to the forecast period, highlighting overall trajectory.

* **Highest Forecast Month:** Identifies the month with the highest projected sales, crucial for anticipating peak demand, optimizing inventory, and scaling operations.

* **Lowest Forecast Month:** Pinpoints the month with the lowest projected sales, useful for planning targeted promotions, managing inventory reductions, or allocating resources during slower periods.

* **Forecast Period:** Clearly defines the precise timeline covered by the sales predictions, ensuring contextual understanding.

* **Visual Sales Trend:** A comprehensive plot illustrating both historical sales performance and future sales forecasts on a single timeline, allowing for easy identification of trends, seasonal patterns, and expected shifts.

* **Strategic Implications & Recommendations:** Actionable insights derived directly from the forecast, guiding business managers on potential operational adjustments, inventory strategies, marketing campaign timing, and resource allocation to capitalize on opportunities or mitigate risks.

## Technologies Used

* **Python:**
    * `pandas`: Essential for efficient data manipulation, cleaning, and transformation.
    * `matplotlib` & `seaborn`: Utilized for generating high-quality static data visualizations.

* **HTML:** The core structural language for the web dashboard.

* **CSS (Tailwind CSS):** A utility-first CSS framework for rapid and responsive UI development.

* **JavaScript:** For dynamic content rendering, data parsing, and interactive dashboard features.

## How to Run/View Locally

To set up and view this project on your local machine:

1.  **Clone the Repository:**
    Open your terminal or command prompt and execute:

    ```bash
    git clone <your-repository-url>
    cd automated-sales-forecasting
    ```

    (Replace `<your-repository-url>` with the actual URL of your GitHub repository.)

2.  **Ensure Files are Present:**
    Verify that the following essential project files are located in the root directory of the cloned repository:

    * `index.html` (the main dashboard file)

    * `sales_forecast_dashboard_insights.json` (the processed data for the dashboard)

    * `historical_vs_forecast_sales_plot.png` (the static image of the sales trend)

3.  **Open with a Live Server:**
    For the best local viewing experience, it is highly recommended to use a local web server:

    * **VS Code Extension:** If you use VS Code, install the "Live Server" extension by Ritwick Dey. Then, right-click on `index.html` in your file explorer and select "Open with Live Server" or click the "Go Live" button in the VS Code status bar.

    * **Direct Browser Open (Limited):** Alternatively, you can simply double-click the `index.html` file in your file explorer. However, this method might have limitations (e.g., security restrictions preventing local file access for JavaScript) compared to using a dedicated web server.
