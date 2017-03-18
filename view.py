# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'googledrive_view.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(995, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDrive = QtGui.QMenu(self.menubar)
        self.menuDrive.setObjectName(_fromUtf8("menuDrive"))
        self.menuFiles = QtGui.QMenu(self.menubar)
        self.menuFiles.setObjectName(_fromUtf8("menuFiles"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Drive = QtGui.QAction(MainWindow)
        self.actionOpen_Drive.setObjectName(_fromUtf8("actionOpen_Drive"))
        self.actionPush = QtGui.QAction(MainWindow)
        self.actionPush.setObjectName(_fromUtf8("actionPush"))
        self.actionPull = QtGui.QAction(MainWindow)
        self.actionPull.setObjectName(_fromUtf8("actionPull"))
        self.actionDiff = QtGui.QAction(MainWindow)
        self.actionDiff.setObjectName(_fromUtf8("actionDiff"))
        self.actionMd5sum = QtGui.QAction(MainWindow)
        self.actionMd5sum.setObjectName(_fromUtf8("actionMd5sum"))
        self.menuDrive.addAction(self.actionOpen_Drive)
        self.menuFiles.addAction(self.actionPush)
        self.menuFiles.addAction(self.actionPull)
        self.menuFiles.addAction(self.actionDiff)
        self.menuFiles.addAction(self.actionMd5sum)
        self.menubar.addAction(self.menuDrive.menuAction())
        self.menubar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Google Drive View", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "perm", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "owner", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "group", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "byte", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "date", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "syncstate", None))
        self.menuDrive.setTitle(_translate("MainWindow", "Drive", None))
        self.menuFiles.setTitle(_translate("MainWindow", "Files", None))
        self.actionOpen_Drive.setText(_translate("MainWindow", "Open Drive", None))
        self.actionPush.setText(_translate("MainWindow", "push", None))
        self.actionPull.setText(_translate("MainWindow", "pull", None))
        self.actionDiff.setText(_translate("MainWindow", "diff", None))
        self.actionMd5sum.setText(_translate("MainWindow", "md5sum ", None))

