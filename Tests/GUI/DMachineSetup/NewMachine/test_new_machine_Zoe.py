import sys
from os.path import isdir, isfile, join
from shutil import rmtree

from PySide2 import QtWidgets
import mock
import pytest
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.Shaft import Shaft
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMachineSetup.SLamShape.SLamShape import SLamShape
from pyleecan.GUI.Dialog.DMachineSetup.SMachineDimension.SMachineDimension import (
    SMachineDimension,
)
from pyleecan.GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.SWPole import SWPole
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.PWSlot60.PWSlot60 import PWSlot60
from pyleecan.GUI.Dialog.DMachineSetup.SSimu.SSimu import SSimu
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.SWindCond import SWindCond
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType11.PCondType11 import PCondType11
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType12.PCondType12 import PCondType12
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.CondType12 import CondType12
from pyleecan.GUI.Dialog.DMachineSetup.SWinding.SWinding import SWinding
from pyleecan.GUI.Dialog.DMachineSetup.SPreview.SPreview import SPreview
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.SWSlot import SWSlot
from pyleecan.GUI.Dialog.DMachineSetup.SSkew.SSkew import SSkew

from Tests.GUI import gui_option  # Set unit as [m]

from pyleecan.Functions.load import load_matlib
from Tests import save_gui_path as save_path

from pyleecan.definitions import DATA_DIR

import logging

mpl_logger = logging.getLogger("matplotlib")
mpl_logger.setLevel(logging.WARNING)

matlib_path = join(DATA_DIR, "Material")


