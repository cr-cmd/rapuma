# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lib/rapuma/dialog/menu_manage_new_dlg.ui'
#
# Created: Thu Jan 23 16:34:37 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MenuManageNew(object):
    def setupUi(self, MenuManageNew):
        MenuManageNew.setObjectName("MenuManageNew")
        MenuManageNew.resize(461, 320)
        self.gridLayout = QtGui.QGridLayout(MenuManageNew)
        self.gridLayout.setObjectName("gridLayout")
        self.labelIdentification = QtGui.QLabel(MenuManageNew)
        self.labelIdentification.setObjectName("labelIdentification")
        self.gridLayout.addWidget(self.labelIdentification, 0, 0, 1, 3)
        self.lineEditProjName = QtGui.QLineEdit(MenuManageNew)
        self.lineEditProjName.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditProjName.setObjectName("lineEditProjName")
        self.gridLayout.addWidget(self.lineEditProjName, 5, 0, 1, 5)
        self.lineEditScriptId = QtGui.QLineEdit(MenuManageNew)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditScriptId.sizePolicy().hasHeightForWidth())
        self.lineEditScriptId.setSizePolicy(sizePolicy)
        self.lineEditScriptId.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditScriptId.setMaxLength(4)
        self.lineEditScriptId.setObjectName("lineEditScriptId")
        self.gridLayout.addWidget(self.lineEditScriptId, 1, 2, 1, 1)
        self.labelDescription = QtGui.QLabel(MenuManageNew)
        self.labelDescription.setObjectName("labelDescription")
        self.gridLayout.addWidget(self.labelDescription, 6, 0, 1, 3)
        self.labelPath = QtGui.QLabel(MenuManageNew)
        self.labelPath.setObjectName("labelPath")
        self.gridLayout.addWidget(self.labelPath, 2, 0, 1, 3)
        self.labelDash_1 = QtGui.QLabel(MenuManageNew)
        self.labelDash_1.setObjectName("labelDash_1")
        self.gridLayout.addWidget(self.labelDash_1, 1, 1, 1, 1)
        self.lineEditProjId = QtGui.QLineEdit(MenuManageNew)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditProjId.sizePolicy().hasHeightForWidth())
        self.lineEditProjId.setSizePolicy(sizePolicy)
        self.lineEditProjId.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditProjId.setMaxLength(10)
        self.lineEditProjId.setObjectName("lineEditProjId")
        self.gridLayout.addWidget(self.lineEditProjId, 1, 4, 1, 1)
        self.pushButtonCancel = QtGui.QPushButton(MenuManageNew)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 8, 4, 1, 1)
        self.labelName = QtGui.QLabel(MenuManageNew)
        self.labelName.setObjectName("labelName")
        self.gridLayout.addWidget(self.labelName, 4, 0, 1, 3)
        self.textEditProjDescription = QtGui.QTextEdit(MenuManageNew)
        self.textEditProjDescription.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEditProjDescription.setTabChangesFocus(True)
        self.textEditProjDescription.setObjectName("textEditProjDescription")
        self.gridLayout.addWidget(self.textEditProjDescription, 7, 0, 1, 5)
        self.labelDash_2 = QtGui.QLabel(MenuManageNew)
        self.labelDash_2.setObjectName("labelDash_2")
        self.gridLayout.addWidget(self.labelDash_2, 1, 3, 1, 1)
        self.lineEditLangId = QtGui.QLineEdit(MenuManageNew)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditLangId.sizePolicy().hasHeightForWidth())
        self.lineEditLangId.setSizePolicy(sizePolicy)
        self.lineEditLangId.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditLangId.setWhatsThis("")
        self.lineEditLangId.setMaxLength(3)
        self.lineEditLangId.setObjectName("lineEditLangId")
        self.gridLayout.addWidget(self.lineEditLangId, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 2)
        self.pushButtonOk = QtGui.QPushButton(MenuManageNew)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.gridLayout.addWidget(self.pushButtonOk, 8, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 8, 3, 1, 1)
        self.lineEditProjPath = QtGui.QLineEdit(MenuManageNew)
        self.lineEditProjPath.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditProjPath.setObjectName("lineEditProjPath")
        self.gridLayout.addWidget(self.lineEditProjPath, 3, 0, 1, 4)
        self.pushButtonBrowse = QtGui.QPushButton(MenuManageNew)
        self.pushButtonBrowse.setObjectName("pushButtonBrowse")
        self.gridLayout.addWidget(self.pushButtonBrowse, 3, 4, 1, 1)

        self.retranslateUi(MenuManageNew)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked(bool)"), MenuManageNew.close)
        QtCore.QObject.connect(self.pushButtonOk, QtCore.SIGNAL("clicked()"), MenuManageNew.setupUi)
        QtCore.QObject.connect(self.pushButtonBrowse, QtCore.SIGNAL("clicked()"), MenuManageNew.setupUi)
        QtCore.QMetaObject.connectSlotsByName(MenuManageNew)
        MenuManageNew.setTabOrder(self.pushButtonCancel, self.lineEditLangId)
        MenuManageNew.setTabOrder(self.lineEditLangId, self.lineEditScriptId)
        MenuManageNew.setTabOrder(self.lineEditScriptId, self.lineEditProjId)
        MenuManageNew.setTabOrder(self.lineEditProjId, self.lineEditProjPath)
        MenuManageNew.setTabOrder(self.lineEditProjPath, self.pushButtonBrowse)
        MenuManageNew.setTabOrder(self.pushButtonBrowse, self.lineEditProjName)
        MenuManageNew.setTabOrder(self.lineEditProjName, self.textEditProjDescription)
        MenuManageNew.setTabOrder(self.textEditProjDescription, self.pushButtonOk)

    def retranslateUi(self, MenuManageNew):
        MenuManageNew.setWindowTitle(QtGui.QApplication.translate("MenuManageNew", "Rapuma - New Project", None, QtGui.QApplication.UnicodeUTF8))
        MenuManageNew.setToolTip(QtGui.QApplication.translate("MenuManageNew", "Create a new Rapuma project", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIdentification.setText(QtGui.QApplication.translate("MenuManageNew", "Identification", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditProjName.setToolTip(QtGui.QApplication.translate("MenuManageNew", "Project name, could be book title", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditProjName.setPlaceholderText(QtGui.QApplication.translate("MenuManageNew", "Project Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditScriptId.setToolTip(QtGui.QApplication.translate("MenuManageNew", "ISO 4 letter script code", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditScriptId.setPlaceholderText(QtGui.QApplication.translate("MenuManageNew", "Script", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDescription.setToolTip(QtGui.QApplication.translate("MenuManageNew", "Create a new Rapuma project", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDescription.setText(QtGui.QApplication.translate("MenuManageNew", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPath.setText(QtGui.QApplication.translate("MenuManageNew", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDash_1.setText(QtGui.QApplication.translate("MenuManageNew", "—", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditProjId.setToolTip(QtGui.QApplication.translate("MenuManageNew", "Make up a project identifier code (max 10 letters)", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditProjId.setPlaceholderText(QtGui.QApplication.translate("MenuManageNew", "Project ID", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setToolTip(QtGui.QApplication.translate("MenuManageNew", "Click to cancel project creation", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("MenuManageNew", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelName.setText(QtGui.QApplication.translate("MenuManageNew", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditProjDescription.setToolTip(QtGui.QApplication.translate("MenuManageNew", "Brief project description", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDash_2.setText(QtGui.QApplication.translate("MenuManageNew", "—", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditLangId.setToolTip(QtGui.QApplication.translate("MenuManageNew", "Ethnologue 3 letter language code", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditLangId.setPlaceholderText(QtGui.QApplication.translate("MenuManageNew", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setToolTip(QtGui.QApplication.translate("MenuManageNew", "Click to create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setText(QtGui.QApplication.translate("MenuManageNew", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditProjPath.setToolTip(QtGui.QApplication.translate("MenuManageNew", "Browse to the project path", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditProjPath.setPlaceholderText(QtGui.QApplication.translate("MenuManageNew", "Project Path", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBrowse.setToolTip(QtGui.QApplication.translate("MenuManageNew", "Browse to the project folder", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBrowse.setText(QtGui.QApplication.translate("MenuManageNew", "Browse", None, QtGui.QApplication.UnicodeUTF8))

