# Smart Stock Inventory Optimization For Retail Stores

This project is developed as part of the **Infosys Springboard Internship**. It demonstrates data analysis, machine learning, and visualization techniques to optimize inventory management for retail stores.

## 📋 Project Overview

This project analyzes retail sales data to help optimize inventory management through:
- Statistical analysis of sales patterns
- Predictive modeling for stock requirements
- Interactive visualizations for data insights
- Stockout risk assessment

## 🗂️ Project Structure

```
├── dataset/
│   ├── sales_data.csv                    # Original sales data
│   └── updated_dataset.csv               # Processed data with features
├── numpy/
│   ├── statistical_analysis.py           # Comprehensive statistical operations
│   ├── array_operations.py               # Array transformations & operations
│   └── missing_data_handler.py           # Missing value handling
├── pandas/
│   ├── data_manipulation.py              # Filtering, sorting, aggregation
│   └── advanced_analysis.py              # Pivot tables, merging, time series
├── preprocessing/
│   └── preprocess.py                     # Complete ETL pipeline
├── regression/
│   ├── sales_prediction_model.py         # Predict units sold (Price, Stock)
│   ├── monthly_forecast_model.py         # Monthly sales forecasting
│   └── regression.ipynb                  # Interactive analysis notebook
├── visualization/
│   └── create_all_visualizations.py      # Generate all charts (Matplotlib + Plotly)
├── streamlit/
│   └── app.py                            # Interactive web dashboard
├── output/
│   ├── visualizations/
│   │   ├── matplotlib/                   # 5 static PNG charts
│   │   └── plotly/                       # 8 interactive HTML charts
│   ├── *.csv                             # Analysis results
│   ├── *.txt                             # Reports and summaries
│   └── *.png                             # Model visualizations
├── .gitignore                            # Git ignore file
├── requirements.txt                      # Python dependencies
└── PROJECT_SUMMARY.md                    # Detailed project documentation
```

## 🚀 Features

### Data Analysis
- **NumPy Operations**: Statistical calculations, array operations
- **Pandas Operations**: Data manipulation, filtering, grouping, merging
- **Data Preprocessing**: Cleaning, feature engineering, null value handling

### Machine Learning
- **Linear Regression Models**: Predict units sold based on stock and pricing
- **Sales Forecasting**: Monthly sales predictions
- **Product-Specific Models**: Individual product demand forecasting

### Visualizations
- **Matplotlib**: 5 static visualizations (bar charts, line charts, scatter plots, histograms, box plots)
- **Plotly**: 8 interactive visualizations (bar, line, 3D scatter, sunburst, treemap, heatmap, pie chart, dashboard)
- **Streamlit Dashboard**: Real-time interactive web-based analytics with 5 tabs

### Key Insights
- Identify best-selling products
- Track sales trends over time
- Analyze price vs demand relationships
- Assess stockout risks
- Predict future inventory requirements

## 📊 Dataset

The dataset contains retail sales information with the following features:
- `Product_ID`: Unique product identifier
- `Product_Name`: Name of the product
- `Units_Sold`: Number of units sold
- `Price`: Product price
- `Month`: Sales month
- `Opening_Stock`: Initial stock quantity
- `Total_Sales_Value`: Calculated total sales revenue
- `Month_Num`: Numeric month representation

## 🛠️ Technologies Used

- **Python 3.x**
- **Libraries**:
  - NumPy - Numerical computing
  - Pandas - Data manipulation
  - Matplotlib - Static visualizations
  - Plotly - Interactive visualizations
  - Scikit-learn - Machine learning
  - Streamlit - Web dashboard

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/ToshitDwivedi/smart_stock_inventory_optimization_for_retail_store.git
cd smart_stock_inventory_optimization_for_retail_store
```

2. Install required packages:
```bash
pip install pandas numpy matplotlib plotly scikit-learn streamlit
```

## 💻 Usage

### 1. Data Preprocessing
```bash
# Run complete ETL pipeline
python preprocessing/preprocess.py
```

### 2. Run Analysis Scripts
```bash
# NumPy statistical analysis
python numpy/statistical_analysis.py
python numpy/array_operations.py

# Pandas data manipulation
python pandas/data_manipulation.py
python pandas/advanced_analysis.py
```

### 3. Run Machine Learning Models
```bash
# Sales prediction model
python regression/sales_prediction_model.py

# Monthly forecast model
python regression/monthly_forecast_model.py
```

### 4. Generate All Visualizations
```bash
# Creates 13 charts (5 Matplotlib PNGs + 8 Plotly HTMLs)
python visualization/create_all_visualizations.py
```

### 5. Launch Interactive Dashboard
```bash
streamlit run streamlit/app.py
```

**Note:** The repository shows 99.8% HTML because Plotly generates interactive HTML files for visualizations. The actual codebase is Python.

## 📈 Sample Outputs

The project generates:
- **Statistical Reports**: Comprehensive sales analysis with mean, median, std dev
- **Regression Models**: R² scores, RMSE, MAE metrics with prediction accuracy
- **13 Visualizations**: 5 static PNGs + 8 interactive HTML charts
- **Interactive Dashboard**: Real-time analytics with KPIs, filters, and insights
- **CSV Reports**: Filtered data, pivot tables, aggregations, time series analysis
- **Risk Assessments**: Stockout probability and inventory optimization recommendations

## 🎯 Use Cases

- **Inventory Optimization**: Determine optimal stock levels
- **Demand Forecasting**: Predict future product demand
- **Sales Analysis**: Identify trends and patterns
- **Risk Management**: Identify products at risk of stockout
- **Business Intelligence**: Data-driven decision making

## 👨‍💻 Author

**Toshit Dwivedi**
- GitHub: [@ToshitDwivedi](https://github.com/ToshitDwivedi)

## 🙏 Acknowledgments

This project was developed as part of the **Infosys Springboard Internship Program**.

## 📄 License

This project is open source and available for educational purposes.
