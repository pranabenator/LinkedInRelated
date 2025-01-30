import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ipywidgets import interactive
from matplotlib.widgets import Button

def plot_bloch_sphere():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Draw the sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    
    ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b', alpha=0.1, linestyle='dashed', linewidth=0.5)
    
    # Equator and the prime meridian
    ax.plot(np.sin(u), np.cos(u), 0, color='k', linestyle=(0, (5, 10)))
    ax.plot([0]*50, np.sin(u[:50]), np.cos(u[:50]), color='k', linestyle=(0, (5, 10)))

    # Axes labels
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    
    return ax, fig

def on_click(event, ax, fig):
    if event.inaxes != ax:
        return
    
    x, y, z = event.xdata, event.ydata, 0  # Project onto the x-y plane
    norm = np.sqrt(x**2 + y**2)
    
    if norm == 0:
        return  # Avoid division by zero
    
    # Convert to spherical coordinates
    theta = np.arccos(z)
    phi = np.arctan2(y, x) % (2 * np.pi)
    
    # Calculate the quantum state
    alpha = np.cos(theta / 2)
    beta = np.sin(theta / 2) * np.exp(1j * phi)
    
    # Print information
    print("Quantum State: |ψ⟩ = {:.2f}|0⟩ + {:.2f}e^{1j * {:.2f}}|1⟩".format(alpha, np.abs(beta), phi))
    print("Latitude: {:.2f} degrees, Longitude: {:.2f} degrees".format(np.degrees(theta), np.degrees(phi)))
    
    ax.scatter([x], [y], [z], color='r')  # Indicate selected point
    fig.canvas.draw()

def interactive_bloch_sphere():
    ax, fig = plot_bloch_sphere()
    fig.canvas.mpl_connect('button_press_event', lambda event: on_click(event, ax, fig))
    plt.show()

interactive_bloch_sphere()