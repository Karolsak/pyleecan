# -*- coding: utf-8 -*-

# File generated according to SWinding.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .....GUI.Tools.MPLCanvas import MPLCanvas2

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SWinding(object):
    def setupUi(self, SWinding):
        if not SWinding.objectName():
            SWinding.setObjectName(u"SWinding")
        SWinding.resize(1158, 758)
        SWinding.setMinimumSize(QSize(650, 550))
        self.verticalLayout_5 = QVBoxLayout(SWinding)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.w_viewer = MPLCanvas2(SWinding)
        self.w_viewer.setObjectName(u"w_viewer")

        self.horizontalLayout_8.addWidget(self.w_viewer)

        self.in_wind_param = QLabel(SWinding)
        self.in_wind_param.setObjectName(u"in_wind_param")
        self.in_wind_param.setMaximumSize(QSize(400, 16777215))
        self.in_wind_param.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WindParam/Winding param.PNG")
        )

        self.horizontalLayout_8.addWidget(self.in_wind_param)

        self.widget = QWidget(SWinding)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 0))
        self.widget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.g_pattern = QGroupBox(self.widget)
        self.g_pattern.setObjectName(u"g_pattern")
        self.verticalLayout_6 = QVBoxLayout(self.g_pattern)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.c_wind_type = QComboBox(self.g_pattern)
        self.c_wind_type.addItem("")
        self.c_wind_type.addItem("")
        self.c_wind_type.setObjectName(u"c_wind_type")

        self.verticalLayout_6.addWidget(self.c_wind_type)

        self.in_Zs = QLabel(self.g_pattern)
        self.in_Zs.setObjectName(u"in_Zs")

        self.verticalLayout_6.addWidget(self.in_Zs)

        self.in_p = QLabel(self.g_pattern)
        self.in_p.setObjectName(u"in_p")

        self.verticalLayout_6.addWidget(self.in_p)

        self.stack_wind_type = QStackedWidget(self.g_pattern)
        self.stack_wind_type.setObjectName(u"stack_wind_type")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.in_qs = QLabel(self.page)
        self.in_qs.setObjectName(u"in_qs")

        self.gridLayout_2.addWidget(self.in_qs, 0, 0, 1, 1)

        self.si_qs = QSpinBox(self.page)
        self.si_qs.setObjectName(u"si_qs")

        self.gridLayout_2.addWidget(self.si_qs, 0, 1, 1, 1)

        self.in_Nlayer = QLabel(self.page)
        self.in_Nlayer.setObjectName(u"in_Nlayer")

        self.gridLayout_2.addWidget(self.in_Nlayer, 1, 0, 1, 1)

        self.si_Nlayer = QSpinBox(self.page)
        self.si_Nlayer.setObjectName(u"si_Nlayer")
        self.si_Nlayer.setMinimum(1)

        self.gridLayout_2.addWidget(self.si_Nlayer, 1, 1, 1, 1)

        self.in_coil_pitch = QLabel(self.page)
        self.in_coil_pitch.setObjectName(u"in_coil_pitch")

        self.gridLayout_2.addWidget(self.in_coil_pitch, 2, 0, 1, 1)

        self.si_coil_pitch = QSpinBox(self.page)
        self.si_coil_pitch.setObjectName(u"si_coil_pitch")

        self.gridLayout_2.addWidget(self.si_coil_pitch, 2, 1, 1, 1)

        self.stack_wind_type.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.b_import_csv = QPushButton(self.page_2)
        self.b_import_csv.setObjectName(u"b_import_csv")

        self.verticalLayout_7.addWidget(self.b_import_csv)

        self.stack_wind_type.addWidget(self.page_2)

        self.verticalLayout_6.addWidget(self.stack_wind_type)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.in_Nslot = QLabel(self.g_pattern)
        self.in_Nslot.setObjectName(u"in_Nslot")
        self.in_Nslot.setMinimumSize(QSize(0, 0))
        self.in_Nslot.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.in_Nslot)

        self.si_Nslot = QSpinBox(self.g_pattern)
        self.si_Nslot.setObjectName(u"si_Nslot")
        self.si_Nslot.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_4.addWidget(self.si_Nslot)

        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.is_reverse = QCheckBox(self.g_pattern)
        self.is_reverse.setObjectName(u"is_reverse")

        self.verticalLayout_6.addWidget(self.is_reverse)

        self.verticalLayout_2.addWidget(self.g_pattern)

        self.g_circuit = QGroupBox(self.widget)
        self.g_circuit.setObjectName(u"g_circuit")
        self.gridLayout = QGridLayout(self.g_circuit)
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_Ntcoil = QLabel(self.g_circuit)
        self.in_Ntcoil.setObjectName(u"in_Ntcoil")

        self.gridLayout.addWidget(self.in_Ntcoil, 0, 0, 1, 1)

        self.si_Ntcoil = QSpinBox(self.g_circuit)
        self.si_Ntcoil.setObjectName(u"si_Ntcoil")

        self.gridLayout.addWidget(self.si_Ntcoil, 0, 1, 1, 1)

        self.in_Npcp = QLabel(self.g_circuit)
        self.in_Npcp.setObjectName(u"in_Npcp")

        self.gridLayout.addWidget(self.in_Npcp, 1, 0, 1, 1)

        self.si_Npcp = QSpinBox(self.g_circuit)
        self.si_Npcp.setObjectName(u"si_Npcp")
        self.si_Npcp.setMaximum(999999999)
        self.si_Npcp.setValue(12345)

        self.gridLayout.addWidget(self.si_Npcp, 1, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.g_circuit)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.b_edit_wind_mat = QPushButton(self.widget)
        self.b_edit_wind_mat.setObjectName(u"b_edit_wind_mat")

        self.verticalLayout_2.addWidget(self.b_edit_wind_mat)

        self.b_export_csv = QPushButton(self.widget)
        self.b_export_csv.setObjectName(u"b_export_csv")

        self.verticalLayout_2.addWidget(self.b_export_csv)

        self.g_output = QGroupBox(self.widget)
        self.g_output.setObjectName(u"g_output")
        self.g_output.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.g_output)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.out_shape = QLabel(self.g_output)
        self.out_shape.setObjectName(u"out_shape")
        self.out_shape.setMinimumSize(QSize(175, 0))

        self.verticalLayout_3.addWidget(self.out_shape)

        self.out_ms = QLabel(self.g_output)
        self.out_ms.setObjectName(u"out_ms")

        self.verticalLayout_3.addWidget(self.out_ms)

        self.out_Nperw = QLabel(self.g_output)
        self.out_Nperw.setObjectName(u"out_Nperw")

        self.verticalLayout_3.addWidget(self.out_Nperw)

        self.out_Ntspc = QLabel(self.g_output)
        self.out_Ntspc.setObjectName(u"out_Ntspc")

        self.verticalLayout_3.addWidget(self.out_Ntspc)

        self.out_Ncspc = QLabel(self.g_output)
        self.out_Ncspc.setObjectName(u"out_Ncspc")

        self.verticalLayout_3.addWidget(self.out_Ncspc)

        self.verticalLayout_2.addWidget(self.g_output)

        self.horizontalLayout_8.addWidget(self.widget)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.b_preview = QPushButton(SWinding)
        self.b_preview.setObjectName(u"b_preview")

        self.horizontalLayout_3.addWidget(self.b_preview)

        self.b_previous = QPushButton(SWinding)
        self.b_previous.setObjectName(u"b_previous")

        self.horizontalLayout_3.addWidget(self.b_previous)

        self.b_next = QPushButton(SWinding)
        self.b_next.setObjectName(u"b_next")

        self.horizontalLayout_3.addWidget(self.b_next)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SWinding)

        self.stack_wind_type.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(SWinding)

    # setupUi

    def retranslateUi(self, SWinding):
        SWinding.setWindowTitle(QCoreApplication.translate("SWinding", u"Form", None))
        self.in_wind_param.setText("")
        self.g_pattern.setTitle(
            QCoreApplication.translate("SWinding", u"Pattern", None)
        )
        self.c_wind_type.setItemText(
            0, QCoreApplication.translate("SWinding", u"Star of Slot", None)
        )
        self.c_wind_type.setItemText(
            1, QCoreApplication.translate("SWinding", u"User Defined", None)
        )

        self.in_Zs.setText(
            QCoreApplication.translate("SWinding", u"Slot number=123", None)
        )
        self.in_p.setText(
            QCoreApplication.translate("SWinding", u"Pole pair number=32", None)
        )
        self.in_qs.setText(
            QCoreApplication.translate("SWinding", u"Phases number", None)
        )
        self.in_Nlayer.setText(
            QCoreApplication.translate("SWinding", u"Layer number", None)
        )
        self.in_coil_pitch.setText(
            QCoreApplication.translate("SWinding", u"Coil pitch", None)
        )
        self.b_import_csv.setText(
            QCoreApplication.translate("SWinding", u"Import from CSV", None)
        )
        self.in_Nslot.setText(
            QCoreApplication.translate("SWinding", u"Slot shift", None)
        )
        self.is_reverse.setText(
            QCoreApplication.translate("SWinding", u"Reversed winding", None)
        )
        self.g_circuit.setTitle(
            QCoreApplication.translate("SWinding", u"Circuit", None)
        )
        self.in_Ntcoil.setText(
            QCoreApplication.translate("SWinding", u"Turns per coil", None)
        )
        self.in_Npcp.setText(
            QCoreApplication.translate("SWinding", u"Parallel circuits", None)
        )
        self.b_edit_wind_mat.setText(
            QCoreApplication.translate("SWinding", u"Edit Winding Matrix", None)
        )
        self.b_export_csv.setText(
            QCoreApplication.translate("SWinding", u"Export to CSV", None)
        )
        self.g_output.setTitle(QCoreApplication.translate("SWinding", u"Output", None))
        self.out_shape.setText(
            QCoreApplication.translate("SWinding", u"Winding Matrix Shape : ", None)
        )
        self.out_ms.setText(
            QCoreApplication.translate("SWinding", u"ms = Zs / (2*p*qs) = ?", None)
        )
        # if QT_CONFIG(tooltip)
        self.out_Nperw.setToolTip(
            QCoreApplication.translate("SWinding", u"Winding periodicity", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.out_Nperw.setText(QCoreApplication.translate("SWinding", u"Nperw", None))
        # if QT_CONFIG(tooltip)
        self.out_Ntspc.setToolTip(
            QCoreApplication.translate(
                "SWinding", u"Winding number of turns in series per phase", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.out_Ntspc.setStatusTip(
            QCoreApplication.translate(
                "SWinding", u"Winding number of turns in series per phase", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.out_Ntspc.setWhatsThis(
            QCoreApplication.translate(
                "SWinding", u"Winding number of turns in series per phase", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.out_Ntspc.setText(QCoreApplication.translate("SWinding", u"Ntspc: ", None))
        # if QT_CONFIG(tooltip)
        self.out_Ncspc.setToolTip(
            QCoreApplication.translate(
                "SWinding", u"Number of coils in series per parallel circuit", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.out_Ncspc.setStatusTip(
            QCoreApplication.translate(
                "SWinding", u"Number of coils in series per parallel circuit", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.out_Ncspc.setWhatsThis(
            QCoreApplication.translate(
                "SWinding", u"Number of coils in series per parallel circuit", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.out_Ncspc.setText(QCoreApplication.translate("SWinding", u"Ncspc:", None))
        self.b_preview.setText(QCoreApplication.translate("SWinding", u"Preview", None))
        self.b_previous.setText(
            QCoreApplication.translate("SWinding", u"Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SWinding", u"Next", None))

    # retranslateUi