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
│   ├── sales_data.csv           # Original sales data
│   └── updated_dataset.csv      # Processed data with additional features
├── numpy/
│   ├── mathfunc.py             # Statistical operations using NumPy
│   ├── null_n.py               # Null value handling with NumPy
│   └── numpy1.py               # Basic NumPy operations
├── pandas/
│   ├── adding_newc.py          # Adding calculated columns
│   ├── filtering.py            # Data filtering operations
│   ├── groupby.py              # Aggregation using groupby
│   ├── merging.py              # Data merging operations
│   ├── null_values.py          # Handling missing values
│   └── sorting_Agg.py          # Sorting and aggregation
├── preprocessing/
│   └── preprocess.py           # Data preprocessing pipeline
├── regression/
│   ├── regression.ipynb        # Interactive regression analysis
│   ├── reggression1.py         # Units sold prediction
│   ├── regression2.py          # Sales value prediction
│   └── regression3.py          # Product-specific predictions
├── streamlit/
│   └── app.py                  # Interactive dashboard
├── Visualization/
│   ├── Matplotlib/             # Static visualizations
│   │   ├── bar_chart.py
│   │   ├── line_chart.py
│   │   └── scatter.py
│   └── plotly/                 # Interactive visualizations
│       ├── histogram.py
│       ├── pie_chart.py
│       └── scatter.py
└── output/                     # Generated outputs
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
- **Matplotlib**: Bar charts, line charts, scatter plots
- **Plotly**: Interactive histograms, pie charts, scatter plots
- **Streamlit Dashboard**: Interactive web-based analytics dashboard

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

### Run Data Analysis Scripts
```bash
# NumPy operations
python numpy/mathfunc.py

# Pandas operations
python pandas/filtering.py

# Preprocessing
python preprocessing/preprocess.py
```

### Run Regression Models
```bash
# Basic prediction model
python regression/reggression1.py

# Monthly sales prediction
python regression/regression2.py

# Product-specific prediction
python regression/regression3.py
```

### Generate Visualizations
```bash
# Matplotlib visualizations
python Visualization/Matplotlib/bar_chart.py

# Plotly visualizations
python Visualization/plotly/histogram.py
```

### Launch Interactive Dashboard
```bash
streamlit run streamlit/app.py
```

## 📈 Sample Outputs

The project provides:
- Statistical summaries of sales data
- Regression models with prediction accuracy
- Visual charts showing sales patterns
- Interactive dashboard for exploring data
- Stockout risk assessments

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
