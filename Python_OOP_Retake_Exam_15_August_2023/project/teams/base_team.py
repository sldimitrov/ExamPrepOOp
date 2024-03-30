from project.equipment.base_equipment import BaseEquipment
from abc import ABC, abstractmethod
from typing import List
from math import floor


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value: str):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value: int):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        total_equipment_price = sum([e.price for e in self.equipment])

        team_protection_values = [p.protection for p in self.equipment]
        avg_team_protection = floor(sum(team_protection_values) / len(team_protection_values) if self.equipment else 0)

        info = f"""Name: {self.name}
Country: {self.country}
Advantage: {self.advantage} points
Budget: {self.budget:.2f}EUR
Wins: {self.wins}
Total Equipment Price: {total_equipment_price:.2f}
Average Protection: {avg_team_protection}"""

        return info

    def sum_points(self):
        return self.advantage + sum([eq.protection for eq in self.equipment])


