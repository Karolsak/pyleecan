from pyleecan.Converter.motor_cad_to_pyleecan.change_mot_dict import convert_mot_dict
from pyleecan.Methods.Converter.Machine_type_mot.get_BPM import get_BPM
from pyleecan.Methods.Converter.Machine_type_mot.get_IM import get_IM
from pyleecan.Methods.Converter.Machine_type_mot.get_SRM import get_SRM
from pyleecan.Methods.Converter.Machine_type_mot.get_BPMO import get_BPMO
from pyleecan.Methods.Converter.Machine_type_mot.get_PMDC import get_PMDC
from pyleecan.Methods.Converter.Machine_type_mot.get_SYNC import get_SYNC
from pyleecan.Methods.Converter.Machine_type_mot.get_CLAW import get_CLAW
from pyleecan.Methods.Converter.Machine_type_mot.get_IM1PH import get_IM1PH
from pyleecan.Methods.Converter.Machine_type_mot.get_WFC import get_WFC

from pyleecan.Converter.Rules.rule_machine_dimension import add_rule_machine_dimension
from pyleecan.Converter.Rules.rule_machine_type import add_rule_machine_type

from pyleecan.Functions.Converter.rule_convert import rule_convert


class MachineSelect:
    def __init__(self, rules=[]):
        self.rules = rules
        self.mot_dict = convert_mot_dict()

    def add_rules(self, mot_dict, rules):
        return rules

    def machine_selection(self):
        motor_type = self.mot_dict["[Calc_Options]"]["Motor_Type"]

        self.rules = self.add_rules(self.mot_dict, self.rules)

        self.rules = add_rule_machine_type(self.rules)
        # selecion motor_type
        if motor_type == "BPM":
            self.rules = add_rule_machine_dimension(self.rules)
            get_BPM(self)
        elif motor_type == "IM":
            get_IM(self)
        elif motor_type == "SRM":
            get_SRM(self)
        elif motor_type == "BPMO":
            get_BPMO(self)
        elif motor_type == "PMDC":
            get_PMDC(self)
        elif motor_type == "SYNC":
            get_SYNC(self)
        elif motor_type == "CLAW":
            get_CLAW(self)
        elif motor_type == "IM1PH":
            get_IM1PH(self)
        elif motor_type == "WFC":
            get_WFC(self)

        return self.rules


if __name__ == "__main__":
    mot_dict = convert_mot_dict()
    machine_select = MachineSelect()
    rules_list = machine_select.machine_selection()
    machine = rule_convert(rules_list, mot_dict, None)

    print("done")