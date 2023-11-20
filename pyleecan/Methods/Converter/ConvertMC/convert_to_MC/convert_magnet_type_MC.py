def convert_magnet_type_MC(self):
    """Selection correct magnet and implementation in obj machine or in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    # conversion to Motor-CAD
    magnet_type = type(self.machine.rotor.slot).__name__

    # selection type of Slot
    if magnet_type == "SlotM11" and self.machine.rotor.slot.H0 == 0:
        name_slot = "Surface_Radial"

    elif magnet_type == "SlotM15" and self.machine.rotor.slot.H0 == 0:
        name_slot = "Surface_Parallel"

    elif magnet_type == "SlotM13":
        name_slot = "Surface_Breadleaof"

    if magnet_type == "SlotM11":
        name_slot = "Inset_Radial"

    elif magnet_type == "SlotM15":
        name_slot = "Inset_Parallel"

    elif magnet_type == "SlotM12":
        name_slot = "Inset_Breadleaof"

    elif magnet_type == "SlotM16":
        name_slot = "Spoke"

    else:
        raise Exception("Conversion of machine doesn't exist")

    # writting in dict
    if "[Design_Options]" not in self.other_dict:
        self.other_dict["[Design_Options]"] = {}
        temp_dict = self.other_dict["[Design_Options]"]
        temp_dict["BPM_Rotor"] = name_slot
    else:
        self.other_dict["[Design_Options]"]["BPM_Rotor"] = name_slot

    self.get_logger().info(f"Conversion {magnet_type} into {name_slot}")