# Question 21: Data Visualization - Create a 3D scatter plot

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def create_3d_scatter_plot():
    """Create and display a 3D scatter plot"""
    # Generate random 3D data
    np.random.seed(42)
    n_points = 200
    
    x = np.random.randn(n_points)
    y = np.random.randn(n_points)
    z = np.random.randn(n_points)
    colors = np.random.rand(n_points)
    sizes = 100 * np.random.rand(n_points)
    
    # Create 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    scatter = ax.scatter(x, y, z, c=colors, s=sizes, alpha=0.6, cmap='viridis')
    
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Scatter Plot')
    
    # Add colorbar
    plt.colorbar(scatter, ax=ax, shrink=0.5)
    
    plt.savefig('3d_scatter_plot.png')
    print("3D scatter plot saved as '3d_scatter_plot.png'")

if __name__ == "__main__":
    create_3d_scatter_plot()
