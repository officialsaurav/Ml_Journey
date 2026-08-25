#animation for sin graph
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#sin graph
class SinGraph:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.x = np.linspace(0, 2 * np.pi, 100)
        self.line, = self.ax.plot(self.x, np.sin(self.x))

    def update(self, frame):
        self.line.set_ydata(np.sin(self.x + frame / 10.0))
        return self.line,

    def animate(self):
        ani = animation.FuncAnimation(self.fig, self.update, frames=100, interval=50, blit=True)
        plt.show()

print("Animating Sin Graph...")
sin_graph = SinGraph()
sin_graph.animate()
print("Animation Complete.")