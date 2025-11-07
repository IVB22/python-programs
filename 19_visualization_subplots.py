# Question 19: Data Visualization - Create subplots with different data

import matplotlib.pyplot as plt
import numpy as np

def create_subplot_layout():
    """Create a 2x2 subplot layout with different visualizations"""
    # Generate sample data
    x = np.linspace(0, 10, 100)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Subplot 1: Sine wave
    axes[0, 0].plot(x, np.sin(x), 'b-', linewidth=2)
    axes[0, 0].set_title('Sine Wave')
    axes[0, 0].grid(True)
    
    # Subplot 2: Cosine wave
    axes[0, 1].plot(x, np.cos(x), 'r-', linewidth=2)
    axes[0, 1].set_title('Cosine Wave')
    axes[0, 1].grid(True)
    
    # Subplot 3: Histogram
    data = np.random.randn(1000)
    axes[1, 0].hist(data, bins=30, color='green', alpha=0.7)
    axes[1, 0].set_title('Random Data Histogram')
    
    # Subplot 4: Scatter plot
    x_scatter = np.random.rand(100)
    y_scatter = np.random.rand(100)
    axes[1, 1].scatter(x_scatter, y_scatter, c='purple', alpha=0.5)
    axes[1, 1].set_title('Scatter Plot')
    
    plt.tight_layout()
    plt.savefig('subplots_layout.png')
    print("Subplots saved as 'subplots_layout.png'")

if __name__ == "__main__":
    create_subplot_layout()
