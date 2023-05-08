# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Delete(object):
    def setupUi(self, Delete):
        if not Delete.objectName():
            Delete.setObjectName(u"Delete")
        Delete.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Delete)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.where_clause_label = QLabel(Delete)
        self.where_clause_label.setObjectName(u"where_clause_label")

        self.horizontalLayout_8.addWidget(self.where_clause_label)

        self.where_clause_line_edit = QLineEdit(Delete)
        self.where_clause_line_edit.setObjectName(u"where_clause_line_edit")

        self.horizontalLayout_8.addWidget(self.where_clause_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.delete_button = QPushButton(Delete)
        self.delete_button.setObjectName(u"delete_button")

        self.verticalLayout.addWidget(self.delete_button)


        self.retranslateUi(Delete)

        QMetaObject.connectSlotsByName(Delete)
    # setupUi

    def retranslateUi(self, Delete):
        Delete.setWindowTitle(QCoreApplication.translate("Delete", u"Form", None))
        self.where_clause_label.setText(QCoreApplication.translate("Delete", u"Where:", None))
        self.delete_button.setText(QCoreApplication.translate("Delete", u"DELETE", None))
    # retranslateUi

