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
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QImage, QPixmap
 

class YOLOv8Detector(QObject):
    frame_ready = Signal(QPixmap,int)  # 定义信号用于传递 QPixmap 图像
    finish_signal = Signal()
    table_list_signal = Signal(list)
    def __init__(self,args):
        super().__init__()
        self.args = args
        self.running = False
        self.model = YOLO(self.args.model_path)
        self.frame_number=0
        self.yolo_train_names=['down','person','mouse']
        self.frame_count=0
        # self.last_emit_time = time.time()
    def yolov8detector_workstart_func(self):
        """
        从视频文件逐帧检测目标，或从图片文件中检测目标并显示结果。
        """
        self.running = True
        if self.args.camera_or_file == "file":
            self.input_path = self.args.input_video_path
            file_ext = os.path.splitext(self.input_path)[1].lower()

            if file_ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
                # 处理单张图片
                self.process_image(self.input_path)
            elif file_ext in ['.mp4', '.avi', '.mov', '.mkv']:
                # 处理视频
                self.process_video(self.input_path)
            else:
                print(f"不支持的文件格式：{file_ext}")
                return
        elif self.args.camera_or_file == 'camera':
            self.input_path = self.args.camera
            self.process_video(self.input_path)
            

        # 处理完成后发出结束信号
        self.finish_signal.emit()

    def process_image(self, image_path):
        frame = cv2.imread(image_path)
        if frame is None:
            print(f"无法读取图片文件：{image_path}")
            return

        results = self.model.predict(frame, device=self.args.device_use, conf = float(self.args.conf)/100.0)
        annotated_frame = results[0].plot()

        qimage = self.convert_cv_to_qimage(annotated_frame)
        pixmap = QPixmap.fromImage(qimage)
        self.frame_ready.emit(pixmap,0)

    def process_video(self, video_path):
        """
        处理视频文件的目标检测。
        """
        cap = cv2.VideoCapture(video_path)
        # print(type(fps))
        if not cap.isOpened():
            print(f"无法打开视频文件：{video_path}")
            return
        fps = cap.get(cv2.CAP_PROP_FPS)
        self.total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.current_frame = 0

        while cap.isOpened() and self.running:
            ret, frame = cap.read()
            if not ret:
                break
            
            results = self.model.predict(frame, device=self.args.device_use, conf = float(self.args.conf)/100.0)
            annotated_frame = results[0].plot()
            self.frame_count = self.frame_count+1
            for result in results:
                boxes = result.boxes  # 获取所有边界框
                if boxes is not None:
                    for box in boxes:
                        if box.cls == 2:  # 假设类别ID 0 代表“人”
                            x1, y1, x2, y2 = box.xyxy[0]  # 获取边界框的坐标
                            # items = [QTableWidgetItem(str(self.current_frame)),QTableWidgetItem(self.yolo_train_names[int(box.cls.item())]),QTableWidgetItem(f"{x1:.2f}, {y1:.2f}, {x2:.2f}, {y2:.2f}"),QTableWidgetItem(self.args.model_path),QTableWidgetItem(self.args.input_video_path)]
                            items = [str(self.current_frame),self.yolo_train_names[int(box.cls.item())],f"{x1:.2f}, {y1:.2f}, {x2:.2f}, {y2:.2f}",self.args.model_path,self.args.input_video_path]
                            # current_time = time.time()
                            # if current_time - self.last_emit_time >= 5:
                                # self.last_emit_time = current_time
                                # print(self.current_frame)
                            # if self.frame_count>int(fps/2.0):
                                # self.frame_count=0
                            self.table_list_signal.emit(items)

            self.frame_number += 1
            qimage = self.convert_cv_to_qimage(annotated_frame)
            pixmap = QPixmap.fromImage(qimage)

            # 发射信号
            self.current_frame += 1
            self.frame_ready.emit(pixmap,int((self.current_frame / self.total_frames) * 100))

        cap.release()
    def yolov8detector_workstop_func(self):
        self.running = False
    def convert_cv_to_qimage(self, cv_img):
        """ 将 OpenCV 图像转换为 QImage """
        if len(cv_img.shape) == 3:
            height, width, channels = cv_img.shape
            bytes_per_line = channels * width
            qimage = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format_RGB888)
            return qimage.rgbSwapped()
        else:
            raise ValueError("Unsupported image format")
