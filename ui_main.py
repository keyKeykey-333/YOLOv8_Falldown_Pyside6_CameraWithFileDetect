# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from ui_file import camera_qrc_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1286, 890)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(14)
        self.centralwidget.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 0)
        self.mainStackedWidget = QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        self.mainStackedWidget.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.mainStackedWidgetPage1 = QWidget()
        self.mainStackedWidgetPage1.setObjectName(u"mainStackedWidgetPage1")
        self.verticalLayout_2 = QVBoxLayout(self.mainStackedWidgetPage1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.top_qframe = QFrame(self.mainStackedWidgetPage1)
        self.top_qframe.setObjectName(u"top_qframe")
        self.top_qframe.setMaximumSize(QSize(16777215, 80))
        self.top_qframe.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.top_qframe.setFrameShape(QFrame.StyledPanel)
        self.top_qframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.top_qframe)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.button_QHbox = QHBoxLayout()
        self.button_QHbox.setObjectName(u"button_QHbox")
        self.open_camera_button = QPushButton(self.top_qframe)
        self.open_camera_button.setObjectName(u"open_camera_button")
        self.open_camera_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_camera_button.setStyleSheet(u"background:transparent")
        icon = QIcon()
        icon.addFile(u":/camera/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_camera_button.setIcon(icon)
        self.open_camera_button.setIconSize(QSize(85, 85))

        self.button_QHbox.addWidget(self.open_camera_button)

        self.select_picture_button = QPushButton(self.top_qframe)
        self.select_picture_button.setObjectName(u"select_picture_button")
        self.select_picture_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_picture_button.setStyleSheet(u"background:transparent")
        icon1 = QIcon()
        icon1.addFile(u":/camera/picture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.select_picture_button.setIcon(icon1)
        self.select_picture_button.setIconSize(QSize(80, 75))

        self.button_QHbox.addWidget(self.select_picture_button)

        self.select_video_button = QPushButton(self.top_qframe)
        self.select_video_button.setObjectName(u"select_video_button")
        self.select_video_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_video_button.setStyleSheet(u"background: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u4e3a\u900f\u660e */\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/camera/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.select_video_button.setIcon(icon2)
        self.select_video_button.setIconSize(QSize(80, 80))

        self.button_QHbox.addWidget(self.select_video_button)

        self.close_button = QPushButton(self.top_qframe)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_button.setStyleSheet(u"background: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u4e3a\u900f\u660e */\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/camera/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(70, 60))
        self.close_button.setCheckable(False)
        self.close_button.setChecked(False)

        self.button_QHbox.addWidget(self.close_button)


        self.verticalLayout_7.addLayout(self.button_QHbox)


        self.verticalLayout_2.addWidget(self.top_qframe)

        self.mid_qhbox = QHBoxLayout()
        self.mid_qhbox.setObjectName(u"mid_qhbox")
        self.mid_qhbox__left_qframe = QFrame(self.mainStackedWidgetPage1)
        self.mid_qhbox__left_qframe.setObjectName(u"mid_qhbox__left_qframe")
        self.mid_qhbox__left_qframe.setMaximumSize(QSize(16777215, 16777215))
        self.mid_qhbox__left_qframe.setFrameShape(QFrame.StyledPanel)
        self.mid_qhbox__left_qframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.mid_qhbox__left_qframe)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.main_show_image_qlabel_father_qv = QVBoxLayout()
        self.main_show_image_qlabel_father_qv.setObjectName(u"main_show_image_qlabel_father_qv")

        self.verticalLayout_8.addLayout(self.main_show_image_qlabel_father_qv)

        self.progress_bar = QProgressBar(self.mid_qhbox__left_qframe)
        self.progress_bar.setObjectName(u"progress_bar")
        font1 = QFont()
        font1.setPointSize(9)
        self.progress_bar.setFont(font1)
        self.progress_bar.setLayoutDirection(Qt.LeftToRight)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(1)
        self.progress_bar.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_8.addWidget(self.progress_bar)

        self.table_widget = QTableWidget(self.mid_qhbox__left_qframe)
        if (self.table_widget.columnCount() < 5):
            self.table_widget.setColumnCount(5)
        font2 = QFont()
        font2.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setMinimumSize(QSize(0, 0))
        self.table_widget.setMaximumSize(QSize(972000, 150))
        self.table_widget.setFont(font2)
        self.table_widget.horizontalHeader().setDefaultSectionSize(242)

        self.verticalLayout_8.addWidget(self.table_widget)


        self.mid_qhbox.addWidget(self.mid_qhbox__left_qframe)

        self.mid_qhbox__right_qframe = QFrame(self.mainStackedWidgetPage1)
        self.mid_qhbox__right_qframe.setObjectName(u"mid_qhbox__right_qframe")
        self.mid_qhbox__right_qframe.setMaximumSize(QSize(250, 16777215))
        self.mid_qhbox__right_qframe.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.mid_qhbox__right_qframe.setFrameShape(QFrame.StyledPanel)
        self.mid_qhbox__right_qframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.mid_qhbox__right_qframe)
        self.verticalLayout_9.setSpacing(30)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.cuda_qcheckbox = QCheckBox(self.mid_qhbox__right_qframe)
        self.cuda_qcheckbox.setObjectName(u"cuda_qcheckbox")
        font5 = QFont()
        font5.setPointSize(15)
        self.cuda_qcheckbox.setFont(font5)
        self.cuda_qcheckbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.cuda_qcheckbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 20px;\n"
"height:20px;\n"
"};")
        self.cuda_qcheckbox.setChecked(True)

        self.verticalLayout_9.addWidget(self.cuda_qcheckbox)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.conf_qlabel = QLabel(self.mid_qhbox__right_qframe)
        self.conf_qlabel.setObjectName(u"conf_qlabel")
        self.conf_qlabel.setMaximumSize(QSize(65, 16777215))
        self.conf_qlabel.setFont(font5)

        self.horizontalLayout_3.addWidget(self.conf_qlabel)

        self.conf_really_value_qlabel = QLabel(self.mid_qhbox__right_qframe)
        self.conf_really_value_qlabel.setObjectName(u"conf_really_value_qlabel")
        self.conf_really_value_qlabel.setFont(font5)
        self.conf_really_value_qlabel.setLineWidth(2)
        self.conf_really_value_qlabel.setTextFormat(Qt.AutoText)

        self.horizontalLayout_3.addWidget(self.conf_really_value_qlabel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.conf_slider = QSlider(self.mid_qhbox__right_qframe)
        self.conf_slider.setObjectName(u"conf_slider")
        self.conf_slider.setMaximumSize(QSize(16777215, 100))
        self.conf_slider.setFont(font5)
        self.conf_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.conf_slider.setMaximum(99)
        self.conf_slider.setSingleStep(1)
        self.conf_slider.setSliderPosition(65)
        self.conf_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.conf_slider)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.select_model_qvbox = QVBoxLayout()
        self.select_model_qvbox.setSpacing(5)
        self.select_model_qvbox.setObjectName(u"select_model_qvbox")
        self.select_model_qlabel = QLabel(self.mid_qhbox__right_qframe)
        self.select_model_qlabel.setObjectName(u"select_model_qlabel")
        self.select_model_qlabel.setFont(font5)

        self.select_model_qvbox.addWidget(self.select_model_qlabel)

        self.select_model_comboBox = QComboBox(self.mid_qhbox__right_qframe)
        self.select_model_comboBox.setObjectName(u"select_model_comboBox")
        self.select_model_comboBox.setFont(font5)
        self.select_model_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.select_model_qvbox.addWidget(self.select_model_comboBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.select_model_qvbox.addItem(self.verticalSpacer_2)


        self.verticalLayout_9.addLayout(self.select_model_qvbox)

        self.pushButton = QPushButton(self.mid_qhbox__right_qframe)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 0))
        self.pushButton.setMaximumSize(QSize(200, 16777215))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_9.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.save_file_qcheckbox = QPushButton(self.mid_qhbox__right_qframe)
        self.save_file_qcheckbox.setObjectName(u"save_file_qcheckbox")
        self.save_file_qcheckbox.setMinimumSize(QSize(200, 0))
        self.save_file_qcheckbox.setMaximumSize(QSize(200, 16777215))
        self.save_file_qcheckbox.setFont(font)
        self.save_file_qcheckbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_file_qcheckbox.setLayoutDirection(Qt.LeftToRight)
        self.save_file_qcheckbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 20px;\n"
