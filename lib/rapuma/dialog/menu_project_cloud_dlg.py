# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dennis/Projects/rapuma/lib/rapuma/dialog/menu_project_cloud_dlg.ui'
#
# Created: Tue Feb 25 20:05:58 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MenuProjectCloud(object):
    def setupUi(self, MenuProjectCloud):
        MenuProjectCloud.setObjectName("MenuProjectCloud")
        MenuProjectCloud.resize(445, 226)
        self.gridLayout = QtGui.QGridLayout(MenuProjectCloud)
        self.gridLayout.setObjectName("gridLayout")
        self.labelPathLocal = QtGui.QLabel(MenuProjectCloud)
        self.labelPathLocal.setObjectName("labelPathLocal")
        self.gridLayout.addWidget(self.labelPathLocal, 0, 0, 1, 1)
        self.pushButtonLocalBrowse = QtGui.QPushButton(MenuProjectCloud)
        self.pushButtonLocalBrowse.setObjectName("pushButtonLocalBrowse")
        self.gridLayout.addWidget(self.pushButtonLocalBrowse, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.pushButtonOk = QtGui.QPushButton(MenuProjectCloud)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.gridLayout.addWidget(self.pushButtonOk, 3, 1, 1, 1)
        self.pushButtonCancel = QtGui.QPushButton(MenuProjectCloud)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 3, 2, 1, 1)
        self.groupBoxAction = QtGui.QGroupBox(MenuProjectCloud)
        self.groupBoxAction.setObjectName("groupBoxAction")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxAction)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButtonPush = QtGui.QRadioButton(self.groupBoxAction)
        self.radioButtonPush.setChecked(True)
        self.radioButtonPush.setObjectName("radioButtonPush")
        self.gridLayout_2.addWidget(self.radioButtonPush, 0, 0, 1, 1)
        self.checkBoxFlush = QtGui.QCheckBox(self.groupBoxAction)
        self.checkBoxFlush.setEnabled(True)
        self.checkBoxFlush.setObjectName("checkBoxFlush")
        self.gridLayout_2.addWidget(self.checkBoxFlush, 0, 1, 1, 1)
        self.radioButtonPull = QtGui.QRadioButton(self.groupBoxAction)
        self.radioButtonPull.setObjectName("radioButtonPull")
        self.gridLayout_2.addWidget(self.radioButtonPull, 1, 0, 1, 1)
        self.checkBoxBackup = QtGui.QCheckBox(self.groupBoxAction)
        self.checkBoxBackup.setEnabled(False)
        self.checkBoxBackup.setChecked(True)
        self.checkBoxBackup.setObjectName("checkBoxBackup")
        self.gridLayout_2.addWidget(self.checkBoxBackup, 1, 1, 1, 1)
        self.radioButtonRestore = QtGui.QRadioButton(self.groupBoxAction)
        self.radioButtonRestore.setObjectName("radioButtonRestore")
        self.gridLayout_2.addWidget(self.radioButtonRestore, 2, 0, 1, 1)
        self.comboBoxCloudProjects = QtGui.QComboBox(self.groupBoxAction)
        self.comboBoxCloudProjects.setEnabled(False)
        self.comboBoxCloudProjects.setFrame(True)
        self.comboBoxCloudProjects.setObjectName("comboBoxCloudProjects")
        self.gridLayout_2.addWidget(self.comboBoxCloudProjects, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBoxAction, 2, 0, 1, 2)
        self.lineEditProjectLocal = QtGui.QLineEdit(MenuProjectCloud)
        self.lineEditProjectLocal.setObjectName("lineEditProjectLocal")
        self.gridLayout.addWidget(self.lineEditProjectLocal, 1, 0, 1, 2)

        self.retranslateUi(MenuProjectCloud)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked(bool)"), MenuProjectCloud.close)
        QtCore.QObject.connect(self.pushButtonOk, QtCore.SIGNAL("clicked()"), MenuProjectCloud.setupUi)
        QtCore.QObject.connect(self.radioButtonPull, QtCore.SIGNAL("toggled(bool)"), self.checkBoxBackup.setEnabled)
        QtCore.QObject.connect(self.radioButtonPush, QtCore.SIGNAL("toggled(bool)"), self.checkBoxFlush.setEnabled)
        QtCore.QObject.connect(self.pushButtonLocalBrowse, QtCore.SIGNAL("clicked(bool)"), MenuProjectCloud.setupUi)
        QtCore.QObject.connect(self.radioButtonRestore, QtCore.SIGNAL("toggled(bool)"), self.comboBoxCloudProjects.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MenuProjectCloud)
        MenuProjectCloud.setTabOrder(self.pushButtonCancel, self.pushButtonOk)
        MenuProjectCloud.setTabOrder(self.pushButtonOk, self.lineEditProjectLocal)
        MenuProjectCloud.setTabOrder(self.lineEditProjectLocal, self.pushButtonLocalBrowse)
        MenuProjectCloud.setTabOrder(self.pushButtonLocalBrowse, self.radioButtonPush)
        MenuProjectCloud.setTabOrder(self.radioButtonPush, self.radioButtonPull)
        MenuProjectCloud.setTabOrder(self.radioButtonPull, self.radioButtonRestore)
        MenuProjectCloud.setTabOrder(self.radioButtonRestore, self.checkBoxFlush)
        MenuProjectCloud.setTabOrder(self.checkBoxFlush, self.checkBoxBackup)

    def retranslateUi(self, MenuProjectCloud):
        MenuProjectCloud.setWindowTitle(QtGui.QApplication.translate("MenuProjectCloud", "Rapuma - Manage Cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPathLocal.setText(QtGui.QApplication.translate("MenuProjectCloud", "Path to Local Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLocalBrowse.setToolTip(QtGui.QApplication.translate("MenuProjectCloud", "Browse to an existing local project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLocalBrowse.setText(QtGui.QApplication.translate("MenuProjectCloud", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setToolTip(QtGui.QApplication.translate("MenuProjectCloud", "Remove a selected project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setText(QtGui.QApplication.translate("MenuProjectCloud", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("MenuProjectCloud", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxAction.setToolTip(QtGui.QApplication.translate("MenuProjectCloud", "Define the action to be taken", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxAction.setTitle(QtGui.QApplication.translate("MenuProjectCloud", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonPush.setToolTip(QtGui.QApplication.translate("MenuProjectCloud", "Update (push to) the cloud with local project data", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonPush.setText(QtGui.QApplication.translate("MenuProjectCloud", "Local to Cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxFlush.setToolTip(QtGui.QApplication.translate("MenuProjectCloud", "Completly replace the cloud version with the local version", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxFlush.setText(QtGui.QApplication.translate("MenuProjectCloud", "Flush", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonPull.setToolTip(QtGui.QApplication.translate("MenuProjectCloud", "Update the local project with data pulled from the cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonPull.setText(QtGui.QApplication.translate("MenuProjectCloud", "Cloud to Local", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxBackup.setToolTip(QtGui.QApplication.translate("MenuProjectCloud", "Create a backup of the project before replacing it with cloud version", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxBackup.setText(QtGui.QApplication.translate("MenuProjectCloud", "Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonRestore.setToolTip(QtGui.QApplication.translate("MenuProjectCloud", "Add a new local project with data from the cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonRestore.setText(QtGui.QApplication.translate("MenuProjectCloud", "Restore From Cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditProjectLocal.setToolTip(QtGui.QApplication.translate("MenuProjectCloud", "Enter the path to the local project", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditProjectLocal.setPlaceholderText(QtGui.QApplication.translate("MenuProjectCloud", "Enter Path", None, QtGui.QApplication.UnicodeUTF8))

