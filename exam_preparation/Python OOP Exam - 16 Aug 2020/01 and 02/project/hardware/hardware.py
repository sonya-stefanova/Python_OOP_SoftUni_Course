from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if software.capacity_consumption <= self.capacity and software.memory_consumption <= self.memory:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    def __str__(self):
        output = []

        express_software_components_num = len([s for s in self.software_components if s.software_type == "Express"])
        light_software_components_num = len([s for s in self.software_components if s.software_type == "Light"])
        total_memory_installed_software = sum(s.memory_consumption for s in self.software_components)
        total_capacity_installed_software = sum(s.capacity_consumption for s in self.software_components)
        names_of_software_components = ', '.join(s.name for s in self.software_components)

        output.append(f"Hardware Component - {self.name}")
        output.append(f"Express Software Components: {express_software_components_num}")
        output.append(f"Light Software Components: {light_software_components_num}")
        output.append(f"Memory Usage: {total_memory_installed_software} / {self.memory}")
        output.append(f"Capacity Usage: {total_capacity_installed_software} / {self.capacity}")
        output.append(f"Type: {self.hardware_type}")
        output.append(f"Software Components: {names_of_software_components if self.software_components else 'None'}")

        return "\n".join(output)