"height: 20px;\n"
"};")
        self.save_file_qcheckbox.setIconSize(QSize(9, 13))

        self.verticalLayout_9.addWidget(self.save_file_qcheckbox, 0, Qt.AlignHCenter)

        self.label = QLabel(self.mid_qhbox__right_qframe)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 150))
        self.label.setMaximumSize(QSize(16777215, 250))
        self.label.setPixmap(QPixmap(u":/camera/ultra.png"))

        self.verticalLayout_9.addWidget(self.label)


        self.mid_qhbox.addWidget(self.mid_qhbox__right_qframe)


        self.verticalLayout_2.addLayout(self.mid_qhbox)

        self.mainStackedWidget.addWidget(self.mainStackedWidgetPage1)
        self.only_picture = QWidget()
        self.only_picture.setObjectName(u"only_picture")
        self.verticalLayout = QVBoxLayout(self.only_picture)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_show_image_qlabel_2_father_qv = QVBoxLayout()
        self.main_show_image_qlabel_2_father_qv.setObjectName(u"main_show_image_qlabel_2_father_qv")

        self.verticalLayout.addLayout(self.main_show_image_qlabel_2_father_qv)

        self.pushButton_2 = QPushButton(self.only_picture)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(100, 16777215))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.mainStackedWidget.addWidget(self.only_picture)

        self.verticalLayout_3.addWidget(self.mainStackedWidget)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(mainWindow)
        self.statusBar.setObjectName(u"statusBar")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setKerning(True)
        self.statusBar.setFont(font6)
        mainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(mainWindow)
        self.conf_slider.valueChanged.connect(self.conf_really_value_qlabel.setNum)

        self.mainStackedWidget.setCurrentIndex(0)
        self.close_button.setDefault(False)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.open_camera_button.setText("")
        self.select_picture_button.setText("")
        self.select_video_button.setText("")
        self.close_button.setText("")
        ___qtablewidgetitem = self.table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"\u65f6\u95f4\u6233", None));
        ___qtablewidgetitem1 = self.table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"\u8bc6\u522b\u7ed3\u679c", None));
        ___qtablewidgetitem2 = self.table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"\u4f4d\u7f6e", None));
        ___qtablewidgetitem3 = self.table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mainWindow", u"\u6a21\u578b\u8def\u5f84", None));
        ___qtablewidgetitem4 = self.table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mainWindow", u"\u56fe\u7247/\u89c6\u9891\u8def\u5f84", None));
        self.cuda_qcheckbox.setText(QCoreApplication.translate("mainWindow", u"\u4f7f\u7528cuda", None))
        self.conf_qlabel.setText(QCoreApplication.translate("mainWindow", u"\u9608\u503c: 0.", None))
        self.conf_really_value_qlabel.setText(QCoreApplication.translate("mainWindow", u"65", None))
        self.select_model_qlabel.setText(QCoreApplication.translate("mainWindow", u"\u6a21\u578b\u9009\u62e9", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"\u56fe\u50cf\u5207\u6362\u4e3a\u5168\u5c4f\u663e\u793a", None))
        self.save_file_qcheckbox.setText(QCoreApplication.translate("mainWindow", u"\u4fdd\u5b58\u8868\u683c\u6587\u4ef6", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("mainWindow", u"\u5207\u6362\u4e3a\u975e\u5168\u5c4f", None))
    # retranslateUi

