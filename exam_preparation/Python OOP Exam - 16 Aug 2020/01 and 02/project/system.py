from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []# an empty list that will be storing all the hardware components
    _software = []# an empty list that will be storing all the software components

    @staticmethod
    def _find_hardware(hardware_name):
    #     for hardware in System._hardware:
    #         if hardware.name == hardware_name:
    #             return hardware
        hardware = next(filter(lambda h: h.name == hardware_name, System._hardware), None)
        return hardware

    @staticmethod
    def _find_software(software_name):
        # for software in System._software:
        #     if software.name == software_name:
        #         return software
        software = next(filter(lambda s: s.name == software_name, System._software), None)
        return software

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        """Create a PowerHardware instance and add it to the hardware list"""
        new_power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        """Create a HeavyHardware instance and add it to the hardware list"""
        new_heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        """•	If the hardware with the given name does NOT exist, return the message "Hardware does not exist"
•	Otherwise, create an express software, install it on the hardware, and add it to the software list
•	If the installation is not possible, raise Exception with the message "Software cannot be installed"
"""
        hardware = System._find_hardware(hardware_name)

        if not hardware:
            return "Hardware does not exist"

        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(new_software)
            System._software.append(new_software)
        except ValueError as error:
            return str(error)


    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        """•	If the hardware with the given name does NOT exist, return a message "Hardware does not exist"
            •	Otherwise, create a light software instance, install it on the hardware, and add it to the software list
            •	If the installation is not possible, raise Exception with the message "Software cannot be installed"
"""
        if hardware_name not in [h.name for h in System._hardware]:
            return "Hardware does not exist"

        hardware = System._find_hardware(hardware_name)

        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(new_software)
            System._software.append(new_software)
        except ValueError as error:
            return str(error)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        """•	If both components exist on the system, uninstall the software from the given hardware,
        and remove it from the software list
            •	Otherwise, return a message "Some of the components do not exist"
"""
        if hardware_name in [h.name for h in System._hardware] and \
            software_name in [s.name for s in System._software]:
            hardware = System._find_hardware(hardware_name)
            software = System._find_software(software_name)

            hardware.uninstall(software)
            System._software.remove(software)

        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        """Return the following information (as a string)
         for the total memory and capacity used (calculated for all hardware components in the system):
         "System Analysis
            Hardware Components: {number_of_hardware_components}
            Software Components: {number_of_software_components}
            Total Operational Memory: {total memory consumption for all registered software components} / {total memory for all registered hardware components}
            Total Capacity Taken: {total capacity consumption for all registered software components} / {total capacity of all registered hardware components}"
"""
        total_memory_cons_software = sum([m.memory_consumption for m in System._software])
        total_memory_cons_hardware = sum([m.memory for m in System._hardware])

        total_capacity_cons_software = sum([c.capacity_consumption for c in System._software])
        total_capacity_cons_hardware = sum([c.capacity for c in System._hardware])

        result = []
        result.append("System Analysis")
        result.append(f"Hardware Components: {len(System._hardware)}")
        result.append(f"Software Components: {len(System._software)}")
        result.append(f"Total Operational Memory: {total_memory_cons_software} / {total_memory_cons_hardware}")
        result.append(f"Total Capacity Taken: {total_capacity_cons_software} / {total_capacity_cons_hardware}")


        return "\n".join(result)


    @staticmethod
    def system_split():
        """Return the following information (as a string) for each hardware component:
        "Hardware Component - {component name}
        Express Software Components: {number of the installed express software components}
        Light Software Components: {number of the installed light software components}
        Memory Usage: {total memory used of all installed software components} / {total memory of the hardware}
        Capacity Usage: {total capacity used of all installed software components } / {total capacity of the hardware}
        Type: {hardware_type}
        Software Components: {names of all software components separated by ', '} (or 'None' if no software components)"
"""
        result = ''

        result = []
        for hardware in System._hardware:
            result.append(str(hardware))
        return "\n".join(result)