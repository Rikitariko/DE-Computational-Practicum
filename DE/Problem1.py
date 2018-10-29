from matplotlib import rcParams
from matplotlib.widgets import Slider
import NumericalMethods as nm
import matplotlib as mplt
from matplotlib import pyplot as plt

# Function that updates graphics
def update():
    global slider
    global ax1
    global ax2
    global ax3

    # create new values that depends on slider
    graph = nm.NumMethods(xStart, xFinite, yStart, int(slider.val))
    graph.buildPlot()
    graph.eulerMethod()
    graph.improvedEulerMethod()
    graph.rungeKutta()
    graph.errors()

    # clear subplots
    ax1.clear()
    ax2.clear()
    ax3.clear()

    # set the grid
    ax1.grid(True)
    ax1.set_ylabel("y")
    ax1.set_xlabel("x")
    ax2.grid(True)
    ax2.set_ylabel("y")
    ax2.set_xlabel("x")
    ax3.grid(True)
    ax3.set_xlabel("x\n\n")
    ax3.set_ylabel("y")

    # plot new values
    ax1.set_title("Numerical Methods")
    ax1.plot(graph.x, graph.yEuler, "blue", label="Euler Method")
    ax1.legend(loc='upper right')
    ax1.plot(graph.x, graph.yImprEuler, "cyan", label="Improved Euler")
    ax1.legend(loc='upper right')
    ax1.plot(graph.x, graph.yRunge, "red", label="Runge-Kutta")
    ax1.legend(loc='lower left')

    ax2.set_title("Exact solution")
    ax2.plot(graph.x, graph.y, "black", label="Grapth")
    ax2.legend(loc='upper center')
    ax3.set_title("Errors")

    ax3.plot(graph.x, graph.errorEuler, "blue", label="Euler Method")
    ax3.plot(graph.x, graph.errorImprEuler, "cyan", label="Improved Euler")
    ax3.plot(graph.x, graph.errorRunge, "red", label="Runge-Kutta")

    ax1.xaxis.set_major_locator(mplt.ticker.MultipleLocator(base=0.5))
    ax1.yaxis.set_major_locator(mplt.ticker.MultipleLocator(base=0.5))
    ax2.xaxis.set_major_locator(mplt.ticker.MultipleLocator(base=0.5))
    ax2.yaxis.set_major_locator(mplt.ticker.MultipleLocator(base=0.5))
    ax3.xaxis.set_major_locator(mplt.ticker.MultipleLocator(base=0.5))
    ax3.yaxis.set_major_locator(mplt.ticker.MultipleLocator(base=0.5))
    plt.draw()


def onChangeValue(value):
    update()


print("Initial x")
xStart = float(input())
print("Initial y")
yStart = float(input())
print("Finite x")
xFinite = float(input())

# create new figure
fig = plt.figure(figsize=(8, 7))
# set boundaries
fig.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.9, wspace=0.3, hspace=0.6)
# distance from title and subplot
rcParams['axes.titlepad'] = 12

ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

axes_slider = plt.axes([0.29, 0.01, 0.45, 0.02])
slider = Slider(axes_slider, label='number of points', valmin=2, valmax=1000, valinit=100)

# method that tracks a slider change
slider.on_changed(onChangeValue)
# First call
update()
plt.show()