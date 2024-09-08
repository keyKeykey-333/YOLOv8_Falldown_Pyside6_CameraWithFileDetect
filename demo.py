import csv
import sys
import os
import torch
import time
import cv2
import argparse
from ultralytics import YOLO
from ui_main import Ui_mainWindow
from qt_fit_image import QFitImage
from yolo_detect import YOLOv8Detector
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QImage, QPixmap
def parse_args():
    current_path = os.getcwd()
    model_file_path = os.path.join(current_path, "model_file","yolov8n.pt")
    input_video_path = os.path.join(current_path, "video_file","test.mp4")
    
    parser = argparse.ArgumentParser(description='Demo')
    
    parser.add_argument('--model_path', default=model_file_path, type=str, help='模型默认路径')
    parser.add_argument('--input_video_path',default=input_video_path,  type=str, help='输入的图片或视频路径')
    parser.add_argument('--device_use',default='cuda' if torch.cuda.is_available() else 'cpu',  type=str, help='cuda/cpu选择参数')
    parser.add_argument('--camera_or_file',default='',  type=str, help='用于判断是相机还是视频传到opencv里')
    parser.add_argument('--conf',default=65,  type=float, help='置信度')
    parser.add_argument('--camera',default=0,  type=int, help='相机默认0')
    parser.add_argument('--cuda_use_or_not',default=torch.cuda.is_available(),  type=bool, help='用于判断是否有cuda')
    return parser.parse_args()

