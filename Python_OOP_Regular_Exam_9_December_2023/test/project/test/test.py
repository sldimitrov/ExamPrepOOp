from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.railway = RailwayStation(
            "Restain"
        )

    def test_correct_init(self):
        self.assertEqual("Restain", self.railway.name)
        self.assertEqual(deque(), self.railway.arrival_trains)
        self.assertEqual(deque(), self.railway.departure_trains)

    def test_set_name_with_less_or_equal_than_3_symbols_raise_exception(self):
        name = "FAL"  # Arrange

        with self.assertRaises(ValueError) as ve:  # Act
            self.railway.name = name

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))  # Assert

    def test_set_name_with_more_than_3_symbols_change_railway_name_successfully(self):
        name = "Valid Test Name"  # Arrange

        self.railway.name = name  # Act

        self.assertEqual(self.railway.name, "Valid Test Name")  # Assert

    def test_new_arrival_on_board(self):
        train_info = "Train N:3"

        self.railway.new_arrival_on_board(train_info)

        self.assertEqual(len(self.railway.arrival_trains), 1)

    def test_to_set_departure_train_on_the_platform_when_it_is_on_turn_expect_success(self):
        self.railway.arrival_trains = deque(["1", "2", "3", "4", "5"])  # Arrange
        train_info = "1"

        expected_return = f"{train_info} is on the platform and will leave in 5 minutes."  # Act
        expected_result = "1"

        action_return = self.railway.train_has_arrived(train_info)  # Act

        self.assertEqual(len(self.railway.departure_trains), 1)  # Assert
        self.assertEqual(expected_return, action_return)
        self.assertEqual(expected_result, self.railway.departure_trains.pop())

    def test_set_to_departure_train_which_is_not_on_turn_expect_failure(self):
        self.railway.arrival_trains = deque(["1", "2", "3", "4", "5"])  # Arrange
        train_info = "Train is not on turn..."
        expected_result = f"There are other trains to arrive before {train_info}."

        result = self.railway.train_has_arrived(train_info)  # Act

        self.assertEqual(len(self.railway.departure_trains), 0)
        self.assertEqual(expected_result, result)  # Assert

    def test_if_train_is_left_expects_true(self):
        self.railway.new_arrival_on_board("Some info")
        self.railway.train_has_arrived("Some info")

        self.assertEqual(len(self.railway.departure_trains), 1)
        self.assertEqual(len(self.railway.arrival_trains), 0)

        result = self.railway.train_has_left("Some info")

        self.assertTrue(result)
        self.assertEqual(len(self.railway.departure_trains), 0)
        self.assertEqual(len(self.railway.departure_trains), 0)

        self.assertEqual(self.railway.departure_trains, deque())

    def test_if_train_is_left_expects_false(self):
        self.railway.new_arrival_on_board("Some info")
        self.railway.train_has_arrived("Some info")

        self.assertEqual(len(self.railway.departure_trains), 1)
        self.assertEqual(len(self.railway.arrival_trains), 0)

        result = self.railway.train_has_left("Different info")

        self.assertFalse(result)
        self.assertEqual(len(self.railway.departure_trains), 1)
        self.assertEqual(len(self.railway.departure_trains), 1)


if __name__ == '__main__':
    main()
