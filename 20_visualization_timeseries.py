# Question 20: Data Visualization - Create a time series plot

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def create_timeseries_plot():
    """Create and display a time series plot"""
    # Generate time series data
    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(365)]
    
    # Generate sample data with trend and seasonality
    trend = np.linspace(100, 200, 365)
    seasonal = 20 * np.sin(np.linspace(0, 4*np.pi, 365))
    noise = np.random.randn(365) * 5
    values = trend + seasonal + noise
    
    # Create DataFrame
    df = pd.DataFrame({'Date': dates, 'Value': values})
    
    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Value'], linewidth=1.5)
    plt.title('Time Series Plot: Daily Values for 2024')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('timeseries_plot.png')
    print("Time series plot saved as 'timeseries_plot.png'")

if __name__ == "__main__":
    create_timeseries_plot()
