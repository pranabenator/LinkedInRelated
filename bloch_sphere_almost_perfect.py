import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D

class BlochSphereApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.draw_bloch_sphere()

        self.last_text = None

        self.canvas.mpl_connect('button_press_event', self.on_click)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Interactive Bloch Sphere')
        self.show()

    def draw_bloch_sphere(self):
        # Draw the sphere
        u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
        x = np.sin(v)*np.cos(u)
        y = np.sin(v)*np.sin(u)
        z = np.cos(v)
        self.ax.plot_surface(x, y, z, color='b', alpha=0.1, linewidth=0)

    def on_click(self, event):
        if event.inaxes != self.ax:
            print("Click not on plot", file=sys.stderr)
            return
        x, y = event.xdata, event.ydata
        z_squared = 1 - x**2 - y**2 
        if z_squared >= 0 and (x**2 + y**2 <= 1):
            z = np.sqrt(z_squared)
            phi = np.arctan2(y, x) % (2 * np.pi)
            theta = np.arccos(z)

            alpha = np.cos(theta / 2)
            beta = np.sin(theta / 2) * np.exp(1j * phi)
            message = f'|Ψ⟩ = {alpha:.2f}|0⟩ + {beta:.2f}e^{{i{phi:.2f}π}}|1⟩'
            message += f'\nTheta (lat): {np.degrees(theta):.0f}°, Phi (long): {np.degrees(phi):.0f}°'
            self.clear_annotations()
            self.last_text = self.ax.text(x, y, z, message, color='red', fontsize=10)

            # Redraw the canvas to show updates
            self.canvas.draw()

    def clear_annotations(self):
        if self.last_text:
            self.last_text.remove()
            self.last_text = None

def main():
    app = QApplication(sys.argv)
    ex = BlochSphereApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()