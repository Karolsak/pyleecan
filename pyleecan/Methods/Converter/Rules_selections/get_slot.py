from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Converter.Rules.rule_parallel_tooth_slotW11 import (
    add_rule_parallel_tooth_slotW11,
)


def get_slot(self, is_stator):
    self.is_stator = is_stator
    slot_type = self.mot_dict["[Calc_Options]"]["Slot_Type"]
    print(slot_type)

    if slot_type == "Parallel_Tooth":
        self.rules = add_rule_parallel_tooth_slotW11(self.rules, self.is_stator)

    elif slot_type == "Parallel Tooth SqB":
        pass
    elif slot_type == "Parallel Slot":
        pass
        # add_rules_parallel_slot_slotW11
    elif slot_type == "Tapered Slot":
        pass
    elif slot_type == "Slotless":
        pass
    elif slot_type == "Form Wound":
        pass

    return self.rules