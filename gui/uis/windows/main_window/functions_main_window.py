# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import shutil
import sys
import yara
import hashlib
import os
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
import gui.uis.windows.main_window
from qt_core import *
from gui.uis.windows.main_window import *
# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

import tkinter as tk
from tkinter import filedialog
type_dict = {}

size_dict = {}

num = 0

names = []  # 存储初始结果

lines = []  # 白名单行

table = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # 创建字符列表

rulepath = os.path.abspath('./rules')

path = 'D:/malware'

whitelist = []

cur_num = 0
# FUNCTIONS
class MainFunctions():
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.pass_text = QTableWidgetItem()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.names = []
    # SET MAIN WINDOW PAGES
    # ///////////////////////////////////////////////////////////////
    def set_page(self, page):
        self.ui.load_pages.pages.setCurrentWidget(page)

    # SET LEFT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_left_column_menu(
        self,
        menu,
        title,
        icon_path
    ):
        self.ui.left_column.menus.menus.setCurrentWidget(menu)
        self.ui.left_column.title_label.setText(title)
        self.ui.left_column.icon.set_icon(icon_path)

    # RETURN IF LEFT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def left_column_is_visible(self):
        width = self.ui.left_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # RETURN IF RIGHT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def right_column_is_visible(self):
        width = self.ui.right_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # SET RIGHT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_right_column_menu(self, menu):
        self.ui.right_column.menus.setCurrentWidget(menu)


    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_title_bar_btn(self, object_name):
        return self.ui.title_bar_frame.findChild(QPushButton, object_name)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_left_menu_btn(self, object_name):
        return self.ui.left_menu.findChild(QPushButton, object_name)
    
    # LEDT AND RIGHT COLUMNS / SHOW / HIDE
    # ///////////////////////////////////////////////////////////////
    def toggle_left_column(self):
        # GET ACTUAL CLUMNS SIZE
        width = self.ui.left_column_frame.width()
        right_column_width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, width, right_column_width, "left")

    def toggle_right_column(self):
        # GET ACTUAL COLUMNS SIZE
        left_column_width = self.ui.left_column_frame.width()
        width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, left_column_width, width, "right")

    # 主要扫描功能实现区域/////////////////////////////////////////////////////////////////////////////////
    # 以下仍以定向扫描为例，全局扫描则需要采用压栈反馈/回调/multiprocess等方式进行load_page中进度条的更新
    def whitelist(self, x):
        for line in lines:
            if x == line:
                return False
        return True
    def get_sha256(self, name):
        with open(name, 'rb') as f:
            sha256obj = hashlib.sha256()
            sha256obj.update(f.read())
            hash_value = sha256obj.hexdigest()
            return hash_value

    def get_md5(self, name):
        with open(name, 'rb') as f:
            md5obj = hashlib.md5()
            md5obj.update(f.read())
            hash_value = md5obj.hexdigest()
            return hash_value

    def get_path(self,p,x):
        return os.path.join(p, x)

    def get_rules(self,path):
        filepath = {}
        for index, file in enumerate(os.listdir(path)):
            rupath = os.path.join(path, file)
            key = "rule" + str(index)
            filepath[key] = rupath
        yararule = yara.compile(filepaths=filepath)
        return yararule

    def scan(self,rule,name,max_num):
        global cur_num
        fp = open(name, 'rb')
        matches = rule.match(data=fp.read())
        if len(matches) > 0:
            cur_num += 1
            self.circular_progress_2.set_value(round(cur_num/max_num * 100, 2))
            return (name, matches)  # 输出匹配到的文件路径和字符串
        else:
            return

    def get_files(self, paths, filenames):
        try:
            file_list = os.listdir(paths)
            file_list = list(map(lambda x: self.get_path(self,paths, x), file_list))  # 找到所有文件的绝对路径
            #file_list = list(filter(whitelist(), file_list))  # 删去白名单内文件
            f_names = list(filter(os.path.isfile, file_list))  # 找到当前目录下的文件
            names.extend(f_names)  # 存入names
            d_names = list(filter(os.path.isdir, file_list))  # 找出当前目录下文件夹名
            go = list(map(lambda x: self.get_files(self,self.get_path(self, paths, x), filenames), d_names))
        except (PermissionError, FileNotFoundError):
            pass

    def run(self,rulepath,path,names):
        rulepath = './rules'
        yararule = self.get_rules(self, rulepath)
        names = list(filter(lambda x: self.scan(self,yararule, x), names))



    def scan1(self,menu):
        # 避免重复编译规则，可以考虑将yara-rule写成全局变量
        # 或者本函数仅作为定向扫描使用，在文件处理时再进行进度条更新
        if not path =='None':
            my_files = MainFunctions.get_files(MainFunctions, path, [])
            yararule = MainFunctions.get_rules(MainFunctions, rulepath)
        try:
            self.names = list(filter(lambda x: MainFunctions.scan(MainFunctions,yararule, x), names))
            # self.run(MainFunctions,rulepath,path,names)
        except (FileNotFoundError, PermissionError):
            pass
            self.circular_progress_1.set_value(0)
        for name in names:
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number)  # Insert row
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(str(name)))  # Add name
            self.table_widget.setItem(row_number, 1, QTableWidgetItem(str(".fas")))  # Add label
            self.pass_text.setTextAlignment(Qt.AlignCenter)
            self.pass_text.setText(str("123"))
            self.table_widget.setItem(row_number, 2, self.pass_text)  # hash
            self.table_widget.setRowHeight(row_number, 22)
            self.circular_progress_1.set_value(round(row_number/len(names) * 100, 2))

    # 接下来处理names列表，首先按后缀分别统计数量存放
    # 暂时使用传统的字典实现，后期需要爬虫进行其他高级操作则改换DataFrame结构

    def get_dict(self):
        for name in names:
            type_name = os.path.splitext(name)[1]
            if not type_name:
                type_dict.setdefault("None", 0)
                type_dict["None"] += 1
            else:
                type_dict.setdefault(type_name, 0)
                type_dict[type_name] += 1

    # 逐个插入table-widget控件
    def get_result_table(self):
        for name in names:
            row_number = SetupMainWindow.table_widget.rowCount()
            self.table_widget.insertRow(row_number)  # Insert row
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(str(name)))  # Add name
            #self.table_widget.setItem(row_number, 1, QTableWidgetItem(str(".fas")))  # Add label
            self.pass_text.setTextAlignment(Qt.AlignCenter)
            self.pass_text.setText(str("123"))
            #self.table_widget.setItem(row_number, 2, self.pass_text)  # hash
            self.table_widget.setRowHeight(row_number, 22)
            self.circular_progress_1.set_value(round(row_number / len(names) * 100, 2))

    def get_malware_path(self):
        root = tk.Tk()
        root.withdraw()
        global path
        folderpath = None
        folderpath = filedialog.askdirectory()     # 获取文件夹路径
        # filepath = filedialog.askopenfilename()  # 获取文件路径
        if not folderpath is None:
         path = folderpath

    def result_handle(self, menu):
        row_list = []
        for item in self.table_widget.selectedItems():
            #row_num = item1.rowCount()
            cur_row = item.text()
            if cur_row in row_list:
                continue
            else:
                row_list.append(cur_row)
        for row in row_list:
            row = row.replace('\\', '/')  # 统一路径格式
            if os.path.isdir(row):
                cur_name = row + '.bak'
                try:
                    os.rename(row, cur_name)
                    shutil.copy(cur_name, './isolation')
                except (FileNotFoundError, PermissionError):
                    pass
        print(row_list)


    def full_disk_scan(self):
        table = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # 创建字符列表
        yararule = MainFunctions.get_rules(MainFunctions, rulepath)
        for word in table:
            single_disk = word+':/'
            if os.path.isdir(single_disk):
                try:
                    file_list = os.listdir(single_disk)
                    file_list = list(map(lambda m: self.get_path(self, single_disk, m), file_list))
                    file_list = list(filter(whitelist, file_list))
                    f_names = list(filter(os.path.isfile, file_list))
                    # 获取到f_names后，统计大小并设置进度条，当前盘符以及盘符进度 （多个进度条作用）
                    # 设置正在扫描单栏的文本
                    names.extend(f_names)
                    names = list(filter(lambda x: self.scan(self, yararule, x), names))
                except (PermissionError, FileNotFoundError):
                    pass



    #//////////////////////////////////////////////////////////////////////////////////////////////////



    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0
        time_animation = self.ui.settings["time_animation"]
        minimum_left = self.ui.settings["left_column_size"]["minimum"]
        maximum_left = self.ui.settings["left_column_size"]["maximum"]
        minimum_right = self.ui.settings["right_column_size"]["minimum"]
        maximum_right = self.ui.settings["right_column_size"]["maximum"]

        # Check Left Values        
        if left_box_width == minimum_left and direction == "left":
            left_width = maximum_left
        else:
            left_width = minimum_left

        # Check Right values        
        if right_box_width == minimum_right and direction == "right":
            right_width = maximum_right
        else:
            right_width = minimum_right       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.left_column_frame, b"minimumWidth")
        self.left_box.setDuration(time_animation)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.right_column_frame, b"minimumWidth")
        self.right_box.setDuration(time_animation)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.stop()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()