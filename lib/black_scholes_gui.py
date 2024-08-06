import sys

import numpy as np
from PySide6 import QtCore, QtGui
from PySide6 import QtWidgets as Qt
import black_scholes_algorithm as bsa
import black_scholes_graphs as bsg


def double_line_editor():
    q = Qt.QLineEdit()
    q.setValidator(QtGui.QDoubleValidator())
    return q


class ScholesGUI(Qt.QWidget):
    def __init__(self):
        super().__init__()
        self.S = double_line_editor()
        self.K = double_line_editor()
        self.T = double_line_editor()
        self.r = double_line_editor()
        self.vol = double_line_editor()

        self.calculate_button = Qt.QPushButton('Calculate')
        self.graph_button = Qt.QPushButton('Open Graph')

        self.call_option_text = Qt.QLabel('Call Option')
        self.put_option_text = Qt.QLabel('Put Option')

        self.layout = Qt.QHBoxLayout(self)
        self.layout.addLayout(self.left_column())
        self.layout.addLayout(self.right_column())

        self.calculate_button.clicked.connect(self.calculate)
        self.graph_button.clicked.connect(self.open_graphs)

    def left_column(self):
        lc = Qt.QFormLayout()
        lc.addRow('Stock Price ($):', self.S)
        lc.addRow('Strike Price ($):', self.K)
        lc.addRow('Time (Years):', self.T)
        lc.addRow('Risk:', self.r)
        lc.addRow('Volatility (σ):', self.vol)
        lc.addRow(self.calculate_button)
        return lc

    def right_column(self):
        rc = Qt.QVBoxLayout(self)
        rc.addLayout(self.display_calculations_row())
        rc.addWidget(self.graph_button)
        rc.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        return rc

    def display_calculations_row(self):
        dc = Qt.QHBoxLayout()
        dc.addWidget(self.call_option_text)
        dc.addWidget(self.put_option_text)
        dc.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        return dc

    def option_v_volatility_graphs(self):
        volatilities = np.linspace(0.1, 1.0, 100)
        call_prices = []
        for vol in volatilities:
            c = bsa.BlackScholesCalculator(
                float(self.S.text()),
                float(self.K.text()),
                float(self.T.text()),
                float(self.r.text()),
                vol
            ).call_option_price()
            call_prices.append(c)

        put_prices = []
        for vol in volatilities:
            c = bsa.BlackScholesCalculator(
                float(self.S.text()),
                float(self.K.text()),
                float(self.T.text()),
                float(self.r.text()),
                vol
            ).put_option_price()
            put_prices.append(c)

        call_price_graph = bsg.BSGraphs('Volatility', volatilities, 'Call Option Price', call_prices)
        put_price_graph = bsg.BSGraphs('Volatility', volatilities, 'Put Option Price', put_prices)
        return [call_price_graph, put_price_graph]

    def calculate(self):
        bc = bsa.BlackScholesCalculator(
            float(self.S.text()),
            float(self.K.text()),
            float(self.T.text()),
            float(self.r.text()),
            float(self.vol.text())
        )
        cp = bc.call_option_price()
        pp = bc.put_option_price()
        self.call_option_text.setText(f'Call Option {round(cp, 2)}')
        self.put_option_text.setText(f'Call Option {round(pp, 2)}')

    def open_graphs(self):
        self.right_column().addWidget(self.option_v_volatility_graphs()[0])
        self.right_column().addWidget(self.option_v_volatility_graphs()[1])


if __name__ == "__main__":
    app = Qt.QApplication([])

    widget = ScholesGUI()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec())
