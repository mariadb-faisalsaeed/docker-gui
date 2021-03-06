# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName("frmMain")
        frmMain.resize(857, 650)
        self.gridLayout = QtWidgets.QGridLayout(frmMain)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(frmMain)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cbGen = QtWidgets.QCommandLinkButton(frmMain)
        self.cbGen.setObjectName("cbGen")
        self.gridLayout.addWidget(self.cbGen, 4, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(frmMain)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.txtSetupName = QtWidgets.QLineEdit(frmMain)
        self.txtSetupName.setClearButtonEnabled(True)
        self.txtSetupName.setObjectName("txtSetupName")
        self.gridLayout.addWidget(self.txtSetupName, 0, 1, 1, 1)
        self.tab = QtWidgets.QTabWidget(frmMain)
        self.tab.setMinimumSize(QtCore.QSize(0, 49))
        self.tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab.setElideMode(QtCore.Qt.ElideNone)
        self.tab.setDocumentMode(True)
        self.tab.setMovable(True)
        self.tab.setTabBarAutoHide(False)
        self.tab.setObjectName("tab")
        self.tabMariaDB = QtWidgets.QWidget()
        self.tabMariaDB.setObjectName("tabMariaDB")
        self.formLayout = QtWidgets.QFormLayout(self.tabMariaDB)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.tabMariaDB)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.tabMariaDB)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cbServerVersion = QtWidgets.QComboBox(self.tabMariaDB)
        self.cbServerVersion.setObjectName("cbServerVersion")
        self.cbServerVersion.addItem("")
        self.cbServerVersion.addItem("")
        self.cbServerVersion.addItem("")
        self.cbServerVersion.addItem("")
        self.cbServerVersion.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbServerVersion)
        self.txtServerNodes = QtWidgets.QSpinBox(self.tabMariaDB)
        self.txtServerNodes.setMinimum(1)
        self.txtServerNodes.setMaximum(7)
        self.txtServerNodes.setProperty("value", 3)
        self.txtServerNodes.setObjectName("txtServerNodes")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtServerNodes)
        self.ckAcidCompliance = QtWidgets.QCheckBox(self.tabMariaDB)
        self.ckAcidCompliance.setObjectName("ckAcidCompliance")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ckAcidCompliance)
        self.ckEncryption = QtWidgets.QCheckBox(self.tabMariaDB)
        self.ckEncryption.setObjectName("ckEncryption")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ckEncryption)
        self.tab.addTab(self.tabMariaDB, "")
        self.tabMaxScale = QtWidgets.QWidget()
        self.tabMaxScale.setObjectName("tabMaxScale")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tabMaxScale)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.tabMaxScale)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtMaxScaleNodes = QtWidgets.QSpinBox(self.tabMaxScale)
        self.txtMaxScaleNodes.setMinimum(1)
        self.txtMaxScaleNodes.setMaximum(4)
        self.txtMaxScaleNodes.setSingleStep(1)
        self.txtMaxScaleNodes.setProperty("value", 2)
        self.txtMaxScaleNodes.setObjectName("txtMaxScaleNodes")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtMaxScaleNodes)
        self.label_5 = QtWidgets.QLabel(self.tabMaxScale)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cbMaxScaleVersion = QtWidgets.QComboBox(self.tabMaxScale)
        self.cbMaxScaleVersion.setObjectName("cbMaxScaleVersion")
        self.cbMaxScaleVersion.addItem("")
        self.cbMaxScaleVersion.addItem("")
        self.cbMaxScaleVersion.addItem("")
        self.cbMaxScaleVersion.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbMaxScaleVersion)
        self.ckCooperativeMonitoring = QtWidgets.QCheckBox(self.tabMaxScale)
        self.ckCooperativeMonitoring.setChecked(True)
        self.ckCooperativeMonitoring.setObjectName("ckCooperativeMonitoring")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ckCooperativeMonitoring)
        self.ckTransactionReplay = QtWidgets.QCheckBox(self.tabMaxScale)
        self.ckTransactionReplay.setChecked(True)
        self.ckTransactionReplay.setObjectName("ckTransactionReplay")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ckTransactionReplay)
        self.ckCausalReads = QtWidgets.QCheckBox(self.tabMaxScale)
        self.ckCausalReads.setChecked(True)
        self.ckCausalReads.setObjectName("ckCausalReads")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.ckCausalReads)
        self.ckAutoFailover = QtWidgets.QCheckBox(self.tabMaxScale)
        self.ckAutoFailover.setChecked(True)
        self.ckAutoFailover.setObjectName("ckAutoFailover")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.ckAutoFailover)
        self.tab.addTab(self.tabMaxScale, "")
        self.gridLayout.addWidget(self.tab, 1, 0, 1, 2)
        self.txtServerConfig = QtWidgets.QPlainTextEdit(frmMain)
        self.txtServerConfig.setReadOnly(True)
        self.txtServerConfig.setObjectName("txtServerConfig")
        self.gridLayout.addWidget(self.txtServerConfig, 3, 0, 1, 1)
        self.txtMaxScaleConfig = QtWidgets.QPlainTextEdit(frmMain)
        self.txtMaxScaleConfig.setReadOnly(True)
        self.txtMaxScaleConfig.setObjectName("txtMaxScaleConfig")
        self.gridLayout.addWidget(self.txtMaxScaleConfig, 3, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(frmMain)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.retranslateUi(frmMain)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMain)
        frmMain.setTabOrder(self.txtSetupName, self.tab)
        frmMain.setTabOrder(self.tab, self.txtServerNodes)
        frmMain.setTabOrder(self.txtServerNodes, self.cbServerVersion)
        frmMain.setTabOrder(self.cbServerVersion, self.ckAcidCompliance)
        frmMain.setTabOrder(self.ckAcidCompliance, self.ckEncryption)
        frmMain.setTabOrder(self.ckEncryption, self.txtMaxScaleNodes)
        frmMain.setTabOrder(self.txtMaxScaleNodes, self.cbMaxScaleVersion)
        frmMain.setTabOrder(self.cbMaxScaleVersion, self.ckCooperativeMonitoring)
        frmMain.setTabOrder(self.ckCooperativeMonitoring, self.ckTransactionReplay)
        frmMain.setTabOrder(self.ckTransactionReplay, self.ckCausalReads)
        frmMain.setTabOrder(self.ckCausalReads, self.ckAutoFailover)
        frmMain.setTabOrder(self.ckAutoFailover, self.cbGen)

    def retranslateUi(self, frmMain):
        _translate = QtCore.QCoreApplication.translate
        frmMain.setWindowTitle(_translate("frmMain", "Generate MariaDB Docker Setup"))
        self.label.setText(_translate("frmMain", "Name this Setup"))
        self.cbGen.setText(_translate("frmMain", "Generate MariaDB Docker-Compose Scripts"))
        self.label_6.setText(_translate("frmMain", "MariaDB Configuration"))
        self.txtSetupName.setText(_translate("frmMain", "mariadb-ha"))
        self.label_2.setText(_translate("frmMain", "Number of MariaDB Nodes"))
        self.label_3.setText(_translate("frmMain", "MariaDB Version to Use"))
        self.cbServerVersion.setItemText(0, _translate("frmMain", "Latest"))
        self.cbServerVersion.setItemText(1, _translate("frmMain", "MariaDB 10.5"))
        self.cbServerVersion.setItemText(2, _translate("frmMain", "MariaDB 10.4"))
        self.cbServerVersion.setItemText(3, _translate("frmMain", "MariaDB 10.3"))
        self.cbServerVersion.setItemText(4, _translate("frmMain", "MariaDB 10.2"))
        self.txtServerNodes.setToolTip(_translate("frmMain", "Number of MariaDB Nodes, 1 to 7 Server nodes allowed"))
        self.ckAcidCompliance.setToolTip(_translate("frmMain", "Enable binlog, relaylog sync and flush_trx_commit to 1 for maximum durability"))
        self.ckAcidCompliance.setText(_translate("frmMain", "MariaDB ACID Compliance/Durability"))
        self.ckEncryption.setToolTip(_translate("frmMain", "Enable File Key Plugin based Encryption"))
        self.ckEncryption.setText(_translate("frmMain", "MariaDB Encryption at rest - TDE"))
        self.tab.setTabText(self.tab.indexOf(self.tabMariaDB), _translate("frmMain", "MariaDB Configuration"))
        self.label_4.setText(_translate("frmMain", "Number of MaxScale Nodes"))
        self.txtMaxScaleNodes.setToolTip(_translate("frmMain", "Number of MaxScale nodes for HA, 1 to 4 MaxScale allowed"))
        self.label_5.setText(_translate("frmMain", "MaxScale Version to Use"))
        self.cbMaxScaleVersion.setItemText(0, _translate("frmMain", "Latest"))
        self.cbMaxScaleVersion.setItemText(1, _translate("frmMain", "MaxScale 2.5"))
        self.cbMaxScaleVersion.setItemText(2, _translate("frmMain", "MaxScale 2.4"))
        self.cbMaxScaleVersion.setItemText(3, _translate("frmMain", "MaxScale 2.3"))
        self.ckCooperativeMonitoring.setToolTip(_translate("frmMain", "Enable Cooperative Monitoring (MaxScale 2.5 or higher)"))
        self.ckCooperativeMonitoring.setText(_translate("frmMain", "MaxScale Cooperative Monitoring"))
        self.ckTransactionReplay.setToolTip(_translate("frmMain", "Transaction Replay enabled for durability (MaxScale 2.4 or higher)"))
        self.ckTransactionReplay.setText(_translate("frmMain", "Transaction Replay"))
        self.ckCausalReads.setToolTip(_translate("frmMain", "Enable Causal Reads to enforce consistent reads (MaxScale 2.3 or higher)"))
        self.ckCausalReads.setText(_translate("frmMain", "Causal Reads"))
        self.ckAutoFailover.setToolTip(_translate("frmMain", "Enable Automatic Database Failover/Rejoin (MaxScale 2.2 or higher)"))
        self.ckAutoFailover.setText(_translate("frmMain", "Auto Failover"))
        self.tab.setTabText(self.tab.indexOf(self.tabMaxScale), _translate("frmMain", "MaxScale Configuration"))
        self.label_7.setText(_translate("frmMain", "MaxScale Configuration"))
