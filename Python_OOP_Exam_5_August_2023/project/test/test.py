from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar(
            "BMW R3",
            "Cabriolet",
            1000,
            12000,
        )

        self.second_car = SecondHandCar(
            "BMW M5",
            "Cabriolet",
            1000,
            20000,
        )

        self.other_car = SecondHandCar(
            "BMW R4",
            "Hashback",
            1000,
            12000,
        )

    def test_correct_init(self):
        self.assertEqual("BMW R3", self.car.model)
        self.assertEqual("Cabriolet", self.car.car_type)
        self.assertEqual(1000, self.car.mileage)
        self.assertEqual(12000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_below_1_should_raise_exception(self):
        invalid_price = 0.5

        with self.assertRaises(ValueError) as ve:
            self.car.price = invalid_price

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_set_price_higher_than_1_expects_success(self):
        price = 50000

        self.car.price = price

        self.assertEqual(50000, self.car.price)

    def test_set_mileage_that_is_lower_than_100_should_raise_exception(self):
        invalid_mileage = 50

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = invalid_mileage

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_mileage_expects_success(self):
        mileage = 300

        self.car.mileage = mileage

        self.assertEqual(300, self.car.mileage)

    def test_set_promotional_price_with_higher_values_raises_exception(self):
        price = 15000

        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(price)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_expects_success(self):
        price = 10000

        return_message = self.car.set_promotional_price(price)

        self.assertEqual(price, self.car.price)
        self.assertEqual(return_message, 'The promotional price has been successfully set.')

    def test_repair_with_price_higher_than_half_the_price_of_the_car_itself_expect_failure(self):
        repair_price = 8000
        repair_description = f"The engine is broken and smashed whole"

        returned_message = self.car.need_repair(repair_price, repair_description)

        self.assertEqual('Repair is impossible!', returned_message)

    def test_repair_with_affordable_price_expects_success(self):
        repair_price = 300
        repair_description = f"Fix the lightbar and the brakes"

        returned_message = self.car.need_repair(repair_price, repair_description)

        self.assertEqual('Price has been increased due to repair charges.', returned_message)
        self.assertEqual(12300, self.car.price)
        self.assertEqual(self.car.repairs[-1], repair_description)

    def test_comparing_two_cars_from_different_types_expects_failure(self):

        result = self.car > self.other_car

        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_comparing_two_cars_from_same_type_expects_true_for_the_car_with_bigger_price(self):
        is_bigger = self.second_car > self.car

        self.assertTrue(is_bigger)

    def test_string_representation(self):
        expected_message = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""
        message = str(self.car)

        self.assertEqual(message, expected_message)


if __name__ == '__main__':
    main()
