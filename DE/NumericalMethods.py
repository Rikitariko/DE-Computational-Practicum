import numpy as np
class NumMethods:
    # Initialization of parameters
    def __init__(self, _xStart, _xFinite, _yStart, _count):
        self.xStart = _xStart
        self.xFinite = _xFinite
        self.yStart = _yStart
        self.count = _count
        self.h = (_xFinite - _xStart) / _count
        self.x = np.linspace(_xStart, _xFinite, _count)
        self.y = np.zeros([_count])
        # arrays for calculation numerical methods
        self.yEuler = np.zeros([_count])
        self.yImprEuler = np.zeros([_count])
        self.yRunge = np.zeros([_count])
        # arrays for calculation errors
        self.errorEuler = np.zeros([_count])
        self.errorImprEuler = np.zeros([_count])
        self.errorRunge = np.zeros([_count])

    # Exact solution
    def buildPlot(self):
        c = self.yStart*np.exp(self.xStart) - np.sin(self.xStart)*np.exp(self.xStart)/2 - np.cos(self.xStart)*np.exp(self.xStart)/2
        for i in range(0, self.count):
            self.y[i] = c * np.exp(-self.x[i]) + 0.5 * np.cos(self.x[i]) + 0.5 * np.sin(self.x[i])

    # Euler Method
    def eulerMethod(self):
        self.yEuler[0] = self.yStart
        for i in range(1, self.count):
            self.yEuler[i] = self.h * (np.cos(self.x[i - 1]) - self.yEuler[i - 1]) + self.yEuler[i - 1]

    # Improved Euler Method
    def improvedEulerMethod(self):
        self.yImprEuler[0] = self.yStart
        for i in range(1, self.count):
            newX = self.x[i - 1] + self.h / 2
            newY = self.yImprEuler[i - 1] + self.h / 2 * (np.cos(self.x[i - 1]) - self.yImprEuler[i - 1])
            self.yImprEuler[i] = self.h * (np.cos(newX) - newY) + self.yImprEuler[i - 1]

    # Runge-Kutta
    def rungeKutta(self):
        self.yRunge[0] = self.yStart
        for i in range(1, self.count):
            k1 = np.cos(self.x[i - 1]) - self.yRunge[i - 1]
            k2 = np.cos(self.x[i - 1] + self.h / 2) - (self.yRunge[i - 1] + self.h / 2 * k1)
            k3 = np.cos(self.x[i - 1] + self.h / 2) - (self.yRunge[i - 1] + self.h / 2 * k2)
            k4 = np.cos(self.x[i - 1] + self.h / 2) - (self.yRunge[i - 1] + self.h / 2 * k3)
            self.yRunge[i] = self.h / 6 * (k1 + k2 + k3 + k4) + self.yRunge[i - 1]

    # Errors
    def errors(self):
        for i in range(0, self.count):
            self.errorEuler[i] = self.y[i] - self.yEuler[i]
            self.errorImprEuler[i] = self.y[i] - self.yImprEuler[i]
            self.errorRunge[i] = self.y[i] - self.yRunge[i]