class TestNewMachineZoe(object):
    """Test that you can create the Renault Zoé"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test NewMachineZoe")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""
        # MatLib widget
        material_dict = load_matlib(matlib_path=matlib_path)
        self.widget = DMachineSetup(
            material_dict=material_dict, machine_path=join(DATA_DIR, "Machine")
        )

    @pytest.mark.IPMSM
    def test_Zoe(self):
        """Create a new machine"""
        # Load data for readibility
        self.widget.nav_step.count() == 12

        ################
        # 1 Machine Type
        ## Initial state
        assert self.widget.machine.rotor.is_internal is True
        assert self.widget.machine.name is None
        assert self.widget.machine.stator.winding.p is None
        assert self.widget.nav_step.currentRow() == 0
        assert self.widget.nav_step.currentItem().text() == " 1: Machine Type"
        assert isinstance(self.widget.w_step, SMachineType)
        assert self.widget.w_step.c_type.currentText() == "SCIM"
        ## Definition
        index_WRSM = self.widget.w_step.c_type.findText("WRSM")
        self.widget.w_step.c_type.setCurrentIndex(index_WRSM)
        assert self.widget.w_step.c_type.currentText() == "WRSM"
        self.widget.w_step.le_name.setText("Zoe_Test")
        self.widget.w_step.le_name.editingFinished.emit()
        self.widget.w_step.si_p.setValue(2)
        self.widget.w_step.si_p.editingFinished.emit()
        assert self.widget.w_step.si_p.value() == 2
        ## Check modif
        assert isinstance(self.widget.machine, MachineWRSM)
        assert self.widget.machine.name == "Zoe_Test"
        assert self.widget.machine.stator.winding.p == 2

        #####################
        # 2 Machine Dimension
        self.widget.w_step.b_next.clicked.emit()
        ## Initial state
        assert self.widget.nav_step.currentRow() == 1
        assert self.widget.nav_step.currentItem().text() == " 2: Machine Dimensions"
        assert isinstance(self.widget.w_step, SMachineDimension)
        assert self.widget.machine.stator.Rint is None
        assert self.widget.machine.stator.Rext is None
        assert self.widget.machine.rotor.Rint == 0
        assert self.widget.machine.rotor.Rext is None
        assert self.widget.machine.shaft is None
        assert self.widget.machine.frame is None
        assert not self.widget.w_step.lf_RRint.isEnabled()
        assert not self.widget.w_step.g_frame.isChecked()
        assert not self.widget.w_step.g_shaft.isChecked()
        ## Definition
        self.widget.w_step.lf_SRext.setText("0.13")
        self.widget.w_step.lf_SRext.editingFinished.emit()
        self.widget.w_step.lf_SRint.setText("0.0845")
        self.widget.w_step.lf_SRint.editingFinished.emit()
        self.widget.w_step.lf_RRext.setText("0.0837")
        self.widget.w_step.lf_RRext.editingFinished.emit()
        self.widget.w_step.g_shaft.setChecked(True)
        assert self.widget.w_step.lf_RRint.isEnabled()
        self.widget.w_step.lf_RRint.setText("0.0125")
        self.widget.w_step.lf_RRint.editingFinished.emit()
        ## Check modif
        assert self.widget.machine.stator.Rext == pytest.approx(0.13)
        assert self.widget.machine.stator.Rint == pytest.approx(0.0845)
        assert self.widget.machine.rotor.Rext == pytest.approx(0.0837)
        assert self.widget.machine.rotor.Rint == pytest.approx(0.0125)
        assert self.widget.w_step.out_Drsh.text() == "Drsh = 0.025 [m]"
        assert self.widget.w_step.out_airgap.text() == "Airgap magnetic width = 0.8 [mm]"
        assert isinstance(self.widget.machine.shaft, Shaft)
        assert self.widget.machine.frame is None

        #####################
        # 3 Stator Slot
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 3: Stator Slot"
        assert isinstance(self.widget.w_step, SWSlot)

        self.widget.w_step.si_Zs.setValue(48)
        self.widget.w_step.si_Zs.editingFinished.emit()
        index_slot28 = self.widget.w_step.c_slot_type.findText("Slot Type 28")
        self.widget.w_step.c_slot_type.setCurrentIndex(index_slot28)
        self.widget.w_step.w_slot.lf_W0.setValue(0.0045)
        self.widget.w_step.w_slot.lf_W0.editingFinished.emit()
        self.widget.w_step.w_slot.lf_W3.setValue(0.006)
        self.widget.w_step.w_slot.lf_W3.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H0.setValue(0.001)
        self.widget.w_step.w_slot.lf_H0.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H3.setValue(0.02)
        self.widget.w_step.w_slot.lf_H3.editingFinished.emit()
        self.widget.w_step.w_slot.lf_R1.setValue(0.002)
        self.widget.w_step.w_slot.lf_R1.editingFinished.emit()
        ## Check modif
        self.widget.w_step.b_plot.clicked.emit()
        assert self.widget.w_step.machine.stator.slot.W0 == pytest.approx(0.0045)
        assert self.widget.w_step.machine.stator.slot.W3 == pytest.approx(0.006)
        assert self.widget.w_step.machine.stator.slot.H0 == pytest.approx(0.001)
        assert self.widget.w_step.machine.stator.slot.H3 == pytest.approx(0.02)
        assert self.widget.w_step.machine.stator.slot.R1 == pytest.approx(0.002)
        assert self.widget.w_step.out_Slot_pitch.text() == "Slot pitch = 360 / Zs = 7.5 [°] (0.1309 [rad])"
        assert (
            self.widget.w_step.w_slot.w_out.out_Wlam.text() == "Stator width: 0.0455 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_slot_height.text() == "Slot height: 0.026 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_yoke_height.text() == "Yoke height: 0.0195 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_wind_surface.text()
            == "Active surface: 0.0001629 [m²]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_tot_surface.text()
            == "Slot surface: 0.0001673 [m²]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_op_angle.text()
            == "Opening angle: 0.05326 [rad]"
        )

        #####################
        # 4 Stator Lamination
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 4: Stator Lamination"
        assert isinstance(self.widget.w_step, SLamShape)

        assert self.widget.w_step.lf_L1.value() is None
        assert self.widget.w_step.lf_Kf1.value() == 0.95

        assert not self.widget.w_step.g_axial.isChecked()
        assert not self.widget.w_step.g_radial.isChecked()
        assert not self.widget.w_step.g_notches.isChecked()

        self.widget.w_step.lf_L1.setValue(0.17)
        self.widget.w_step.lf_L1.editingFinished.emit()

        assert self.widget.w_step.lf_L1.value() == 0.17
        # ? -> Because Radial cooling duct hasn't been activated once
        assert self.widget.w_step.out_length.text() == "Stator total length = ?"

        assert self.widget.w_step.machine.stator.L1 == 0.17
        assert self.widget.w_step.machine.stator.Kf1 == 0.95

        #####################
        # 5 Stator Winding
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 5: Stator Winding"
        assert isinstance(self.widget.w_step, SWinding)

        assert self.widget.w_step.c_wind_type.currentText() == "Star of Slot"
        assert self.widget.w_step.in_Zs.text() == "Slot number=48"
        assert self.widget.w_step.in_p.text() == "Pole pair number=2"
        assert self.widget.w_step.si_qs.value() == 3
        assert self.widget.w_step.si_Nlayer.value() == 1
        assert self.widget.w_step.si_coil_pitch.value() == 12
        assert self.widget.w_step.si_Ntcoil.value() == 1
        assert self.widget.w_step.si_Npcp.value() == 1
        assert self.widget.w_step.si_Nslot.value() == 0
        assert not self.widget.w_step.is_reverse.isChecked()
        assert not self.widget.w_step.is_permute_B_C.isChecked()
        assert not self.widget.w_step.is_reverse_layer.isChecked()
        assert not self.widget.w_step.is_change_layer.isChecked()

        self.widget.w_step.si_Nlayer.setValue(2)
        self.widget.w_step.si_Nlayer.editingFinished.emit()
        self.widget.w_step.si_coil_pitch.setValue(10)
        self.widget.w_step.si_coil_pitch.editingFinished.emit()
        self.widget.w_step.si_Ntcoil.setValue(10)
        self.widget.w_step.si_Ntcoil.editingFinished.emit()
        self.widget.w_step.si_Npcp.setValue(4)
        self.widget.w_step.si_Npcp.editingFinished.emit()

        self.widget.w_step.b_generate.clicked.emit()

        assert self.widget.w_step.si_Nlayer.value() == 2
        assert self.widget.w_step.si_coil_pitch.value() == 10
        assert self.widget.w_step.si_Ntcoil.value() == 10
        assert self.widget.w_step.si_Npcp.value() == 4
        # TODO BUG find why the Rotation direction does not setup as a CCW rotation (In an imported Zoé, it does.)
        assert self.widget.w_step.out_rot_dir.text() == "Rotation direction: ?"
        assert self.widget.w_step.out_ms.text() == "Number of slots/pole/phase: 4.0"
        assert self.widget.w_step.out_Nperw.text() == "Winding periodicity: 4"
        assert self.widget.w_step.out_Ntspc.text() == "Number of turns Ntspc: 40"
        assert self.widget.w_step.out_Ncspc.text() == "Number of coils Ncspc: 4"

        # Is the stator winding well defined ?
        assert self.widget.w_step.machine.stator.winding.qs == 3
        assert self.widget.w_step.machine.stator.winding.Nlayer == 2
        assert self.widget.w_step.machine.stator.winding.coil_pitch == 10
        assert self.widget.w_step.machine.stator.winding.Ntcoil == 10
        assert self.widget.w_step.machine.stator.winding.Npcp == 4
        assert self.widget.w_step.machine.stator.winding.Nslot_shift_wind == 0
        assert not self.widget.w_step.machine.stator.winding.is_reverse_wind
        assert not self.widget.w_step.machine.stator.winding.is_permute_B_C
        assert not self.widget.w_step.machine.rotor.winding.is_reverse_layer
        assert not self.widget.w_step.machine.rotor.winding.is_change_layer

        #####################
        # 6 Stator Conductor
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 6: Stator Conductor"
        assert isinstance(self.widget.w_step, SWindCond)

        # Initial state
        assert self.widget.w_step.c_cond_type.currentText() == "Preformed Rectangular"
        assert self.widget.w_step.w_mat_0.c_mat_type.currentText() == "Copper1"
        assert self.widget.w_step.w_mat_1.c_mat_type.currentText() == "Insulator1"
        assert isinstance(self.widget.w_step.w_cond, PCondType11)
        assert not self.widget.w_step.w_cond.g_ins.isChecked()
        assert self.widget.w_step.w_cond.si_Nwpc1_rad.value() == 1
        assert self.widget.w_step.w_cond.si_Nwpc1_tan.value() == 1
        assert self.widget.w_step.w_cond.lf_Wwire.value() is None
        assert self.widget.w_step.w_cond.lf_Hwire.value() is None
        assert self.widget.w_step.w_cond.lf_Lewout.value() == 0

        assert isinstance(self.widget.w_step.machine.stator.winding.conductor, CondType11)

        self.widget.w_step.c_cond_type.setCurrentIndex(1)

        assert self.widget.w_step.c_cond_type.currentText() == "Random Round Wire"
        assert self.widget.w_step.w_mat_0.c_mat_type.currentText() == "Copper1"
        assert self.widget.w_step.w_mat_1.c_mat_type.currentText() == "Insulator1"
        assert isinstance(self.widget.w_step.w_cond, PCondType12)
        assert not self.widget.w_step.w_cond.g_ins.isChecked()
        assert self.widget.w_step.w_cond.si_Nwpc1.value() == 1
        assert self.widget.w_step.w_cond.lf_Wwire.value() is None
        assert self.widget.w_step.w_cond.lf_Lewout.value() == 0

        self.widget.w_step.w_cond.g_ins.setChecked(True)

        assert self.widget.w_step.w_cond.lf_Wins_cond.value() is None
        assert self.widget.w_step.w_cond.lf_Wins_wire.value() == 0

        self.widget.w_step.w_cond.si_Nwpc1.setValue(1)
        self.widget.w_step.w_cond.si_Nwpc1.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wwire.setValue(0.002)
        self.widget.w_step.w_cond.lf_Wwire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wins_cond.setValue(0.002)
        self.widget.w_step.w_cond.lf_Wins_cond.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wins_wire.setValue(0)
        self.widget.w_step.w_cond.lf_Wins_wire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Lewout.setValue(0)
        self.widget.w_step.w_cond.lf_Lewout.editingFinished.emit()

        assert self.widget.w_step.w_cond.w_out.out_H.text() == "Hcond = 0.002 [m]"
        assert self.widget.w_step.w_cond.w_out.out_W.text() == "Wcond = 0.002 [m]"
        assert self.widget.w_step.w_cond.w_out.out_S.text() == "Scond = 3.142e-06 [m²]"
        assert self.widget.w_step.w_cond.w_out.out_Sact.text() == "Scond_active = 3.142e-06 [m²]"
        assert self.widget.w_step.w_cond.w_out.out_K.text() == "Ksfill = 38.56 %"
        assert self.widget.w_step.w_cond.w_out.out_MLT.text() == "Mean Length Turn = 0.34 [m]"
        assert self.widget.w_step.w_cond.w_out.out_Rwind.text() == "Rwind 20°C = 0.01872 [Ohm]"

        # Is the stator winding conductors well defined ?
        assert isinstance(self.widget.w_step.machine.stator.winding.conductor, CondType12)
        assert self.widget.w_step.machine.stator.winding.conductor.Nwppc == 1
        assert self.widget.w_step.machine.stator.winding.conductor.Wwire == 0.002
        assert self.widget.w_step.machine.stator.winding.conductor.Wins_cond == 0.002
        assert self.widget.w_step.machine.stator.winding.conductor.Wins_wire == 0
        
        assert self.widget.w_step.machine.stator.winding.Lewout == 0

        #####################
        # 7 Rotor Pole
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 7: Rotor Pole"
        assert isinstance(self.widget.w_step, SWPole)

        assert self.widget.w_step.out_Slot_pitch.text() == "Slot pitch = 360 / Zs = 90 [°] (1.571 [rad])"

        assert self.widget.w_step.c_slot_type.count() == 2
        assert self.widget.w_step.c_slot_type.currentText() == "Pole Type 60"

        wid_pole = self.widget.w_step.w_slot
        assert isinstance(self.widget.w_step.w_slot, PWSlot60)

        assert wid_pole.lf_R1.value() is None
        assert wid_pole.lf_W1.value() is None
        assert wid_pole.lf_W2.value() is None
        assert wid_pole.lf_H1.value() is None
        assert wid_pole.lf_H2.value() is None
        assert wid_pole.lf_H3.value() is None
        assert wid_pole.lf_H4.value() is None
        assert wid_pole.lf_W3.value() is None


        wid_pole.lf_R1.setValue(0.0754)
        wid_pole.lf_R1.editingFinished.emit()
        wid_pole.lf_W1.setValue(0.0687)
        wid_pole.lf_W1.editingFinished.emit()
        wid_pole.lf_W2.setValue(0.045)
        wid_pole.lf_W2.editingFinished.emit()
        wid_pole.lf_H1.setValue(0.003)
        wid_pole.lf_H1.editingFinished.emit()
        wid_pole.lf_H2.setValue(0.025)
        wid_pole.lf_H2.editingFinished.emit()
        wid_pole.lf_H3.setValue(0.0005)
        wid_pole.lf_H3.editingFinished.emit()
        wid_pole.lf_H4.setValue(0)
        wid_pole.lf_H4.editingFinished.emit()
        wid_pole.lf_W3.setValue(0)
        wid_pole.lf_W3.editingFinished.emit()

        assert wid_pole.out_Wlam.text() == "Lamination width: 0.0712 [m]"
        assert wid_pole.out_slot_height.text() == "Slot height: 0.03121 [m]"
        assert wid_pole.out_yoke_height.text() == "Yoke height: 0.03999 [m]"
        assert wid_pole.out_wind_surface.text() == "Winding surface: 0.0005807 [m²]"
        assert wid_pole.out_tot_surface.text() == "Total surface: 0.001539 [m²]"
        assert wid_pole.out_op_angle.text() == "Opening angle: 1.571 [rad]"

        assert self.widget.w_step.machine.rotor.slot.R1 == 0.0754
        assert self.widget.w_step.machine.rotor.slot.H1 == 0.003
        assert self.widget.w_step.machine.rotor.slot.H2 == 0.025
        assert self.widget.w_step.machine.rotor.slot.H3 == 0.0005
        assert self.widget.w_step.machine.rotor.slot.H4 == 0
        assert self.widget.w_step.machine.rotor.slot.W1 == 0.0687
        assert self.widget.w_step.machine.rotor.slot.W2 == 0.045
        assert self.widget.w_step.machine.rotor.slot.W3 == 0


        #####################
        # 8 Rotor Lamination
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 8: Rotor Lamination"
        assert isinstance(self.widget.w_step, SLamShape)

        assert self.widget.w_step.lf_L1.value() == 0.17
        assert self.widget.w_step.lf_Kf1.value() == 0.95

        assert not self.widget.w_step.g_axial.isChecked()
        assert not self.widget.w_step.g_radial.isChecked()
        assert not self.widget.w_step.g_notches.isChecked()

        assert self.widget.w_step.machine.rotor.L1 == 0.17
        assert self.widget.w_step.machine.rotor.Kf1 == 0.95

        #####################
        # 9 Rotor Winding
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 9: Rotor Winding"
        assert isinstance(self.widget.w_step, SWinding)

        assert self.widget.w_step.c_wind_type.currentText() == "Star of Slot"
        assert self.widget.w_step.in_p.text() == "Pole pair number=2"
        assert self.widget.w_step.si_qs.value() == 1
        assert not self.widget.w_step.si_qs.isEnabled()
        assert self.widget.w_step.si_Nlayer.value() == 2
        assert not self.widget.w_step.si_Nlayer.isEnabled()
        assert self.widget.w_step.si_coil_pitch.value() == 1
        assert not self.widget.w_step.si_coil_pitch.isEnabled()
        assert self.widget.w_step.si_Ntcoil.value() == 1
        assert self.widget.w_step.si_Npcp.value() == 1
        assert self.widget.w_step.si_Nslot.value() == 0
        assert not self.widget.w_step.is_reverse.isChecked()
        assert not self.widget.w_step.is_permute_B_C.isChecked()
        assert not self.widget.w_step.is_reverse_layer.isChecked()
        assert not self.widget.w_step.is_change_layer.isChecked()

        self.widget.w_step.si_Ntcoil.setValue(45)
        self.widget.w_step.si_Ntcoil.editingFinished.emit()


        self.widget.w_step.b_generate.clicked.emit()

        assert self.widget.w_step.si_Ntcoil.value() == 45
        assert self.widget.w_step.out_rot_dir.text() == "Rotation direction: CW"
        assert self.widget.w_step.out_ms.text() == "Number of slots/pole/phase: 1.0"
        assert self.widget.w_step.out_Nperw.text() == "Winding periodicity: 4"
        assert self.widget.w_step.out_Ntspc.text() == "Number of turns Ntspc: 180"
        assert self.widget.w_step.out_Ncspc.text() == "Number of coils Ncspc: 4"

        # Is the rotor winding well defined ?
        assert self.widget.w_step.machine.rotor.winding.qs == 1
        assert self.widget.w_step.machine.rotor.winding.Nlayer == 2
        assert self.widget.w_step.machine.rotor.winding.coil_pitch == 1
        assert self.widget.w_step.machine.rotor.winding.Ntcoil == 45
        assert self.widget.w_step.machine.rotor.winding.Npcp == 1
        assert self.widget.w_step.machine.rotor.winding.Nslot_shift_wind == 0
        assert not self.widget.w_step.machine.rotor.winding.is_reverse_wind
        assert not self.widget.w_step.machine.rotor.winding.is_permute_B_C
        assert not self.widget.w_step.machine.rotor.winding.is_reverse_layer
        assert not self.widget.w_step.machine.rotor.winding.is_change_layer

        #####################
        # 10 Rotor Conductor
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == "10: Rotor Conductor"
        assert isinstance(self.widget.w_step, SWindCond)

        # Initial state
        assert self.widget.w_step.c_cond_type.currentText() == "Preformed Rectangular"
        assert self.widget.w_step.w_mat_0.c_mat_type.currentText() == "Copper1"
        assert self.widget.w_step.w_mat_1.c_mat_type.currentText() == "Insulator1"

        index_copper2 = self.widget.w_step.w_mat_0.c_mat_type.findText("Copper2")
        self.widget.w_step.w_mat_0.c_mat_type.setCurrentIndex(index_copper2)

        assert isinstance(self.widget.w_step.w_cond, PCondType11)
        assert not self.widget.w_step.w_cond.g_ins.isChecked()
        assert self.widget.w_step.w_cond.si_Nwpc1_rad.value() == 1
        assert self.widget.w_step.w_cond.si_Nwpc1_tan.value() == 1
        assert self.widget.w_step.w_cond.lf_Wwire.value() is None
        assert self.widget.w_step.w_cond.lf_Hwire.value() is None
        assert self.widget.w_step.w_cond.lf_Lewout.value() == 0

        self.widget.w_step.w_cond.g_ins.setChecked(True)

        self.widget.w_step.w_cond.si_Nwpc1_rad.setValue(1)
        self.widget.w_step.w_cond.si_Nwpc1_rad.editingFinished.emit()
        self.widget.w_step.w_cond.si_Nwpc1_tan.setValue(1)
        self.widget.w_step.w_cond.si_Nwpc1_tan.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wwire.setValue(0.002)
        self.widget.w_step.w_cond.lf_Wwire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Hwire.setValue(0.002)
        self.widget.w_step.w_cond.lf_Hwire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wins_wire.setValue(1e-06)
        self.widget.w_step.w_cond.lf_Wins_wire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Lewout.setValue(0)
        self.widget.w_step.w_cond.lf_Lewout.editingFinished.emit()

        assert self.widget.w_step.w_cond.w_out.out_H.text() == "Hcond = 0.002002 [m]"
        assert self.widget.w_step.w_cond.w_out.out_W.text() == "Wcond = 0.002002 [m]"
        assert self.widget.w_step.w_cond.w_out.out_S.text() == "Scond = 4.008e-06 [m²]"
        assert self.widget.w_step.w_cond.w_out.out_Sact.text() == "Scond_active = 4e-06 [m²]"
        assert self.widget.w_step.w_cond.w_out.out_K.text() == "Krfill = 62.00 %"
        assert self.widget.w_step.w_cond.w_out.out_MLT.text() == "Mean Length Turn = 0.34 [m]"
        assert self.widget.w_step.w_cond.w_out.out_Rwind.text() == "Rwind 20°C = 0.3366 [Ohm]"

        # Is the stator winding conductors well defined ?
        assert isinstance(self.widget.w_step.machine.rotor.winding.conductor, CondType11)
        assert self.widget.w_step.machine.rotor.winding.conductor.Nwppc_tan == 1
        assert self.widget.w_step.machine.rotor.winding.conductor.Nwppc_rad == 1
        assert self.widget.w_step.machine.rotor.winding.conductor.Wwire == 0.002
        assert self.widget.w_step.machine.rotor.winding.conductor.Hwire == 0.002
        assert self.widget.w_step.machine.rotor.winding.conductor.Wins_wire == 1e-06
        assert self.widget.w_step.machine.rotor.winding.Lewout == 0

        #####################
        # 11 Rotor Skew
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == "11: Rotor Skew"
        assert isinstance(self.widget.w_step, SSkew)

        assert not self.widget.w_step.g_activate.isChecked()

        #####################
        # 12 Machine Summary
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == "12: Machine Summary"
        assert isinstance(self.widget.w_step, SPreview)

        assert self.widget.w_step.tab_machine.tab_param.item(0,0).text() == "Machine Type"
        assert self.widget.w_step.tab_machine.tab_param.item(0,1).text() == "WRSM"
        assert self.widget.w_step.tab_machine.tab_param.item(1,0).text() == "Stator slot number"
        assert self.widget.w_step.tab_machine.tab_param.item(1,1).text() == "48"
        assert self.widget.w_step.tab_machine.tab_param.item(2,0).text() == "Pole pair number"
        assert self.widget.w_step.tab_machine.tab_param.item(2,1).text() == "2"
        assert self.widget.w_step.tab_machine.tab_param.item(3,0).text() == "Topology"
        assert self.widget.w_step.tab_machine.tab_param.item(3,1).text() == "Internal Rotor"
        assert self.widget.w_step.tab_machine.tab_param.item(4,0).text() == "Stator phase number"
        assert self.widget.w_step.tab_machine.tab_param.item(4,1).text() == "3"
        assert self.widget.w_step.tab_machine.tab_param.item(5,0).text() == "Stator winding resistance"
        assert self.widget.w_step.tab_machine.tab_param.item(5,1).text() == "0.01872 Ohm"
        assert self.widget.w_step.tab_machine.tab_param.item(6,0).text() == "Machine total mass"
        assert self.widget.w_step.tab_machine.tab_param.item(6,1).text() == "53.68 kg"
        assert self.widget.w_step.tab_machine.tab_param.item(7,0).text() == "Stator lamination mass"
        assert self.widget.w_step.tab_machine.tab_param.item(7,1).text() == "27.96 kg"
        assert self.widget.w_step.tab_machine.tab_param.item(8,0).text() == "Stator winding mass"
        assert self.widget.w_step.tab_machine.tab_param.item(8,1).text() == "4.563 kg"
        assert self.widget.w_step.tab_machine.tab_param.item(9,0).text() == "Rotor lamination mass"
        assert self.widget.w_step.tab_machine.tab_param.item(9,1).text() == "18.98 kg"
        assert self.widget.w_step.tab_machine.tab_param.item(10,0).text() == "Rotor winding mass"
        assert self.widget.w_step.tab_machine.tab_param.item(10,1).text() == "2.179 kg"

        self.widget.w_step.tab_machine.b_plot_machine.clicked.emit()
        self.widget.w_step.tab_machine.b_mmf.clicked.emit()

        #####################
        # 13 FEMM Simulation
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == "13: FEMM Simulation"
        assert isinstance(self.widget.w_step, SSimu)

        assert self.widget.w_step.lf_N0.value() == 1000
        assert self.widget.w_step.lf_I1.value() == 0
        assert self.widget.w_step.lf_I2.value() == 0
        assert self.widget.w_step.lf_I3.value() == 5
        assert self.widget.w_step.si_Na_tot.value() == 840
        assert self.widget.w_step.si_Nt_tot.value() == 480
        assert self.widget.w_step.is_per_a.isChecked()
        assert self.widget.w_step.is_per_t.isChecked()
        assert self.widget.w_step.lf_Kmesh.value() == 1
        assert self.widget.w_step.si_nb_worker.value() == 12
        assert self.widget.w_step.le_name.text() == "FEMM_Zoe_Test"


if __name__ == "__main__":
    a = TestNewMachineZoe()
    a.setup_class()
    a.setup_method()
    a.test_Zoe()
    print("Done")