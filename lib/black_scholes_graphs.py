import matplotlib
from PySide6 import QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class BlackScholesGraphs(QtWidgets.QMainWindow):
    def __init__(self, x_label, x_plots: list[float], y_label, y_plots: list[float],  *args, **kwargs):
        super(BlackScholesGraphs, self).__init__(*args, **kwargs)

        self.x_label = x_label
        self.x_plots = x_plots
        self.y_label = y_label
        self.y_plots = y_plots

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.figure.supxlabel(self.x_label)
        sc.figure.supylabel(self.y_label)

        sc.axes.plot(self.x_plots, self.y_plots)

        toolbar = NavigationToolbar(sc, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()
