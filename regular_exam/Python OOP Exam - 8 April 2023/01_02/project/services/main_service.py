from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        result = []
        robots_status = "none"
        result.append(f"{self.name} Main Service:")
        if self.robots:
            robots_status = ' '.join([r.name for r in self.robots])
        result.append(f"Robots: {robots_status}")

        return "\n".join(result)