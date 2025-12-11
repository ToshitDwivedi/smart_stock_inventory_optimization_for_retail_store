"""
Sales Prediction Model
----------------------
Predicts units sold based on price and opening stock using Linear Regression.
Author: Toshit Dwivedi
Project: Smart Stock Inventory Optimization
"""

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Configure paths (run from project root)
DATA_PATH = "dataset/updated_dataset.csv"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_and_prepare_data():
    """Load and prepare data for modeling."""
    print("\n" + "=" * 60)
    print("LOADING AND PREPARING DATA")
    print("=" * 60)
    
    df = pd.read_csv(DATA_PATH)
    print(f"✓ Data loaded: {len(df)} records")
    
    # Features and target
    X = df[['Price', 'Opening_Stock']]
    y = df['Units_Sold']
    
    print(f"✓ Features: {list(X.columns)}")
    print(f"✓ Target: Units_Sold")
    
    return X, y, df


def train_model(X, y):
    """Train linear regression model."""
    print("\n" + "=" * 60)
    print("TRAINING MODEL")
    print("=" * 60)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Training set: {len(X_train)} samples")
    print(f"Testing set: {len(X_test)} samples")
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    print(f"\n✓ Model trained successfully")
    print(f"\nModel Coefficients:")
    print(f"  Price coefficient: {model.coef_[0]:.4f}")
    print(f"  Stock coefficient: {model.coef_[1]:.4f}")
    print(f"  Intercept: {model.intercept_:.4f}")
    
    return model, X_train, X_test, y_train, y_test


def evaluate_model(model, X_train, X_test, y_train, y_test):
    """Evaluate model performance."""
    print("\n" + "=" * 60)
    print("MODEL EVALUATION")
    print("=" * 60)
    
    # Predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    # Training metrics
    train_r2 = r2_score(y_train, y_train_pred)
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    train_mae = mean_absolute_error(y_train, y_train_pred)
    
    # Testing metrics
    test_r2 = r2_score(y_test, y_test_pred)
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
    test_mae = mean_absolute_error(y_test, y_test_pred)
    
    print("\nTraining Performance:")
    print(f"  R² Score: {train_r2:.4f}")
    print(f"  RMSE: {train_rmse:.2f}")
    print(f"  MAE: {train_mae:.2f}")
    
    print("\nTesting Performance:")
    print(f"  R² Score: {test_r2:.4f}")
    print(f"  RMSE: {test_rmse:.2f}")
    print(f"  MAE: {test_mae:.2f}")
    
    # Model interpretation
    print("\nModel Interpretation:")
    if model.coef_[0] < 0:
        print(f"  → Price has negative impact: Each $1 increase reduces sales by {abs(model.coef_[0]):.2f} units")
    else:
        print(f"  → Price has positive impact: Each $1 increase adds {model.coef_[0]:.2f} units sold")
    
    print(f"  → Stock impact: Each additional stock unit increases sales by {model.coef_[1]:.4f} units")
    
    return y_test_pred, test_r2, test_rmse


