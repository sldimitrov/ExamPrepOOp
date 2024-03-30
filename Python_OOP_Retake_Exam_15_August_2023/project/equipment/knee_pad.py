from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PRICE_INCREASE = 1.2  # 20 percent

    def __init__(self):
        super().__init__(protection=120, price=15.0)

    def increase_price(self):
        self.price *= self.PRICE_INCREASE
