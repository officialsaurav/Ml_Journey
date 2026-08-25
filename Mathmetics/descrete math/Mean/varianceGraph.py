import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

data = np.array([2, 4, 5, 6, 8, 10, 12])

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

mean = np.mean(data)
variance = np.mean((data - mean) ** 2)

bars = ax.bar(range(len(data)), (data - mean) ** 2)

ax.axhline(0, color="black")
ax.set_xlabel("Data points")
ax.set_ylabel("Squared deviation")
ax.set_title(f"Mean = {mean:.2f} | Variance = {variance:.2f}")

# Slider to change one value
slider_ax = plt.axes([0.2, 0.08, 0.6, 0.03])

slider = Slider(
    slider_ax,
    "Value",
    0,
    20,
    valinit=data[0]
)

def update(value):
    data[0] = slider.val

    mean = np.mean(data)
    squared_deviation = (data - mean) ** 2
    variance = np.mean(squared_deviation)

    for bar, height in zip(bars, squared_deviation):
        bar.set_height(height)

    ax.set_title(
        f"Mean = {mean:.2f} | Variance = {variance:.2f}"
    )

    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()