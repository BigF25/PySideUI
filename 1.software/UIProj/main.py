from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QGridLayout
)
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from MainUI import Ui_MainWindow
import sys
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter


class MyGenerate(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.series = QLineSeries()
        self.series.append(0, 6)
        self.series.append(2, 4)
        self.series.append(3, 8)
        self.series.append(7, 4)
        self.series.append(10, 5)
        self.series.append(QPointF(11, 1))
        self.series.append(QPointF(13, 3))
        self.series.append(QPointF(17, 6))
        self.series.append(QPointF(18, 3))
        self.series.append(QPointF(20, 2))

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Simple line chart example")
        self.mainChart = QChartView(self.chart)
        self.mainChart.setRenderHint(QPainter.Antialiasing)
        # self.setCentralWidget(self.mainChart)
        self.gridLayout_2.addWidget(self.mainChart, 0, 0, 1, 1)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myGenerate = MyGenerate()

    sys.exit(app.exec())  # 启动循环
