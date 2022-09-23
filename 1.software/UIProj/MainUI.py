# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 762)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_1 = QGroupBox(self.centralwidget)
        self.groupBox_1.setObjectName(u"groupBox_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_1.sizePolicy().hasHeightForWidth())
        self.groupBox_1.setSizePolicy(sizePolicy)
        self.groupBox_1.setMinimumSize(QSize(0, 50))
        self.gridLayout = QGridLayout(self.groupBox_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_1_horizontalLayout = QHBoxLayout()
        self.groupBox_1_horizontalLayout.setSpacing(0)
        self.groupBox_1_horizontalLayout.setObjectName(u"groupBox_1_horizontalLayout")
        self.groupBox_1_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.serachDeviceButton = QPushButton(self.groupBox_1)
        self.serachDeviceButton.setObjectName(u"serachDeviceButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.serachDeviceButton.sizePolicy().hasHeightForWidth())
        self.serachDeviceButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.serachDeviceButton.setFont(font)

        self.groupBox_1_horizontalLayout.addWidget(self.serachDeviceButton)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.groupBox_1_horizontalLayout.addItem(self.horizontalSpacer)

        self.deviceNameLable = QLabel(self.groupBox_1)
        self.deviceNameLable.setObjectName(u"deviceNameLable")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.deviceNameLable.sizePolicy().hasHeightForWidth())
        self.deviceNameLable.setSizePolicy(sizePolicy2)
        self.deviceNameLable.setFont(font)

        self.groupBox_1_horizontalLayout.addWidget(self.deviceNameLable)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.groupBox_1_horizontalLayout.addItem(self.horizontalSpacer_2)

        self.deviceSelectComobBox = QComboBox(self.groupBox_1)
        self.deviceSelectComobBox.setObjectName(u"deviceSelectComobBox")
        sizePolicy.setHeightForWidth(self.deviceSelectComobBox.sizePolicy().hasHeightForWidth())
        self.deviceSelectComobBox.setSizePolicy(sizePolicy)
        self.deviceSelectComobBox.setFont(font)

        self.groupBox_1_horizontalLayout.addWidget(self.deviceSelectComobBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.groupBox_1_horizontalLayout.addItem(self.horizontalSpacer_3)

        self.ferqLabel = QLabel(self.groupBox_1)
        self.ferqLabel.setObjectName(u"ferqLabel")
        sizePolicy2.setHeightForWidth(self.ferqLabel.sizePolicy().hasHeightForWidth())
        self.ferqLabel.setSizePolicy(sizePolicy2)
        self.ferqLabel.setFont(font)

        self.groupBox_1_horizontalLayout.addWidget(self.ferqLabel)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.groupBox_1_horizontalLayout.addItem(self.horizontalSpacer_4)

        self.freqSelectComobBox = QComboBox(self.groupBox_1)
        self.freqSelectComobBox.setObjectName(u"freqSelectComobBox")
        sizePolicy.setHeightForWidth(self.freqSelectComobBox.sizePolicy().hasHeightForWidth())
        self.freqSelectComobBox.setSizePolicy(sizePolicy)
        self.freqSelectComobBox.setFont(font)

        self.groupBox_1_horizontalLayout.addWidget(self.freqSelectComobBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.groupBox_1_horizontalLayout.addItem(self.horizontalSpacer_5)

        self.channalNumLabel = QLabel(self.groupBox_1)
        self.channalNumLabel.setObjectName(u"channalNumLabel")
        sizePolicy2.setHeightForWidth(self.channalNumLabel.sizePolicy().hasHeightForWidth())
        self.channalNumLabel.setSizePolicy(sizePolicy2)
        self.channalNumLabel.setFont(font)

        self.groupBox_1_horizontalLayout.addWidget(self.channalNumLabel)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.groupBox_1_horizontalLayout.addItem(self.horizontalSpacer_6)

        self.channalNumSelectComobBox = QComboBox(self.groupBox_1)
        self.channalNumSelectComobBox.setObjectName(u"channalNumSelectComobBox")
        sizePolicy.setHeightForWidth(self.channalNumSelectComobBox.sizePolicy().hasHeightForWidth())
        self.channalNumSelectComobBox.setSizePolicy(sizePolicy)
        self.channalNumSelectComobBox.setFont(font)

        self.groupBox_1_horizontalLayout.addWidget(self.channalNumSelectComobBox)

        self.horizontalSpacer_25 = QSpacerItem(200, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.groupBox_1_horizontalLayout.addItem(self.horizontalSpacer_25)


        self.gridLayout.addLayout(self.groupBox_1_horizontalLayout, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.groupBox_2.setMinimumSize(QSize(800, 300))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mainChart = QChartView(self.groupBox_2)
        self.mainChart.setObjectName(u"mainChart")

        self.gridLayout_2.addWidget(self.mainChart, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 10, 10)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy4)
        self.groupBox_3.setMinimumSize(QSize(550, 175))
        self.groupBox_3.setFont(font)
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_22 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_22, 2, 3, 1, 1)

        self.gradientSetDoubleSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.gradientSetDoubleSpinBox.setObjectName(u"gradientSetDoubleSpinBox")
        sizePolicy4.setHeightForWidth(self.gradientSetDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.gradientSetDoubleSpinBox.setSizePolicy(sizePolicy4)
        self.gradientSetDoubleSpinBox.setMinimumSize(QSize(80, 0))

        self.gridLayout_4.addWidget(self.gradientSetDoubleSpinBox, 1, 4, 1, 1)

        self.demoduleCheckBox = QCheckBox(self.groupBox_3)
        self.demoduleCheckBox.setObjectName(u"demoduleCheckBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.demoduleCheckBox.sizePolicy().hasHeightForWidth())
        self.demoduleCheckBox.setSizePolicy(sizePolicy5)
        self.demoduleCheckBox.setMinimumSize(QSize(80, 0))
        font1 = QFont()
        font1.setPointSize(10)
        self.demoduleCheckBox.setFont(font1)

        self.gridLayout_4.addWidget(self.demoduleCheckBox, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_10, 0, 5, 1, 1)

        self.gradientCheckBox = QCheckBox(self.groupBox_3)
        self.gradientCheckBox.setObjectName(u"gradientCheckBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.gradientCheckBox.sizePolicy().hasHeightForWidth())
        self.gradientCheckBox.setSizePolicy(sizePolicy6)
        self.gradientCheckBox.setMinimumSize(QSize(80, 0))
        self.gradientCheckBox.setFont(font1)

        self.gridLayout_4.addWidget(self.gradientCheckBox, 1, 0, 1, 1)

        self.gradientLabel = QLabel(self.groupBox_3)
        self.gradientLabel.setObjectName(u"gradientLabel")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.gradientLabel.sizePolicy().hasHeightForWidth())
        self.gradientLabel.setSizePolicy(sizePolicy7)
        self.gradientLabel.setMinimumSize(QSize(60, 0))
        self.gradientLabel.setFont(font1)

        self.gridLayout_4.addWidget(self.gradientLabel, 1, 2, 1, 1)

        self.demoduleFilterLabel = QLabel(self.groupBox_3)
        self.demoduleFilterLabel.setObjectName(u"demoduleFilterLabel")
        sizePolicy7.setHeightForWidth(self.demoduleFilterLabel.sizePolicy().hasHeightForWidth())
        self.demoduleFilterLabel.setSizePolicy(sizePolicy7)
        self.demoduleFilterLabel.setMinimumSize(QSize(60, 0))
        self.demoduleFilterLabel.setFont(font1)

        self.gridLayout_4.addWidget(self.demoduleFilterLabel, 0, 6, 1, 1)

        self.denoiseCheckBox = QCheckBox(self.groupBox_3)
        self.denoiseCheckBox.setObjectName(u"denoiseCheckBox")
        sizePolicy6.setHeightForWidth(self.denoiseCheckBox.sizePolicy().hasHeightForWidth())
        self.denoiseCheckBox.setSizePolicy(sizePolicy6)
        self.denoiseCheckBox.setMinimumSize(QSize(80, 0))
        self.denoiseCheckBox.setFont(font1)

        self.gridLayout_4.addWidget(self.denoiseCheckBox, 2, 0, 1, 1)

        self.denoiseValueSetdoubleSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.denoiseValueSetdoubleSpinBox.setObjectName(u"denoiseValueSetdoubleSpinBox")
        self.denoiseValueSetdoubleSpinBox.setMinimumSize(QSize(80, 0))

        self.gridLayout_4.addWidget(self.denoiseValueSetdoubleSpinBox, 2, 8, 1, 1)

        self.demoduleFucSelectComboBox = QComboBox(self.groupBox_3)
        self.demoduleFucSelectComboBox.setObjectName(u"demoduleFucSelectComboBox")
        sizePolicy4.setHeightForWidth(self.demoduleFucSelectComboBox.sizePolicy().hasHeightForWidth())
        self.demoduleFucSelectComboBox.setSizePolicy(sizePolicy4)
        self.demoduleFucSelectComboBox.setMinimumSize(QSize(80, 0))

        self.gridLayout_4.addWidget(self.demoduleFucSelectComboBox, 0, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_9, 1, 9, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_12, 2, 5, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_20, 0, 3, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_21, 1, 3, 1, 1)

        self.denoiseFucSelectComboBox = QComboBox(self.groupBox_3)
        self.denoiseFucSelectComboBox.setObjectName(u"denoiseFucSelectComboBox")
        sizePolicy4.setHeightForWidth(self.denoiseFucSelectComboBox.sizePolicy().hasHeightForWidth())
        self.denoiseFucSelectComboBox.setSizePolicy(sizePolicy4)
        self.denoiseFucSelectComboBox.setMinimumSize(QSize(80, 0))

        self.gridLayout_4.addWidget(self.denoiseFucSelectComboBox, 2, 4, 1, 1)

        self.denoiseValueLabel = QLabel(self.groupBox_3)
        self.denoiseValueLabel.setObjectName(u"denoiseValueLabel")
        sizePolicy7.setHeightForWidth(self.denoiseValueLabel.sizePolicy().hasHeightForWidth())
        self.denoiseValueLabel.setSizePolicy(sizePolicy7)
        self.denoiseValueLabel.setMinimumSize(QSize(60, 0))
        self.denoiseValueLabel.setFont(font1)

        self.gridLayout_4.addWidget(self.denoiseValueLabel, 2, 6, 1, 1)

        self.denoiseFucLabel = QLabel(self.groupBox_3)
        self.denoiseFucLabel.setObjectName(u"denoiseFucLabel")
        sizePolicy7.setHeightForWidth(self.denoiseFucLabel.sizePolicy().hasHeightForWidth())
        self.denoiseFucLabel.setSizePolicy(sizePolicy7)
        self.denoiseFucLabel.setMinimumSize(QSize(60, 0))
        self.denoiseFucLabel.setFont(font1)

        self.gridLayout_4.addWidget(self.denoiseFucLabel, 2, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_11, 1, 5, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_19, 2, 1, 1, 1)

        self.demoduleFucLabel = QLabel(self.groupBox_3)
        self.demoduleFucLabel.setObjectName(u"demoduleFucLabel")
        sizePolicy7.setHeightForWidth(self.demoduleFucLabel.sizePolicy().hasHeightForWidth())
        self.demoduleFucLabel.setSizePolicy(sizePolicy7)
        self.demoduleFucLabel.setMinimumSize(QSize(60, 0))
        self.demoduleFucLabel.setFont(font1)

        self.gridLayout_4.addWidget(self.demoduleFucLabel, 0, 2, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_17, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(30, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 2, 9, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 0, 9, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_18, 1, 1, 1, 1)

        self.demoduleFilterLenSetDoubleSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.demoduleFilterLenSetDoubleSpinBox.setObjectName(u"demoduleFilterLenSetDoubleSpinBox")
        self.demoduleFilterLenSetDoubleSpinBox.setMinimumSize(QSize(80, 0))

        self.gridLayout_4.addWidget(self.demoduleFilterLenSetDoubleSpinBox, 0, 8, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_23, 0, 7, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_24, 2, 7, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_13 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.statrButton = QPushButton(self.groupBox_3)
        self.statrButton.setObjectName(u"statrButton")

        self.horizontalLayout_10.addWidget(self.statrButton)

        self.horizontalSpacer_14 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)

        self.stopButton = QPushButton(self.groupBox_3)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout_10.addWidget(self.stopButton)

        self.horizontalSpacer_15 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_15)

        self.saveButton = QPushButton(self.groupBox_3)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_10.addWidget(self.saveButton)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_16)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)


        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy8)
        self.pushButton_4.setMinimumSize(QSize(100, 50))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.groupBox_4.setMinimumSize(QSize(400, 250))
        self.groupBox_4.setFont(font)
        self.graphicsView_2 = QGraphicsView(self.groupBox_4)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(120, 70, 256, 192))

        self.horizontalLayout_9.addWidget(self.groupBox_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)


        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f4d\u673a\u754c\u9762V1.0", None))
        self.groupBox_1.setTitle("")
        self.serachDeviceButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u8bbe\u5907", None))
        self.deviceNameLable.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u540d\u79f0\uff1a", None))
        self.ferqLabel.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u9891\u7387\uff1a", None))
        self.channalNumLabel.setText(QCoreApplication.translate("MainWindow", u"\u901a\u9053\u6570\uff1a", None))
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u8f85\u52a9\u9762\u677f", None))
        self.demoduleCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u8c03\u5904\u7406", None))
        self.gradientCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u68af\u5ea6\u5904\u7406", None))
        self.gradientLabel.setText(QCoreApplication.translate("MainWindow", u"\u68af\u5ea6\u503c\uff1a", None))
        self.demoduleFilterLabel.setText(QCoreApplication.translate("MainWindow", u"\u6ee4\u6ce2\u957f\u5ea6\uff1a", None))
        self.denoiseCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u6570\u503c\u964d\u566a", None))
        self.denoiseValueLabel.setText(QCoreApplication.translate("MainWindow", u"\u964d\u566a\u8bbe\u503c\uff1a", None))
        self.denoiseFucLabel.setText(QCoreApplication.translate("MainWindow", u"\u964d\u566a\u65b9\u6cd5\uff1a", None))
        self.demoduleFucLabel.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u8c03\u65b9\u6cd5\uff1a", None))
        self.statrButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u91c7\u96c6", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u91c7\u96c6", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8bc6\u522b", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u53ef\u7591\u533a\u57df", None))
    # retranslateUi

