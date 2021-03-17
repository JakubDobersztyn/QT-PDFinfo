# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtpdfinfo.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from os import path, walk
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QMessageBox, QAbstractItemView, QWidget
from PyQt5.QtCore import Qt, QUrl, QRect
import pdf_size_calc
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

class ListboxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setSelectionMode(QAbstractItemView.MultiSelection)
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
            # print(event.mimeData().text())
            event.setDropAction(Qt.CopyAction)
            event.accept()
            self.clear()

            for url in event.mimeData().urls():
                if path.isdir(url.toLocalFile()):
                    for root, dirs, files in walk(url.toLocalFile()):
                        for name in files:
                            if name.endswith(".pdf"):
                                self.links.append(str(path.join(root, name)))
                else:
                    if url.toLocalFile().endswith(".pdf"):
                        self.links.append(str(url.toLocalFile()))
            # print(len(self.links))
            self.addItems(self.links)
            self.print_calcs(self.links)

        else:
            event.ignore()

    def print_calcs(self, lst):
        # self.clear()

        a, b, c, d, e = pdf_size_calc.pdf_size_calc(lst)
        calc = ListboxWidget.calcs_format(a,b,c,d,e)
        ui.pdfInfos.setText(calc)

    @classmethod
    def calcs_format(cls, a, b, c, d, e):
        fstr = f"Ilosc a4:    {a} \n\nIlosc a3:    {b}   |   Metry a3:    {c} \n\nMetry:    {d}\nIlosc arkuszy wf:    {e}\n\n"
        return fstr



    def del_selected(self):
        newlist = []
        listItems = self.selectedItems()
        if not listItems:
            return
        for item in listItems:
            # print(item.text())
            self.takeItem(self.row(item))
            self.links.remove(item.text())

        for i in range(self.count()):
            # print(self.item(i).text())
            newlist.append(self.item(i).text())
        # print("newlist", newlist)
        # print(listItems)
        self.print_calcs(newlist)
        # self.mimeData().clear()



class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = ListboxWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")

        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(920, 470, 89, 25))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(self.closeEvent)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(720, 470, 89, 25))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.clicked.connect(lambda: self.clear_list())
        self.printButton = QtWidgets.QPushButton(self.centralwidget)
        self.printButton.setGeometry(QtCore.QRect(820, 470, 89, 25))
        self.printButton.setObjectName("printButton")
        self.printButton.clicked.connect(self.printDialog)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1, 1))

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
        self.pdfInfos.setTextInteractionFlags(Qt.TextSelectableByMouse)
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
        self.actionNew.triggered.connect(lambda: self.clear_list())
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.closeEvent)
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCut.triggered.connect(lambda: self.listWidget.del_selected())

        self.actionAbout_author = QtWidgets.QAction(MainWindow)
        self.actionAbout_author.setObjectName("actionAbout_author")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)

        self.menuHelp.addAction(self.actionAbout_author)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def closeEvent(self, event):
        app.quit()

    def clear_list(self):
        self.listWidget.clear()
        self.listWidget.links = []



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QT PDFinfo"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.printButton.setText(_translate("MainWindow", "Print"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.pdfInfos.setText(_translate("MainWindow", ""))
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
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setStatusTip(_translate("MainWindow", "Cut selected"))
        self.actionCut.setShortcut(_translate("MainWindow", "Delete"))

        self.actionAbout_author.setText(_translate("MainWindow", "About author"))
        self.actionAbout_author.setStatusTip(_translate("MainWindow", "Display author info"))

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        self.textEdit.setText(self.pdfInfos.text())

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