class MainWindow(QMainWindow):
    def __init__(self,args):
        super(MainWindow, self).__init__()
        self.args = args
        self.current_path = os.getcwd()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.load_pt_files_to_qcomobox()
        self.ui.pushButton.clicked.connect(self.button_state1)
        self.ui.pushButton_2.clicked.connect(self.button_state2)
        if self.args.device_use == "cpu":
            self.ui.cuda_qcheckbox.setChecked(False)
        self.ui.table_widget.setColumnWidth(0, 70)
        self.ui.table_widget.setColumnWidth(1, 140)
        self.ui.statusBar.showMessage(f'状态:   ✔✔✔推理设备-{self.args.device_use}  ✔✔✔模型文件:{self.args.model_path}')
        self.image_frame = QFitImage(self)
        self.image_frame.setStyleSheet("background-color: black;")
        self.full_image_frame = QFitImage(self)
        self.full_image_frame.setStyleSheet("background-color: black;")
        self.ui.main_show_image_qlabel_father_qv.addWidget(self.image_frame)
        self.ui.main_show_image_qlabel_2_father_qv.addWidget(self.full_image_frame)
        
        self.ui.save_file_qcheckbox.clicked.connect(self.save_table_to_csv)
        self.ui.open_camera_button.clicked.connect(self.open_camera_slot)
        self.ui.select_picture_button.clicked.connect(self.open_file_dialog_slot)
        self.ui.select_video_button.clicked.connect(self.open_file_dialog_slot)
        self.ui.close_button.clicked.connect(self.yolov8detector_thread_stop_slot)
        self.ui.select_model_comboBox.currentIndexChanged.connect(self.select_model_comboBox_slot)
        self.ui.cuda_qcheckbox.stateChanged.connect(self.cuda_qcheckbox_state_slot)
        self.ui.conf_slider.valueChanged.connect(self.conf_slider_slot)

    
    def save_table_to_csv(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Table to CSV", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_path:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                headers = []
                for column in range(self.ui.table_widget.columnCount()):
                    header_item = self.ui.table_widget.horizontalHeaderItem(column)
                    if header_item is not None:
                        headers.append(header_item.text())
                    else:
                        headers.append(f"Column {column+1}")
                writer.writerow(headers)
                for row in range(self.ui.table_widget.rowCount()):
                    row_data = []
                    for column in range(self.ui.table_widget.columnCount()):
                        item = self.ui.table_widget.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)
            self.ui.statusBar.showMessage(f'状态:   ✔✔✔csv表格文件已经保存在{file_path}')

                  
    def conf_slider_slot(self):
        self.args.conf = self.ui.conf_slider.value()
        
        
    def open_camera_slot(self):
        self.args.camera_or_file = "camera"
        self.yolov8detector_thread_start()
        
        
    def open_file_dialog_slot(self):
        self.ui.statusBar.showMessage(f'状态:   ✔✔✔选择文件中...')

        self.args.camera_or_file = "file"
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)")
        if file_path:
            self.args.input_video_path = file_path
            self.yolov8detector_thread_start()
            
            
    def select_model_comboBox_slot(self):
        self.args.model_path = os.path.join(self.current_path, "model_file",self.ui.select_model_comboBox.currentText())
        print(f"选择的模型是{self.args.model_path}")
        self.ui.statusBar.showMessage(f'状态:   ✔✔✔模型变更: {self.args.model_path}')


    def cuda_qcheckbox_state_slot(self):
        if self.args.cuda_use_or_not:
            if self.ui.cuda_qcheckbox.isChecked():
                self.args.device_use = 'cuda'
            else:
                self.args.device_use = 'cpu'
        else:
            self.args.device_use = 'cpu'
        print(f"当前设备设置为: {self.args.device_use}")
        self.ui.statusBar.showMessage(f'状态:   ✔✔✔推理设备变更: {self.args.device_use}')


    def button_state1(self, state):
        self.ui.mainStackedWidget.setCurrentIndex(1)
        print("当前页面为全屏页面")
    def button_state2(self, state):
        self.ui.mainStackedWidget.setCurrentIndex(0)
        print("当前页面为非全屏页面")


    def load_pt_files_to_qcomobox(self):
        self.model_file_path = os.path.join(self.current_path, "model_file")
        for file_name in os.listdir(self.model_file_path):
            if file_name.endswith('.pt'):
                self.ui.select_model_comboBox.addItem(file_name)


    def yolov8detector_thread_start(self):
        # self.yolov8detector_thread_started_func()
        self.yolov8detector_instance = YOLOv8Detector(self.args)
        self.yolov8detector_thread = QThread(self)
        self.yolov8detector_instance.moveToThread(self.yolov8detector_thread)
        
        self.yolov8detector_instance.frame_ready.connect(self.update_image)
        self.yolov8detector_instance.finish_signal.connect(self.yolov8detector_thread_finish_func)
        self.yolov8detector_instance.table_list_signal.connect(self.update_table_slot)
        
        self.yolov8detector_thread.started.connect(self.yolov8detector_thread_started_func)
        self.yolov8detector_thread.started.connect(self.yolov8detector_instance.yolov8detector_workstart_func)

        self.yolov8detector_thread.start()
        print("yolov8detector_thread_start")
        # 任务信号处理
    @Slot(list)
    def update_table_slot(self,data):
        # print(data)
        self.ui.statusBar.showMessage(f'状态:   ✔✔✔目标检测实例建立成功,正在进行检测...')
        row_count = self.ui.table_widget.rowCount()
        self.ui.table_widget.insertRow(row_count)
        for col, value in enumerate(data):
            item = QTableWidgetItem(value)
            self.ui.table_widget.setItem(row_count, col, item)
        self.ui.table_widget.scrollToBottom()
        
    def yolov8detector_thread_started_func(self):
        self.ui.open_camera_button.setEnabled(False)
        self.ui.select_picture_button.setEnabled(False)
        self.ui.select_video_button.setEnabled(False)
        self.ui.close_button.setEnabled(True)
        print("目标检测实例建立中...")
        self.ui.statusBar.showMessage(f'状态:   ✔✔✔目标检测实例建立中...')

    def yolov8detector_thread_finish_func(self):
        self.yolov8detector_thread.quit()
        self.yolov8detector_thread.wait()
        self.ui.open_camera_button.setEnabled(True)
        self.ui.select_picture_button.setEnabled(True)
        self.ui.select_video_button.setEnabled(True)
        self.ui.close_button.setEnabled(False)
        self.yolov8detector_thread.deleteLater()
        self.yolov8detector_instance.deleteLater()
        print("实例销毁完成,内存回收完成,目标检测结束...")
        self.ui.statusBar.showMessage(f'状态:   ✔✔✔实例销毁完成,内存回收完成,目标检测结束...')
    def yolov8detector_thread_stop_slot(self):
        self.yolov8detector_instance.yolov8detector_workstop_func()
        print('停止键被按下,正在销毁实例,回收内存中...')
        self.ui.statusBar.showMessage(f'状态:   ✔停止键被按下,正在销毁实例,回收内存中...')

    @Slot(QPixmap)
    def update_image(self, pixmap,progress):
        self.image_frame.set_image(pixmap)
        self.full_image_frame.set_image(pixmap)
        self.ui.progress_bar.setValue(progress)
        
        

    
    
if __name__ == "__main__":
    args = parse_args()

    app = QApplication(sys.argv)
    window = MainWindow(args)
    window.show()
    sys.exit(app.exec())
