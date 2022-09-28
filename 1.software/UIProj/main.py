import sys
from collections import deque
import random

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter
from PySide6.QtNetwork import QTcpServer, QTcpSocket
from PySide6.QtNetwork import QHostAddress

from MainUI import Ui_MainWindow
from PySide6.QtCore import Qt


class Point:
    X = 0
    Y = 0


listpoint = deque()
AXIS_MAX_X = 30


class MyGenerate(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setupUi(self)
        self.CreatMainChart()

        self.my_ListenTcp = QTcpServer(self)  # 创建一个监听tcp
        try:
            print("creat my_ListenTcp succeed!")
        finally:
            pass

        self.my_ListenTcp.newConnection.connect(
            self.newConnection)  # 有新的连接请求后，创建一个通信tcp

    count = 0
    datatemp = 0
    
    def newConnection(self):
        self.createNewTcp()

    def createNewTcp(self):
        self.my_CommTcp = self.my_ListenTcp.nextPendingConnection()     # 创建通信tcp
        self.my_CommTcp.readyRead.connect(self.read_socket)  # 接收到数据后，执行读数据事件函数
        print("creat my_CommTcp succeed!")

    def read_socket(self):
        print("start read_socket")
        data = self.my_CommTcp.readAll()
        count = 0
        # datatemp = 0
        print(data)

        # 直到e 才append temp = 0
        # 直到空才释放本轮
        # 如果本轮不是e结尾，保留数据，下一个read继续，
        while True:
            # print(count, ':', data[count:count+1])
            if data[count:count+1] == b'e':
                if self.count > AXIS_MAX_X:
                    self.series.remove(0)
                    self.AxisX.setMin(self.count-AXIS_MAX_X)
                    self.AxisX.setMax(self.count)
                self.series.append(self.count, self.datatemp)
                self.count += 1
                print("datatemp",self.datatemp)
                self.datatemp = 0
                count += 1
            if data[count:count+1] == b'':
                break
            self.datatemp = self.datatemp*10 + int(data[count:count+1])
            count += 1
            
        # while data[count:count+1] != b'':
        #     # print(data[count:count+1])
        #     # print(count)
        #     while data[count:count+1] != b'e' and data[count:count+1] != b'':
        #         print(data[count:count+1])
        #         # print(data[count:count+1])
        #         datatemp =  int(data) + datatemp*10
        #         count += 1
        #         print(datatemp)
        #     datatemp = 0
        #     count += 1
        # if self.count > AXIS_MAX_X:
        #     self.series.remove(0)
        #     self.AxisX.setMin(self.count-AXIS_MAX_X)
        #     self.AxisX.setMax(self.count)
        # self.series.append(self.count, int(data))
        # self.count += 1
        # print(self.count)
        # print(hex(data))
        # print(datatemp)

    # def CreatMainChart
    def CreatMainChart(self):
        self.AxisX = QValueAxis()  # 新建一根X坐标轴
        self.AxisY = QValueAxis()  # 新建一根Y坐标轴
        self.AxisX.setMin(0)
        self.AxisX.setMax(AXIS_MAX_X)
        self.AxisY.setMin(0)
        self.AxisY.setMax(100)
        self.series = QLineSeries()  # 新建一根数据
        self.series.setPointsVisible(True)  # 设置点可见
        self.series.setName("随机数曲线")
        self.mainChart = QChart()
        # self.mainChart.legend().hide() # 隐藏图例
        # self.mainChart.setAnimationOptions(QChart.SeriesAnimations) # 设置平滑
        self.mainChart.addAxis(self.AxisX, Qt.AlignBottom)
        self.mainChart.addAxis(self.AxisY, Qt.AlignLeft)
        # self.mainChart.createDefaultAxes()
        self.mainChart.addSeries(self.series)
        self.series.attachAxis(self.AxisX)
        self.series.attachAxis(self.AxisY)
        self.mainChartView = QChartView(self.mainChart)
        self.mainChartView.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.gridLayout_2.addWidget(self.mainChartView, 0, 0, 1, 1)
    # end def

    def startButtonEvent(self):
        if self.count > AXIS_MAX_X:
            self.series.remove(0)
            self.AxisX.setMin(self.count-AXIS_MAX_X)
            self.AxisX.setMax(self.count)
        self.series.append(self.count, random.randint(0, 9))
        self.count += 1
        print(self.count)

    def serachDeviceButtonEvent(self):  # 按下搜索设备按钮，监听tcp开始监听
        self.my_ListenTcp.listen(
            address=QHostAddress("192.168.137.1"), port=8888)
        print("192.168.137.1:8888 start listening!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 加载窗体界面
    myGenerate = MyGenerate()
    myGenerate.show()
    sys.exit(app.exec())  # 启动循环
