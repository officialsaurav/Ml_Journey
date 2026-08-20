import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial data
data = np.array([2, 4, 5, 6, 8, 10, 12])

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Initial plot
scatter = ax.scatter(range(len(data)), data)

ax.set_ylim(0, 20)
ax.set_xlabel("Data points")
ax.set_ylabel("Value")

# Slider
slider_ax = plt.axes([0.2, 0.1, 0.6, 0.03])

std_slider = Slider(
    slider_ax,
    "Spread",
    0.5,
    10,
    valinit=1
)

def update(value):
    spread = std_slider.val

    mean = np.mean(data)
    new_data = mean + (data - mean) * spread

    scatter.set_offsets(
        np.c_[range(len(new_data)), new_data]
    )

    ax.set_title(
        f"Mean = {np.mean(new_data):.2f} | "
        f"SD = {np.std(new_data):.2f}"
    )

    fig.canvas.draw_idle()

std_slider.on_changed(update)

plt.show()