# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dennis/Projects/rapuma/lib/rapuma/dialog/menu_project_backup_dlg.ui'
#
# Created: Tue Feb 25 20:05:58 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MenuProjectBackupRestore(object):
    def setupUi(self, MenuProjectBackupRestore):
        MenuProjectBackupRestore.setObjectName("MenuProjectBackupRestore")
        MenuProjectBackupRestore.resize(370, 412)
        self.gridLayout_2 = QtGui.QGridLayout(MenuProjectBackupRestore)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBoxBackupAction = QtGui.QGroupBox(MenuProjectBackupRestore)
        self.groupBoxBackupAction.setTitle("")
        self.groupBoxBackupAction.setObjectName("groupBoxBackupAction")
        self.gridLayout = QtGui.QGridLayout(self.groupBoxBackupAction)
        self.gridLayout.setObjectName("gridLayout")
        self.labelNeLocation = QtGui.QLabel(self.groupBoxBackupAction)
        self.labelNeLocation.setEnabled(False)
        self.labelNeLocation.setObjectName("labelNeLocation")
        self.gridLayout.addWidget(self.labelNeLocation, 11, 0, 1, 1)
        self.radioButtonRemove = QtGui.QRadioButton(self.groupBoxBackupAction)
        self.radioButtonRemove.setObjectName("radioButtonRemove")
        self.gridLayout.addWidget(self.radioButtonRemove, 8, 0, 1, 1)
        self.radioButtonRestoreNew = QtGui.QRadioButton(self.groupBoxBackupAction)
        self.radioButtonRestoreNew.setObjectName("radioButtonRestoreNew")
        self.gridLayout.addWidget(self.radioButtonRestoreNew, 10, 0, 1, 1)
        self.lineEditProjectLocation = QtGui.QLineEdit(self.groupBoxBackupAction)
        self.lineEditProjectLocation.setEnabled(False)
        self.lineEditProjectLocation.setObjectName("lineEditProjectLocation")
        self.gridLayout.addWidget(self.lineEditProjectLocation, 12, 0, 1, 2)
        self.pushButtonBrowseProjectLocation = QtGui.QPushButton(self.groupBoxBackupAction)
        self.pushButtonBrowseProjectLocation.setEnabled(False)
        self.pushButtonBrowseProjectLocation.setObjectName("pushButtonBrowseProjectLocation")
        self.gridLayout.addWidget(self.pushButtonBrowseProjectLocation, 12, 2, 1, 1)
        self.pushButtonBrowseBackupFile = QtGui.QPushButton(self.groupBoxBackupAction)
        self.pushButtonBrowseBackupFile.setEnabled(False)
        self.pushButtonBrowseBackupFile.setObjectName("pushButtonBrowseBackupFile")
        self.gridLayout.addWidget(self.pushButtonBrowseBackupFile, 14, 2, 1, 1)
        self.labelSelectBackup = QtGui.QLabel(self.groupBoxBackupAction)
        self.labelSelectBackup.setObjectName("labelSelectBackup")
        self.gridLayout.addWidget(self.labelSelectBackup, 4, 0, 1, 1)
        self.labelBackupFile = QtGui.QLabel(self.groupBoxBackupAction)
        self.labelBackupFile.setEnabled(False)
        self.labelBackupFile.setObjectName("labelBackupFile")
        self.gridLayout.addWidget(self.labelBackupFile, 13, 0, 1, 1)
        self.lineEditBackupFile = QtGui.QLineEdit(self.groupBoxBackupAction)
        self.lineEditBackupFile.setEnabled(False)
        self.lineEditBackupFile.setObjectName("lineEditBackupFile")
        self.gridLayout.addWidget(self.lineEditBackupFile, 14, 0, 1, 2)
        self.checkBoxCustomBackupLocation = QtGui.QCheckBox(self.groupBoxBackupAction)
        self.checkBoxCustomBackupLocation.setEnabled(False)
        self.checkBoxCustomBackupLocation.setChecked(False)
        self.checkBoxCustomBackupLocation.setObjectName("checkBoxCustomBackupLocation")
        self.gridLayout.addWidget(self.checkBoxCustomBackupLocation, 10, 1, 1, 1)
        self.labelSelectAction = QtGui.QLabel(self.groupBoxBackupAction)
        self.labelSelectAction.setObjectName("labelSelectAction")
        self.gridLayout.addWidget(self.labelSelectAction, 6, 0, 1, 1)
        self.labelSelectProject = QtGui.QLabel(self.groupBoxBackupAction)
        self.labelSelectProject.setObjectName("labelSelectProject")
        self.gridLayout.addWidget(self.labelSelectProject, 1, 0, 1, 1)
        self.comboBoxSelectBackup = QtGui.QComboBox(self.groupBoxBackupAction)
        self.comboBoxSelectBackup.setObjectName("comboBoxSelectBackup")
        self.gridLayout.addWidget(self.comboBoxSelectBackup, 5, 0, 1, 3)
        self.comboBoxSelectProject = QtGui.QComboBox(self.groupBoxBackupAction)
        self.comboBoxSelectProject.setObjectName("comboBoxSelectProject")
        self.gridLayout.addWidget(self.comboBoxSelectProject, 3, 0, 1, 3)
        self.radioButtonRestore = QtGui.QRadioButton(self.groupBoxBackupAction)
        self.radioButtonRestore.setChecked(True)
        self.radioButtonRestore.setObjectName("radioButtonRestore")
        self.gridLayout.addWidget(self.radioButtonRestore, 7, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBoxBackupAction, 0, 0, 1, 4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButtonOk = QtGui.QPushButton(MenuProjectBackupRestore)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.gridLayout_2.addWidget(self.pushButtonOk, 1, 1, 1, 1)
        self.pushButtonCancel = QtGui.QPushButton(MenuProjectBackupRestore)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout_2.addWidget(self.pushButtonCancel, 1, 2, 1, 1)

        self.retranslateUi(MenuProjectBackupRestore)
        self.comboBoxSelectProject.setCurrentIndex(-1)
        QtCore.QObject.connect(self.radioButtonRestoreNew, QtCore.SIGNAL("toggled(bool)"), self.labelNeLocation.setEnabled)
        QtCore.QObject.connect(self.radioButtonRestoreNew, QtCore.SIGNAL("toggled(bool)"), self.lineEditProjectLocation.setEnabled)
        QtCore.QObject.connect(self.radioButtonRestoreNew, QtCore.SIGNAL("toggled(bool)"), self.pushButtonBrowseProjectLocation.setEnabled)
        QtCore.QObject.connect(self.radioButtonRestoreNew, QtCore.SIGNAL("toggled(bool)"), self.checkBoxCustomBackupLocation.setEnabled)
        QtCore.QObject.connect(self.checkBoxCustomBackupLocation, QtCore.SIGNAL("toggled(bool)"), self.labelBackupFile.setEnabled)
        QtCore.QObject.connect(self.checkBoxCustomBackupLocation, QtCore.SIGNAL("toggled(bool)"), self.lineEditBackupFile.setEnabled)
        QtCore.QObject.connect(self.checkBoxCustomBackupLocation, QtCore.SIGNAL("toggled(bool)"), self.pushButtonBrowseBackupFile.setEnabled)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"), MenuProjectBackupRestore.close)
        QtCore.QObject.connect(self.pushButtonOk, QtCore.SIGNAL("clicked()"), MenuProjectBackupRestore.setupUi)
        QtCore.QObject.connect(self.pushButtonBrowseProjectLocation, QtCore.SIGNAL("clicked()"), MenuProjectBackupRestore.setupUi)
        QtCore.QObject.connect(self.pushButtonBrowseBackupFile, QtCore.SIGNAL("clicked()"), MenuProjectBackupRestore.setupUi)
        QtCore.QMetaObject.connectSlotsByName(MenuProjectBackupRestore)
        MenuProjectBackupRestore.setTabOrder(self.pushButtonOk, self.pushButtonCancel)
        MenuProjectBackupRestore.setTabOrder(self.pushButtonCancel, self.comboBoxSelectProject)
        MenuProjectBackupRestore.setTabOrder(self.comboBoxSelectProject, self.comboBoxSelectBackup)
        MenuProjectBackupRestore.setTabOrder(self.comboBoxSelectBackup, self.radioButtonRestore)
        MenuProjectBackupRestore.setTabOrder(self.radioButtonRestore, self.radioButtonRemove)
        MenuProjectBackupRestore.setTabOrder(self.radioButtonRemove, self.radioButtonRestoreNew)
        MenuProjectBackupRestore.setTabOrder(self.radioButtonRestoreNew, self.checkBoxCustomBackupLocation)
        MenuProjectBackupRestore.setTabOrder(self.checkBoxCustomBackupLocation, self.lineEditProjectLocation)
        MenuProjectBackupRestore.setTabOrder(self.lineEditProjectLocation, self.pushButtonBrowseProjectLocation)
        MenuProjectBackupRestore.setTabOrder(self.pushButtonBrowseProjectLocation, self.lineEditBackupFile)
        MenuProjectBackupRestore.setTabOrder(self.lineEditBackupFile, self.pushButtonBrowseBackupFile)

    def retranslateUi(self, MenuProjectBackupRestore):
        MenuProjectBackupRestore.setWindowTitle(QtGui.QApplication.translate("MenuProjectBackupRestore", "Rapuma - Manage Backups", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxBackupAction.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Define the action to be taken", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNeLocation.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "New Location (Folder)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonRemove.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Update the local project with data pulled from the cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonRemove.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "Remove Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonRestoreNew.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Add a new local project with data from the cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonRestoreNew.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "Restore As New", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditProjectLocation.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Path to a location to restore a backup to", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBrowseProjectLocation.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Browse to a location to restore a backup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBrowseProjectLocation.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBrowseBackupFile.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Browse to backup file you wish to restore", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBrowseBackupFile.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSelectBackup.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "Select Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBackupFile.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "Backup File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditBackupFile.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Path to a backup file", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCustomBackupLocation.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Restore a backup from outside the system", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCustomBackupLocation.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "Custom", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSelectAction.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "Select Action", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSelectProject.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "Select Project", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxSelectBackup.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Select a backup to restore", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxSelectProject.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Select project to restore a backup to", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonRestore.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Update (push to) the cloud with local project data", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonRestore.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "Restore Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Manage a backup operation", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setToolTip(QtGui.QApplication.translate("MenuProjectBackupRestore", "Cancel this operation", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("MenuProjectBackupRestore", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

