# Smart Stock Inventory Optimization

This is my project to analyze retail store sales.

## How to Run

1.  **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run Preprocessing:**
    ```bash
    python preprocessing/preprocess.py
    ```

3.  **Run Analysis:**
    ```bash
    python numpy/array_operations.py
    python numpy/missing_data_handler.py
    python pandas/data_manipulation.py
    python pandas/advanced_analysis.py
    ```

4.  **Run Models:**
    ```bash
    python regression/sales_prediction_model.py
    python regression/monthly_forecast_model.py
    ```

5.  **Create Graphs:**
    ```bash
    python visualization/create_all_visualizations.py
    ```

6.  **Run Dashboard:**
    ```bash
    streamlit run streamlit/app.py
    ```

## Project Structure

*   `dataset/`: Contains the data.
*   `numpy/`: Scripts for math operations.
*   `pandas/`: Scripts for data sorting and cleaning.
*   `regression/`: Machine learning models for prediction.
*   `visualization/`: Code to make charts.
*   `output/`: Where all the results and graphs are saved.

## Output

Check the `output` folder for CSV files, Reports, and PNG images of the charts.
