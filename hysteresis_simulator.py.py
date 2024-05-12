import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class HysteresisSimulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hysteresis Curve Simulator")
        self.geometry("800x600")

        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.slider_frame = tk.Frame(self)
        self.slider_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.b1 = tk.Button(self.slider_frame, text="Clear", command=self.clear)
        self.b1.pack(side=tk.LEFT)

        self.slider_a = tk.Scale(self.slider_frame, from_=-10, to=10, orient=tk.HORIZONTAL, command=self.update_a)
        self.slider_a.set(1)
        self.slider_a.pack(side=tk.LEFT, fill=tk.X)

        self.slider_b = tk.Scale(self.slider_frame, from_=-10, to=10, orient=tk.HORIZONTAL, command=self.update_b)
        self.slider_b.set(1)
        self.slider_b.pack(side=tk.LEFT, fill=tk.X)

        self.slider_c = tk.Scale(self.slider_frame, from_=-10, to=10, orient=tk.HORIZONTAL, command=self.update_c)
        self.slider_c.set(0)
        self.slider_c.pack(side=tk.LEFT, fill=tk.X)

        self.xdata = np.linspace(-10, 10, 1000)
        self.ydata = []
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)

        self.a = 1
        self.b = 1
        self.c = 0

        self.update()

    def update_a(self, value):
        self.a = float(value)
        self.update()

    def update_b(self, value):
        self.b = float(value)
        self.update()

    def update_c(self, value):
        self.c = float(value)
        self.update()

    def update(self):
        self.ydata = self.a * np.sin(self.b * self.xdata + self.c)
        self.ax.clear()
        self.ax.plot(self.xdata, self.ydata)
        self.ax.set_ylim(-10, 10)
        self.canvas.draw()

    def clear(self):
        self.ax.clear()
        self.canvas.draw()

if __name__ == "__main__":
    app = HysteresisSimulator()
    app.mainloop()