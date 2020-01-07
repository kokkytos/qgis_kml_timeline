# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_2kml_dialog_base.ui'
#
# Created: Sun Mar  8 23:52:17 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_export2kmlDialogBase(object):
    def setupUi(self, export2kmlDialogBase):
        export2kmlDialogBase.setObjectName(_fromUtf8("export2kmlDialogBase"))
        export2kmlDialogBase.resize(288, 96)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/export2kml/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        export2kmlDialogBase.setWindowIcon(icon)
        self.formLayout = QtGui.QFormLayout(export2kmlDialogBase)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(export2kmlDialogBase)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox_timestamp = QtGui.QComboBox(export2kmlDialogBase)
        self.comboBox_timestamp.setObjectName(_fromUtf8("comboBox_timestamp"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_timestamp)
        self.label_2 = QtGui.QLabel(export2kmlDialogBase)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox_altitude = QtGui.QComboBox(export2kmlDialogBase)
        self.comboBox_altitude.setObjectName(_fromUtf8("comboBox_altitude"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_altitude)
        self.button_box = QtGui.QDialogButtonBox(export2kmlDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.button_box)

        self.retranslateUi(export2kmlDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), export2kmlDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), export2kmlDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(export2kmlDialogBase)

    def retranslateUi(self, export2kmlDialogBase):
        export2kmlDialogBase.setWindowTitle(_translate("export2kmlDialogBase", "Εξαγωγή σε kml", None))
        self.label.setText(_translate("export2kmlDialogBase", "<html><head/><body><p>Πεδίο Timestamp</p></body></html>", None))
        self.label_2.setText(_translate("export2kmlDialogBase", "<html><head/><body><p>Πεδίο Υψομέτρου</p></body></html>", None))

