# Question 18: Data Visualization - Demonstrate basic plot types

import matplotlib.pyplot as plt
import numpy as np

def create_basic_plots():
    """Create and display basic plot types: line, bar, scatter"""
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    # Line plot
    axes[0].plot(x, y, 'b-', linewidth=2)
    axes[0].set_title('Line Plot')
    axes[0].set_xlabel('X')
    axes[0].set_ylabel('Y')
    axes[0].grid(True)
    
    # Bar plot
    categories = ['A', 'B', 'C', 'D']
    values = [25, 40, 30, 55]
    axes[1].bar(categories, values, color=['red', 'green', 'blue', 'orange'])
    axes[1].set_title('Bar Plot')
    axes[1].set_ylabel('Values')
    
    # Scatter plot
    x_scatter = np.random.rand(50) * 10
    y_scatter = np.random.rand(50) * 10
    axes[2].scatter(x_scatter, y_scatter, c='purple', alpha=0.6)
    axes[2].set_title('Scatter Plot')
    axes[2].set_xlabel('X')
    axes[2].set_ylabel('Y')
    
    plt.tight_layout()
    plt.savefig('basic_plots.png')
    print("Plots saved as 'basic_plots.png'")

if __name__ == "__main__":
    create_basic_plots()
