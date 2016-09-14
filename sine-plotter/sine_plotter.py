"""Paul Fordham | ptf06c """
#!/user/bin/env python

import sys, os, random
from PyQt5 import QtWidgets, QtGui, QtCore

import matplotlib
matplotlib.use('QT5Agg')   ###
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas   ###
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar  ###
from matplotlib.figure import Figure
import numpy as np

class AppForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setup()

    def setup(self):
        self.main_frame = QtWidgets.QWidget()
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        self.setWindowTitle("Let's plot the sine function!")
        self.axes = self.fig.add_subplot(111)
        self.axes.axis([0, 2, -1.5, 1.5])
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
    
        # create buttons
        self.sineBtn = QtWidgets.QPushButton('Plot sine', self)
        self.sineBtn.clicked.connect(self.plotSine) # connect button click to method

        self.clearBtn = QtWidgets.QPushButton('Clear', self)
        self.clearBtn.clicked.connect(self.clear)

        # create labels
        self.ALabel = QtWidgets.QLabel('Amplitude: ', self)
	self.fLabel = QtWidgets.QLabel('Frequency: ', self)
	self.pLabel = QtWidgets.QLabel('Phase: ', self)

        # create text field listeners
        self.A = QtWidgets.QLineEdit()
	self.f = QtWidgets.QLineEdit()
        self.p = QtWidgets.QLineEdit()
        
        # add all widgets to grid layout
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.canvas,1,1,1,4)
        self.grid.addWidget(self.mpl_toolbar,2,1,1,4)
        self.grid.addWidget(self.ALabel,3,1,1,1)
        self.grid.addWidget(self.A,3,2,1,2)
        self.grid.addWidget(self.fLabel,4,1,1,1)
        self.grid.addWidget(self.f,4,2,1,2)
        self.grid.addWidget(self.pLabel,5,1,1,1)
        self.grid.addWidget(self.p,5,2,1,2)
        self.grid.addWidget(self.sineBtn,6,1,1,1)
        self.grid.addWidget(self.clearBtn,6,2,1,1)
       
        self.main_frame.setLayout(self.grid)     
        self.setCentralWidget(self.main_frame)

    # clear button
    def clear(self):
        self.axes.clear()
        self.canvas.draw()

    # plot sin button
    def plotSine(self):
        x = np.linspace(-np.pi, np.pi, 201)
        A = float(self.A.text())
        f = float(self.f.text())
        p = float(self.p.text())

        self.axes.plot(x, A*np.sin(2*np.pi*f*x+p))
        self.canvas.draw()

app = QtWidgets.QApplication(sys.argv)
form = AppForm()
form.show()
app.exec_()
