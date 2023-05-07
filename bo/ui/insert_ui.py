# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'insert.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_InsertWidget(object):
    def setupUi(self, InsertWidget):
        if not InsertWidget.objectName():
            InsertWidget.setObjectName(u"InsertWidget")
        InsertWidget.resize(470, 377)
        self.verticalLayout_2 = QVBoxLayout(InsertWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.region_label = QLabel(InsertWidget)
        self.region_label.setObjectName(u"region_label")

        self.horizontalLayout.addWidget(self.region_label)

        self.region_line_edit = QLineEdit(InsertWidget)
        self.region_line_edit.setObjectName(u"region_line_edit")

        self.horizontalLayout.addWidget(self.region_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.product_label = QLabel(InsertWidget)
        self.product_label.setObjectName(u"product_label")

        self.horizontalLayout_4.addWidget(self.product_label)

        self.product_line_edit = QLineEdit(InsertWidget)
        self.product_line_edit.setObjectName(u"product_line_edit")

        self.horizontalLayout_4.addWidget(self.product_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qty_label = QLabel(InsertWidget)
        self.qty_label.setObjectName(u"qty_label")

        self.horizontalLayout_2.addWidget(self.qty_label)

        self.qty_line_edit = QLineEdit(InsertWidget)
        self.qty_line_edit.setObjectName(u"qty_line_edit")

        self.horizontalLayout_2.addWidget(self.qty_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cost_label = QLabel(InsertWidget)
        self.cost_label.setObjectName(u"cost_label")

        self.horizontalLayout_5.addWidget(self.cost_label)

        self.cost_line_edit = QLineEdit(InsertWidget)
        self.cost_line_edit.setObjectName(u"cost_line_edit")

        self.horizontalLayout_5.addWidget(self.cost_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.amt_label = QLabel(InsertWidget)
        self.amt_label.setObjectName(u"amt_label")

        self.horizontalLayout_6.addWidget(self.amt_label)

        self.amt_line_edit = QLineEdit(InsertWidget)
        self.amt_line_edit.setObjectName(u"amt_line_edit")

        self.horizontalLayout_6.addWidget(self.amt_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tax_label = QLabel(InsertWidget)
        self.tax_label.setObjectName(u"tax_label")

        self.horizontalLayout_3.addWidget(self.tax_label)

        self.tax_line_edit = QLineEdit(InsertWidget)
        self.tax_line_edit.setObjectName(u"tax_line_edit")

        self.horizontalLayout_3.addWidget(self.tax_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.total_label = QLabel(InsertWidget)
        self.total_label.setObjectName(u"total_label")

        self.horizontalLayout_7.addWidget(self.total_label)

        self.total_line_edit = QLineEdit(InsertWidget)
        self.total_line_edit.setObjectName(u"total_line_edit")

        self.horizontalLayout_7.addWidget(self.total_line_edit)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.insert_button = QPushButton(InsertWidget)
        self.insert_button.setObjectName(u"insert_button")

        self.verticalLayout.addWidget(self.insert_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(InsertWidget)

        QMetaObject.connectSlotsByName(InsertWidget)
    # setupUi

    def retranslateUi(self, InsertWidget):
        InsertWidget.setWindowTitle(QCoreApplication.translate("InsertWidget", u"Form", None))
        self.region_label.setText(QCoreApplication.translate("InsertWidget", u"Region", None))
        self.product_label.setText(QCoreApplication.translate("InsertWidget", u"Product", None))
        self.qty_label.setText(QCoreApplication.translate("InsertWidget", u"Qty", None))
        self.cost_label.setText(QCoreApplication.translate("InsertWidget", u"Cost", None))
        self.amt_label.setText(QCoreApplication.translate("InsertWidget", u"Amt", None))
        self.tax_label.setText(QCoreApplication.translate("InsertWidget", u"Tax", None))
        self.total_label.setText(QCoreApplication.translate("InsertWidget", u"Total", None))
        self.insert_button.setText(QCoreApplication.translate("InsertWidget", u"INSERT", None))
    # retranslateUi

