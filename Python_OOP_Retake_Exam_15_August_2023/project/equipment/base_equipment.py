from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    def __init__(self, protection: int, price: float):
        self.protection: int = protection
        self.price: float = price

    @abstractmethod
    def increase_price(self):
        ...
