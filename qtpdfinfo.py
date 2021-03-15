# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtpdfinfo.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtCore import Qt, QUrl, QRect
import pdf_size_calc


class ListboxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setGeometry(QRect(10, 10, 531, 491))
        self.links = []

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            for url in event.mimeData().urls():
                if os.path.isdir(url.toLocalFile()):
                    for root, dirs, files in os.walk(url.toLocalFile()):
                        for name in files:
                            if name.endswith(".pdf"):
                                self.links.append(str(os.path.join(root, name)))
                else:
                    if url.toLocalFile().endswith(".pdf"):
                        self.links.append(str(url.toLocalFile()))
            # print(links)
            self.addItems(self.links)
            a,b,c,d = pdf_size_calc.pdf_size_calc(self.links)
            calcs = f"Ilosc a4: {a} \nIlosc a3: {b} metry a3: {c} \nmetry: {d}"
            ui.pdfInfos.setText(calcs)
        else:
            event.ignore()





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = ListboxWidget(self.centralwidget)
        # self.listWidget.setGeometry(QtCore.QRect(10, 10, 531, 491))
        self.listWidget.setObjectName("listWidget")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(920, 470, 89, 25))
        self.exitButton.setObjectName("exitButton")
        self.printButton = QtWidgets.QPushButton(self.centralwidget)
        self.printButton.setGeometry(QtCore.QRect(820, 470, 89, 25))
        self.printButton.setObjectName("printButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(550, 10, 461, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 6394, 425))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.pdfInfos = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pdfInfos.setObjectName("pdfInfos")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pdfInfos)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout_author = QtWidgets.QAction(MainWindow)
        self.actionAbout_author.setObjectName("actionAbout_author")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionAbout_author)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.printButton.setText(_translate("MainWindow", "Print"))
        self.pdfInfos.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In efficitur a nulla quis imperdiet. Curabitur egestas leo nisl, porta lacinia dui auctor at. Aliquam hendrerit interdum quam, a aliquam nibh finibus vitae. Nulla convallis mauris turpis, vel scelerisque urna imperdiet non. Sed finibus augue quis nisi pulvinar, varius dictum dolor consectetur. Praesent aliquam metus vel purus facilisis, in molestie arcu fringilla. Etiam commodo gravida dapibus. Vivamus et hendrerit lacus, vitae iaculis arcu. Mauris urna dui, dignissim ut varius non, accumsan at lorem. Nulla risus lacus, molestie ut sapien vel, dictum vestibulum quam. Nullam sagittis, odio mattis pulvinar mollis, tortor nulla tincidunt lorem, ac accumsan dolor quam at massa. Aliquam erat volutpat. Maecenas consectetur metus at euismod scelerisque.\n"
"\n"
"Pellentesque ornare, lorem nec condimentum posuere, lectus est euismod sem, ut pellentesque magna sem ac dui. In dolor nunc, mollis a mi quis, fermentum consequat est. Aliquam et lobortis justo, in varius libero. Phasellus ultricies fermentum erat, id venenatis felis lobortis eget. Sed elit arcu, porta vitae purus quis, malesuada dictum sapien. Pellentesque augue odio, lacinia sit amet mauris dapibus, auctor tempus mauris. Cras pulvinar, lectus sit amet varius posuere, enim arcu consectetur mauris, eget suscipit nisi nunc vel eros. Donec sollicitudin vel erat sed tempor. Ut suscipit velit vitae aliquam vulputate. Nullam elementum mi et aliquet luctus. Nulla nec nisl scelerisque, ullamcorper neque eget, ultrices eros. Nunc ut iaculis elit. Mauris eu arcu eget justo pharetra vulputate. Etiam sed ligula facilisis, efficitur erat sit amet, convallis erat. Proin tristique, magna ut fringilla commodo, enim nibh placerat augue, vel sagittis nisi lorem id orci.\n"
"\n"
"Pellentesque vel ante nibh. In fringilla vel arcu et mattis. Aliquam finibus malesuada lorem, nec tempor libero condimentum vel. Donec non aliquam erat. Fusce eget commodo eros. Sed orci felis, dictum ac sodales at, ornare non tellus. Quisque mattis ipsum ac bibendum convallis. Nunc id elit mi. Fusce velit ligula, volutpat ut tempus non, rhoncus rhoncus sapien. Praesent faucibus ut urna in mattis. Sed quam libero, accumsan nec tempus sit amet, maximus sed nunc. Aenean dapibus, enim in auctor facilisis, sem sem convallis arcu, sed feugiat erat sem eget massa. Vivamus quis nibh metus. Praesent blandit purus in diam porttitor posuere. Mauris faucibus neque sed efficitur viverra. Mauris accumsan est in metus vehicula, quis dapibus ante pellentesque.\n"
"\n"
"Sed vitae mauris nulla. Maecenas viverra neque sed est fringilla, non auctor ante pharetra. Vivamus eget vehicula purus. Cras eleifend augue quis arcu maximus, et vulputate nisl semper. Donec id suscipit arcu. Aenean iaculis ultrices faucibus. Quisque quis aliquam arcu. Sed sem enim, eleifend id augue ac, elementum tempor mauris. Proin vestibulum, mi quis convallis efficitur, arcu metus tristique lacus, sit amet aliquet leo sem nec mi. Sed tincidunt lorem id nisi convallis cursus. Nulla blandit eros eget leo aliquet, sit amet finibus magna pharetra. Aliquam ut tortor turpis.\n"
"\n"
"Maecenas vel euismod diam. Proin interdum dapibus laoreet. Duis interdum ullamcorper lectus pellentesque dictum. Quisque lacus turpis, rutrum nec consectetur eu, suscipit sit amet quam. Sed pellentesque a ipsum eu consequat. Suspendisse non eleifend odio. Curabitur pulvinar placerat sodales. Nulla semper dapibus sagittis. Maecenas congue neque ut nibh malesuada, at euismod purus mattis. In porttitor magna ac est varius, pharetra pretium lorem ultricies. Cras non dolor dui. Etiam tristique est egestas ipsum vulputate accumsan. Phasellus lobortis, turpis at volutpat cursus, neque sem congue erat, eu consequat eros libero at lorem."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Clear the list"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setStatusTip(_translate("MainWindow", "Print infos"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Close app"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy info"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste info"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionAbout_author.setText(_translate("MainWindow", "About author"))
        self.actionAbout_author.setStatusTip(_translate("MainWindow", "Display author info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
