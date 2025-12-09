# 🏪 Smart Stock Inventory Optimization for Retail Stores

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)](https://streamlit.io/)

> **A comprehensive data science project for optimizing retail inventory management using Python, Machine Learning, and Interactive Dashboards**

**Developed by:** Toshit Dwivedi  
**Program:** Infosys Springboard Internship 2024-2025

---

## 📊 Project Overview

This project demonstrates end-to-end data science workflow for retail inventory optimization, including:
- **Data Preprocessing & Cleaning**
- **Exploratory Data Analysis (EDA)**
- **Statistical Analysis with NumPy**
- **Data Manipulation with Pandas**
- **Machine Learning for Sales Prediction**
- **Interactive Visualizations**
- **Real-time Dashboard with Streamlit**

### 🎯 Business Objectives

1. **Optimize Stock Levels** - Prevent overstocking and stockouts
2. **Forecast Sales** - Predict future demand patterns
3. **Identify Risks** - Flag products with high stockout probability
4. **Maximize Revenue** - Data-driven pricing and inventory decisions
5. **Visualize Insights** - Interactive dashboards for stakeholders

---

## 🗂️ Project Structure

```
Smart_Stock_Inventory_Optimization/
│
├── dataset/                          # Data files
│   ├── sales_data.csv               # Original raw data
│   └── updated_dataset.csv          # Processed data with features
│
├── numpy/                            # NumPy analysis modules
│   ├── statistical_analysis.py      # Comprehensive statistical operations
│   ├── array_operations.py          # Array transformations & operations
│   └── missing_data_handler.py      # Missing value handling demonstrations
│
├── pandas/                           # Pandas data manipulation
│   ├── data_manipulation.py         # Filtering, sorting, aggregation
│   └── advanced_analysis.py         # Pivot tables, merging, time series
│
├── preprocessing/                    # Data preprocessing pipeline
│   └── preprocess.py                # Complete data cleaning & feature engineering
│
├── regression/                       # Machine learning models
│   ├── sales_prediction_model.py    # Predict units sold (Price, Stock)
│   ├── monthly_forecast_model.py    # Monthly sales forecasting
│   └── regression.ipynb            # Interactive analysis notebook
│
├── visualization/                    # Visualization modules
│   └── create_all_visualizations.py # Generate all charts & plots
│
├── streamlit/                        # Interactive dashboard
│   └── app.py                       # Streamlit web application
│
├── output/                           # Generated outputs
│   ├── visualizations/              # Charts and plots
│   │   ├── matplotlib/             # Static visualizations
│   │   └── plotly/                 # Interactive visualizations
│   ├── *.csv                        # Analysis results
│   ├── *.txt                        # Reports and summaries
│   └── *.png                        # Model visualizations
│
└── README.md                         # Project documentation

```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/ToshitDwivedi/smart_stock_inventory_optimization_for_retail_store.git
cd smart_stock_inventory_optimization_for_retail_store
```

2. **Install dependencies**
```bash
pip install pandas numpy matplotlib plotly scikit-learn streamlit seaborn
```

### 📦 Required Packages

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
plotly>=5.14.0
scikit-learn>=1.3.0
streamlit>=1.28.0
seaborn>=0.12.0
```

---

## 💻 Usage Guide

### 1. Data Preprocessing

Process raw data and create features:

```bash
cd preprocessing
python preprocess.py
```

### 2. NumPy Statistical Analysis

```bash
cd numpy
python statistical_analysis.py
python array_operations.py
python missing_data_handler.py
```

### 3. Pandas Data Manipulation

```bash
cd pandas
python data_manipulation.py
python advanced_analysis.py
```

### 4. Machine Learning Models

```bash
cd regression
python sales_prediction_model.py
python monthly_forecast_model.py
```

### 5. Create Visualizations

```bash
cd visualization
python create_all_visualizations.py
```

### 6. Launch Interactive Dashboard

```bash
cd streamlit
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`

---

## 📈 Features & Capabilities

### Data Analysis

- Statistical Operations (Mean, Median, Std Dev, Correlations)
- Data Transformations (Filtering, Grouping, Pivoting, Merging)
- Time Series Analysis (Trends, Seasonality, Growth Rates)
- Missing Data Handling (Multiple Imputation Techniques)

### Machine Learning

- Linear Regression Models for Sales Prediction
- Monthly Sales Forecasting
- Model Evaluation (R², RMSE, MAE)
- Visualization (Actual vs Predicted, Residuals)

### Visualizations

**Static (Matplotlib):** Bar charts, Line charts, Scatter plots, Histograms, Box plots

**Interactive (Plotly):** 3D scatter, Heatmaps, Treemaps, Sunburst charts, Pie charts

### Dashboard Features

- Real-time KPIs (Sales, Units, Efficiency)
- Interactive Filters (Product, Month)
- Multiple Analysis Tabs
- Risk Analysis & Stockout Warnings
- Responsive Design

---

## 📊 Dataset

### Features

| Column | Description |
|--------|-------------|
| Product_ID | Unique product identifier |
| Product_Name | Name of product |
| Units_Sold | Number of units sold |
| Price | Product price ($) |
| Month | Sales month |
| Opening_Stock | Initial stock quantity |
| Total_Sales_Value | Revenue (Units × Price) |
| Stock_Efficiency | Turnover rate (%) |

### Statistics

- **104 Records** across 17 products
- **6 Months** of data (Jan-Jun)
- **$509K+** Total Sales Value
- **9,000+** Units Sold

---

## 🎯 Key Insights

1. **Top Products**: Rice, Wheat, Biscuits generate highest revenue
2. **Sales Trends**: Stable across months with minor variations
3. **Stock Efficiency**: 58% average turnover rate
4. **Risk Products**: 15-20% show stockout risk (>70% utilization)

---

## 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core language |
| NumPy | Numerical computing |
| Pandas | Data manipulation |
| Matplotlib | Static visualization |
| Plotly | Interactive charts |
| Scikit-learn | Machine learning |
| Streamlit | Web dashboard |

---

## 📂 Output Files

### Reports
- `preprocessing_report.txt` - Data cleaning summary
- `statistical_summary.txt` - NumPy analysis
- `model_summary.txt` - ML model details
- `sales_forecast_report.txt` - Forecast analysis

### Data Exports
- `transformed_sales_data.csv`
- `product_sales_summary.csv`
- `monthly_sales_summary.csv`
- `category_analysis.csv`

### Visualizations
- Matplotlib PNG files (High-resolution charts)
- Plotly HTML files (Interactive visualizations)

---

## 🔄 Workflow

```
Raw Data → Preprocessing → Enhanced Data
    ↓                           ↓
    ├── NumPy Analysis
    ├── Pandas Manipulation
    ├── ML Models
    └── Visualizations
            ↓
    Streamlit Dashboard
```

---

## 🎓 Learning Outcomes

- Data Science Fundamentals
- Python Libraries (NumPy, Pandas, Scikit-learn)
- Machine Learning (Regression, Forecasting)
- Data Visualization (Matplotlib, Plotly)
- Dashboard Development (Streamlit)
- Software Engineering Best Practices

---

## 🚦 Future Enhancements

- [ ] Advanced ML models (Random Forest, XGBoost)
- [ ] ARIMA/Prophet forecasting
- [ ] Product recommendation system
- [ ] ABC analysis
- [ ] Automated alerts
- [ ] Cloud deployment

---

## 👨‍💻 Author

**Toshit Dwivedi**

- 🐙 GitHub: [@ToshitDwivedi](https://github.com/ToshitDwivedi)
- 📧 Email: [Your Email]
- 💼 LinkedIn: [Your Profile]

---

## 🙏 Acknowledgments

- **Infosys Springboard** - Internship opportunity
- **Open Source Community** - Amazing libraries and tools

---

## 📄 License

This project is open source and available under the MIT License.

---

<div align="center">

**Made with ❤️ for Inventory Optimization**

*Empowering retail businesses with data-driven decisions*

⭐ Star this repo if you found it helpful!

</div>
