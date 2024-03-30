from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PRICE_INCREASE = 1.1  # 10 percent

    def __init__(self):
        super().__init__(protection=90, price=25.0)

    def increase_price(self):
        self.price *= self.PRICE_INCREASE

