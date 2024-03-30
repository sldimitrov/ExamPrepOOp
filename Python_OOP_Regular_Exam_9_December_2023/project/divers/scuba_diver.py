from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540
    OXY_DECREASE_INDEX = 0.3

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=self.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        used_oxy = round(time_to_catch * self.OXY_DECREASE_INDEX)
        if self.oxygen_level < used_oxy:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= used_oxy

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_LEVEL
