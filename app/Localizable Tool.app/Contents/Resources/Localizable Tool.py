# -*- coding: UTF-8 -*-
import tkinter

import PyQt5
import clipboard
from PyQt5 import QtCore, QtWidgets

from python import Xml2Xls, Xls2Xml


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.source_dir = ""
        self.target_dir = ""
        self.resultStr = ""

        self.setup_ui(self)
        self.retranslateUi(self)

    def setup_ui(self, window):
        window.setObjectName("MainWindow")
        window.resize(445, 420)
        self.centralWidget = QtWidgets.QWidget(window)
        self.retranslateUi(window)

        # Xml2Xls / Xls2Xml 转换方式选择 Radio
        self.typeChoose = QtWidgets.QLabel('Xml2Xls / Xls2Xml：', self.centralWidget)
        self.typeChoose.move(20, 20)
        self.typeChooseXml2Xls = QtWidgets.QRadioButton('Xml2Xls', self.centralWidget)
        self.typeChooseXml2Xls.move(20, 50)
        self.typeChooseXml2Xls.clicked.connect(self.choose_xml2xls_or_xls2xml)
        self.typeChooseXml2Xls.setChecked(True)
        self.typeChooseXls2Xml = QtWidgets.QRadioButton('Xls2Xml', self.centralWidget)
        self.typeChooseXls2Xml.move(120, 50)
        self.typeChooseXls2Xml.clicked.connect(self.choose_xml2xls_or_xls2xml)
        self.typeChooseGroup = QtWidgets.QButtonGroup(self.centralWidget)
        self.typeChooseGroup.addButton(self.typeChooseXml2Xls, 11)
        self.typeChooseGroup.addButton(self.typeChooseXls2Xml, 12)

        # 分割线
        self.lineView = QtWidgets.QLabel('------------------------------------------------------------------',
                                         self.centralWidget)
        self.lineView.move(20, 80)

        # 选择源文件夹和目标文件夹
        self.sourceDirBtn = QtWidgets.QPushButton(self.centralWidget)
        self.sourceDirBtn.setGeometry(QtCore.QRect(20, 110, 175, 50))
        self.sourceDirBtn.setText("选择源文件夹")
        self.sourceDirBtn.clicked.connect(self.choose_source_dir)
        self.targetDirBtn = QtWidgets.QPushButton(self.centralWidget)
        self.targetDirBtn.setGeometry(QtCore.QRect(250, 110, 175, 50))
        self.targetDirBtn.setText("选择目标文件夹")
        self.targetDirBtn.clicked.connect(self.choose_target_dir)

        # Single / Multiple 生成文件选项 Radio
        self.fileCreate = QtWidgets.QLabel('Single / Multiple：', self.centralWidget)
        self.fileCreate.move(20, 180)
        self.fileCreateSingle = QtWidgets.QRadioButton('single', self.centralWidget)
        self.fileCreateSingle.move(20, 210)
        self.fileCreateSingle.clicked.connect(self.choose_single_or_multiple)
        self.fileCreateSingle.setChecked(True)
        self.fileCreateMultiple = QtWidgets.QRadioButton('multiple', self.centralWidget)
        self.fileCreateMultiple.move(120, 210)
        self.fileCreateMultiple.clicked.connect(self.choose_single_or_multiple)
        self.fileCreateGroup = QtWidgets.QButtonGroup(self.centralWidget)
        self.fileCreateGroup.addButton(self.fileCreateSingle, 21)
        self.fileCreateGroup.addButton(self.fileCreateMultiple, 22)

        # 组装脚本 文本
        self.resultShellStr = QtWidgets.QTextBrowser(self.centralWidget)
        self.resultShellStr.setGeometry(QtCore.QRect(20, 250, 405, 100))
        self.resultShellStr.setText('脚本语言：')
        self.copyResultStrBtn = QtWidgets.QPushButton(self.centralWidget)
        self.copyResultStrBtn.setGeometry(QtCore.QRect(360, 310, 60, 35))
        self.copyResultStrBtn.setText("Copy")
        self.copyResultStrBtn.clicked.connect(self.copy_result_str)

        # 执行脚本 按钮
        self.todoBtn = QtWidgets.QPushButton(self.centralWidget)
        self.todoBtn.setGeometry(QtCore.QRect(135, 365, 175, 45))
        self.todoBtn.setText("GO MAKE")
        self.todoBtn.clicked.connect(self.todo_make)

        window.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Localizable Tool"))

    def choose_xml2xls_or_xls2xml(self):
        if self.typeChooseXml2Xls.isChecked():
            print("Xml2Xls")
            return "Xml2Xls"
        else:
            print("Xls2Xml")
            return "Xls2Xml"

    def choose_source_dir(self):
        self.source_dir = PyQt5.QtWidgets.QFileDialog.getExistingDirectory(self, "选择源文件夹", "")
        print(self.source_dir)
        self.formatResultShellStr()

    def choose_target_dir(self):
        self.target_dir = PyQt5.QtWidgets.QFileDialog.getExistingDirectory(self, "选择目标文件夹", "")
        print(self.target_dir)
        self.formatResultShellStr()

    def choose_single_or_multiple(self):
        if self.fileCreateSingle.isChecked():
            print("single")
            return "single"
        else:
            print("multiple")
            return "multiple"

    def formatResultShellStr(self):
        self.resultStr = "python3 " + self.choose_xml2xls_or_xls2xml() + ".py -f " + self.source_dir + " -t " + self.target_dir + " -e " + self.choose_single_or_multiple()
        print(self.resultStr)
        self.resultShellStr.setText("脚本语言：" + self.resultStr)

    def copy_result_str(self):
        if len(self.resultStr) != 0:
            clipboard.copy(self.resultStr)

    def todo_make(self):
        if self.typeChooseXml2Xls.isChecked():
            if self.fileCreateSingle.isChecked():
                Xml2Xls.convertToSingleFile(self.source_dir, self.target_dir)
            else:
                Xml2Xls.convertToMultipleFiles(self.source_dir, self.target_dir)
        else:
            if self.fileCreateSingle.isChecked():
                Xls2Xml.convertFromSingleForm(self.source_dir, self.target_dir)
            else:
                Xls2Xml.convertFromMultipleForm(self.source_dir, self.target_dir)
        print("OK")


if __name__ == "__main__":
    app = QtWidgets.QApplication(tkinter.sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MyWindow()
    ui.setup_ui(window)
    window.show()
    tkinter.sys.exit(app.exec_())
