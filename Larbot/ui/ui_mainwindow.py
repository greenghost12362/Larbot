# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Mar 18 20:28:56 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 538)
        MainWindow.setStyleSheet("f")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.irc_info = QtGui.QWidget()
        self.irc_info.setObjectName("irc_info")
        self.verticalLayout = QtGui.QVBoxLayout(self.irc_info)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.widget = QtGui.QWidget(self.irc_info)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bot_name_label = QtGui.QLabel(self.widget)
        self.bot_name_label.setObjectName("bot_name_label")
        self.horizontalLayout.addWidget(self.bot_name_label)
        self.bot_name_line_edit = QtGui.QLineEdit(self.widget)
        self.bot_name_line_edit.setObjectName("bot_name_line_edit")
        self.horizontalLayout.addWidget(self.bot_name_line_edit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.irc_info)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.bot_oauth_label = QtGui.QLabel(self.widget_2)
        self.bot_oauth_label.setObjectName("bot_oauth_label")
        self.horizontalLayout_5.addWidget(self.bot_oauth_label)
        self.bot_oauth_help_button = QtGui.QToolButton(self.widget_2)
        self.bot_oauth_help_button.setObjectName("bot_oauth_help_button")
        self.horizontalLayout_5.addWidget(self.bot_oauth_help_button)
        self.bot_oauth_line_edit = QtGui.QLineEdit(self.widget_2)
        self.bot_oauth_line_edit.setMinimumSize(QtCore.QSize(300, 0))
        self.bot_oauth_line_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.bot_oauth_line_edit.setObjectName("bot_oauth_line_edit")
        self.horizontalLayout_5.addWidget(self.bot_oauth_line_edit)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtGui.QWidget(self.irc_info)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.channel_label = QtGui.QLabel(self.widget_3)
        self.channel_label.setObjectName("channel_label")
        self.horizontalLayout_6.addWidget(self.channel_label)
        self.channel_line_edit = QtGui.QLineEdit(self.widget_3)
        self.channel_line_edit.setObjectName("channel_line_edit")
        self.horizontalLayout_6.addWidget(self.channel_line_edit)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtGui.QWidget(self.irc_info)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.connect_button = QtGui.QPushButton(self.widget_4)
        self.connect_button.setObjectName("connect_button")
        self.horizontalLayout_7.addWidget(self.connect_button)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.verticalLayout.addWidget(self.widget_4)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.tabWidget.addTab(self.irc_info, "")
        self.bot_info = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot_info.sizePolicy().hasHeightForWidth())
        self.bot_info.setSizePolicy(sizePolicy)
        self.bot_info.setObjectName("bot_info")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.bot_info)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_12 = QtGui.QWidget(self.bot_info)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget_12)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_5 = QtGui.QWidget(self.widget_12)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 155))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 155))
        self.widget_5.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.widget_5.setFont(font)
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_7 = QtGui.QWidget(self.widget_5)
        self.widget_7.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_7.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtGui.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_4.addWidget(self.widget_7)
        self.widget_8 = QtGui.QWidget(self.widget_5)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mii_name_line_edit = QtGui.QLineEdit(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.mii_name_line_edit.setFont(font)
        self.mii_name_line_edit.setAutoFillBackground(False)
        self.mii_name_line_edit.setFrame(False)
        self.mii_name_line_edit.setReadOnly(True)
        self.mii_name_line_edit.setObjectName("mii_name_line_edit")
        self.verticalLayout_4.addWidget(self.mii_name_line_edit)
        self.player_NNID_line_edit = QtGui.QLineEdit(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.player_NNID_line_edit.setFont(font)
        self.player_NNID_line_edit.setAutoFillBackground(False)
        self.player_NNID_line_edit.setFrame(False)
        self.player_NNID_line_edit.setReadOnly(True)
        self.player_NNID_line_edit.setObjectName("player_NNID_line_edit")
        self.verticalLayout_4.addWidget(self.player_NNID_line_edit)
        self.player_name_line_edit = QtGui.QLineEdit(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.player_name_line_edit.setFont(font)
        self.player_name_line_edit.setAutoFillBackground(False)
        self.player_name_line_edit.setFrame(False)
        self.player_name_line_edit.setReadOnly(True)
        self.player_name_line_edit.setObjectName("player_name_line_edit")
        self.verticalLayout_4.addWidget(self.player_name_line_edit)
        self.horizontalLayout_4.addWidget(self.widget_8)
        self.next_button = QtGui.QPushButton(self.widget_5)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout_4.addWidget(self.next_button)
        self.verticalLayout_7.addWidget(self.widget_5)
        self.widget_6 = QtGui.QWidget(self.widget_12)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setBaseSize(QtCore.QSize(0, 0))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_13 = QtGui.QWidget(self.widget_6)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_13)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtGui.QListWidget(self.widget_13)
        self.listWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.reset_line_button = QtGui.QPushButton(self.widget_13)
        self.reset_line_button.setObjectName("reset_line_button")
        self.verticalLayout_2.addWidget(self.reset_line_button)
        self.horizontalLayout_2.addWidget(self.widget_13)
        self.widget_10 = QtGui.QWidget(self.widget_6)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget_10)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_9 = QtGui.QWidget(self.widget_10)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.open_line_checkbox = QtGui.QCheckBox(self.widget_9)
        self.open_line_checkbox.setObjectName("open_line_checkbox")
        self.horizontalLayout_3.addWidget(self.open_line_checkbox)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.label_4 = QtGui.QLabel(self.widget_9)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.entrants_cap_spinbox = QtGui.QSpinBox(self.widget_9)
        self.entrants_cap_spinbox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.entrants_cap_spinbox.setObjectName("entrants_cap_spinbox")
        self.horizontalLayout_3.addWidget(self.entrants_cap_spinbox)
        self.verticalLayout_6.addWidget(self.widget_9)
        self.widget_11 = QtGui.QWidget(self.widget_10)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.widget_11)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.subscriber_checkbox = QtGui.QCheckBox(self.widget_11)
        self.subscriber_checkbox.setObjectName("subscriber_checkbox")
        self.horizontalLayout_10.addWidget(self.subscriber_checkbox)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.verticalLayout_6.addWidget(self.widget_11)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem12)
        self.horizontalLayout_2.addWidget(self.widget_10)
        self.verticalLayout_7.addWidget(self.widget_6)
        self.horizontalLayout_9.addWidget(self.widget_12)
        spacerItem13 = QtGui.QSpacerItem(600, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.tabWidget.addTab(self.bot_info, "")
        self.horizontalLayout_8.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.statusbar.setToolTip("")
        self.statusbar.setAutoFillBackground(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionNoLogin = QtGui.QAction(MainWindow)
        self.actionNoLogin.setObjectName("actionNoLogin")
        self.menuFile.addAction(self.actionClose)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Larbot - Simple Smash Bot", None, QtGui.QApplication.UnicodeUTF8))
        self.irc_info.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>IRC Info</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.irc_info.setWhatsThis(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>IRC Info</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.bot_name_label.setText(QtGui.QApplication.translate("MainWindow", "Bot Twitch Name", None, QtGui.QApplication.UnicodeUTF8))
        self.bot_oauth_label.setText(QtGui.QApplication.translate("MainWindow", "Bot Twitch OAuth Token", None, QtGui.QApplication.UnicodeUTF8))
        self.bot_oauth_help_button.setText(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.channel_label.setText(QtGui.QApplication.translate("MainWindow", "Channel to join", None, QtGui.QApplication.UnicodeUTF8))
        self.connect_button.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.irc_info), QtGui.QApplication.translate("MainWindow", "IRC Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Now playing:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "NNID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Mii Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.next_button.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_line_button.setText(QtGui.QApplication.translate("MainWindow", "Reset List (Cannot be cancelled!)", None, QtGui.QApplication.UnicodeUTF8))
        self.open_line_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Open line", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Line entrants cap (0 for no cap):", None, QtGui.QApplication.UnicodeUTF8))
        self.subscriber_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Subscriber only (doesn\'t work for now)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bot_info), QtGui.QApplication.translate("MainWindow", "Bot Info", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.statusbar.setStatusTip(QtGui.QApplication.translate("MainWindow", "Not connected", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNoLogin.setText(QtGui.QApplication.translate("MainWindow", "NoLogin", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNoLogin.setToolTip(QtGui.QApplication.translate("MainWindow", "NoLogin", None, QtGui.QApplication.UnicodeUTF8))