def visualize_predictions(y_test, y_test_pred):
    """Create visualization of predictions."""
    print("\n" + "=" * 60)
    print("GENERATING VISUALIZATIONS")
    print("=" * 60)
    
    # Actual vs Predicted
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_test_pred, alpha=0.6, edgecolors='k')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual Units Sold', fontsize=12)
    plt.ylabel('Predicted Units Sold', fontsize=12)
    plt.title('Actual vs Predicted Units Sold', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    output_path = os.path.join(OUTPUT_DIR, "prediction_scatter.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✓ Scatter plot saved: {output_path}")
    plt.close()
    
    # Residuals plot
    residuals = y_test - y_test_pred
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test_pred, residuals, alpha=0.6, edgecolors='k')
    plt.axhline(y=0, color='r', linestyle='--', lw=2)
    plt.xlabel('Predicted Units Sold', fontsize=12)
    plt.ylabel('Residuals', fontsize=12)
    plt.title('Residual Plot', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    output_path = os.path.join(OUTPUT_DIR, "residuals_plot.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✓ Residuals plot saved: {output_path}")
    plt.close()


def make_predictions(model):
    """Make predictions for new scenarios."""
    print("\n" + "=" * 60)
    print("MAKING PREDICTIONS")
    print("=" * 60)
    
    # Scenario 1
    new_data_1 = pd.DataFrame({'Price': [50], 'Opening_Stock': [150]})
    predicted_1 = model.predict(new_data_1)[0]
    print(f"\nScenario 1:")
    print(f"  Price: $50, Opening Stock: 150")
    print(f"  → Predicted Units Sold: {np.round(predicted_1, 0):.0f}")
    
    # Scenario 2
    new_data_2 = pd.DataFrame({'Price': [75], 'Opening_Stock': [200]})
    predicted_2 = model.predict(new_data_2)[0]
    print(f"\nScenario 2:")
    print(f"  Price: $75, Opening Stock: 200")
    print(f"  → Predicted Units Sold: {np.round(predicted_2, 0):.0f}")
    
    # Scenario 3
    new_data_3 = pd.DataFrame({'Price': [30], 'Opening_Stock': [250]})
    predicted_3 = model.predict(new_data_3)[0]
    print(f"\nScenario 3:")
    print(f"  Price: $30, Opening Stock: 250")
    print(f"  → Predicted Units Sold: {np.round(predicted_3, 0):.0f}")
    
    # Save predictions
    scenarios = pd.DataFrame({
        'Scenario': ['Scenario 1', 'Scenario 2', 'Scenario 3'],
        'Price': [50, 75, 30],
        'Opening_Stock': [150, 200, 250],
        'Predicted_Units_Sold': [predicted_1, predicted_2, predicted_3]
    })
    
    output_path = os.path.join(OUTPUT_DIR, "prediction_scenarios.csv")
    scenarios.to_csv(output_path, index=False)
    print(f"\n✓ Scenarios saved: {output_path}")


def save_model_summary(model, test_r2, test_rmse):
    """Save model summary to file."""
    output_path = os.path.join(OUTPUT_DIR, "model_summary.txt")
    
    with open(output_path, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write(" " * 20 + "MODEL SUMMARY\n")
        f.write(" " * 15 + "Sales Prediction Model\n")
        f.write("=" * 70 + "\n\n")
        
        f.write("MODEL TYPE: Linear Regression\n")
        f.write("TARGET: Units_Sold\n")
        f.write("FEATURES: Price, Opening_Stock\n\n")
        
        f.write("MODEL COEFFICIENTS:\n")
        f.write(f"  Price: {model.coef_[0]:.6f}\n")
        f.write(f"  Opening_Stock: {model.coef_[1]:.6f}\n")
        f.write(f"  Intercept: {model.intercept_:.6f}\n\n")
        
        f.write("PERFORMANCE METRICS:\n")
        f.write(f"  R² Score: {test_r2:.4f}\n")
        f.write(f"  RMSE: {test_rmse:.2f}\n\n")
        
        f.write("EQUATION:\n")
        f.write(f"  Units_Sold = {model.intercept_:.2f} + ({model.coef_[0]:.4f} × Price) + ({model.coef_[1]:.4f} × Opening_Stock)\n")
        f.write("\n" + "=" * 70 + "\n")
    
    print(f"✓ Model summary saved: {output_path}")


def main():
    """Main execution function."""
    print("\n" + "=" * 70)
    print(" " * 20 + "SALES PREDICTION MODEL")
    print("=" * 70)
    
    # Load data
    X, y, df = load_and_prepare_data()
    
    # Train model
    model, X_train, X_test, y_train, y_test = train_model(X, y)
    
    # Evaluate model
    y_test_pred, test_r2, test_rmse = evaluate_model(model, X_train, X_test, y_train, y_test)
    
    # Visualize
    visualize_predictions(y_test, y_test_pred)
    
    # Make predictions
    make_predictions(model)
    
    # Save summary
    save_model_summary(model, test_r2, test_rmse)
    
    print("\n" + "=" * 70)
    print(" " * 25 + "MODEL COMPLETE!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
