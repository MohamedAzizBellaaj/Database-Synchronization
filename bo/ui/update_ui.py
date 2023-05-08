# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Update(object):
    def setupUi(self, Update):
        if not Update.objectName():
            Update.setObjectName(u"Update")
        Update.resize(400, 300)
        self.verticalLayout_3 = QVBoxLayout(Update)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.region_label = QLabel(Update)
        self.region_label.setObjectName(u"region_label")

        self.horizontalLayout.addWidget(self.region_label)

        self.region_line_edit = QLineEdit(Update)
        self.region_line_edit.setObjectName(u"region_line_edit")

        self.horizontalLayout.addWidget(self.region_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.product_label = QLabel(Update)
        self.product_label.setObjectName(u"product_label")

        self.horizontalLayout_4.addWidget(self.product_label)

        self.product_line_edit = QLineEdit(Update)
        self.product_line_edit.setObjectName(u"product_line_edit")

        self.horizontalLayout_4.addWidget(self.product_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qty_label = QLabel(Update)
        self.qty_label.setObjectName(u"qty_label")

        self.horizontalLayout_2.addWidget(self.qty_label)

        self.qty_line_edit = QLineEdit(Update)
        self.qty_line_edit.setObjectName(u"qty_line_edit")

        self.horizontalLayout_2.addWidget(self.qty_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cost_label = QLabel(Update)
        self.cost_label.setObjectName(u"cost_label")

        self.horizontalLayout_5.addWidget(self.cost_label)

        self.cost_line_edit = QLineEdit(Update)
        self.cost_line_edit.setObjectName(u"cost_line_edit")

        self.horizontalLayout_5.addWidget(self.cost_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.amt_label = QLabel(Update)
        self.amt_label.setObjectName(u"amt_label")

        self.horizontalLayout_6.addWidget(self.amt_label)

        self.amt_line_edit = QLineEdit(Update)
        self.amt_line_edit.setObjectName(u"amt_line_edit")

        self.horizontalLayout_6.addWidget(self.amt_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tax_label = QLabel(Update)
        self.tax_label.setObjectName(u"tax_label")

        self.horizontalLayout_3.addWidget(self.tax_label)

        self.tax_line_edit = QLineEdit(Update)
        self.tax_line_edit.setObjectName(u"tax_line_edit")

        self.horizontalLayout_3.addWidget(self.tax_line_edit)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.total_label = QLabel(Update)
        self.total_label.setObjectName(u"total_label")

        self.horizontalLayout_7.addWidget(self.total_label)

        self.total_line_edit = QLineEdit(Update)
        self.total_line_edit.setObjectName(u"total_line_edit")

        self.horizontalLayout_7.addWidget(self.total_line_edit)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.where_clause_label = QLabel(Update)
        self.where_clause_label.setObjectName(u"where_clause_label")

        self.horizontalLayout_8.addWidget(self.where_clause_label)

        self.where_clause_line_edit = QLineEdit(Update)
        self.where_clause_line_edit.setObjectName(u"where_clause_line_edit")

        self.horizontalLayout_8.addWidget(self.where_clause_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.update_button = QPushButton(Update)
        self.update_button.setObjectName(u"update_button")

        self.verticalLayout_2.addWidget(self.update_button)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Update)

        QMetaObject.connectSlotsByName(Update)
    # setupUi

    def retranslateUi(self, Update):
        Update.setWindowTitle(QCoreApplication.translate("Update", u"Form", None))
        self.region_label.setText(QCoreApplication.translate("Update", u"Region", None))
        self.product_label.setText(QCoreApplication.translate("Update", u"Product", None))
        self.qty_label.setText(QCoreApplication.translate("Update", u"Qty", None))
        self.cost_label.setText(QCoreApplication.translate("Update", u"Cost", None))
        self.amt_label.setText(QCoreApplication.translate("Update", u"Amt", None))
        self.tax_label.setText(QCoreApplication.translate("Update", u"Tax", None))
        self.total_label.setText(QCoreApplication.translate("Update", u"Total", None))
        self.where_clause_label.setText(QCoreApplication.translate("Update", u"Where:", None))
        self.update_button.setText(QCoreApplication.translate("Update", u"UPDATE", None))
    # retranslateUi

