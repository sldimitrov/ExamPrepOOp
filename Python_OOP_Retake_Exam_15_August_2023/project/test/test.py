from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    DESTINATION_PRICES_PER_PERSON = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}

    def setUp(self):
        self.trip = Trip(5000.0, 3, True)

    def test_init(self):
        self.assertEqual(5000.0, self.trip.budget)
        self.assertEqual(3, self.trip.travelers)
        self.assertTrue(self.trip.budget)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_set_travelers_less_than_1_except_exception(self):

        with self.assertRaises(Exception) as ex:
            self.trip.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ex.exception))

    def test_set_travelers_with_1_expect_success(self):
        self.trip.travelers = 1
        self.assertEqual(1, self.trip.travelers)

    def test_set_family_to_true_with_less_than_2_people_expect_false(self):
        self.trip.travelers = 1
        self.trip.is_family = True

        self.assertEqual(False, self.trip.is_family)

    def test_set_family_to_true_with_2_people_expect_true(self):
        self.trip.travelers = 2
        self.trip.is_family = True

        self.assertEqual(True, self.trip.is_family)

    def test_set_family_with_diff_value_and_with_2_people_expect_diff_value(self):
        self.trip.travelers = 2
        self.trip.is_family = "Big Family"

        self.assertEqual("Big Family", self.trip.is_family)

    def test_book_a_trip_with_invalid_destination(self):
        result = self.trip.book_a_trip("Persia")
        expected_result = 'This destination is not in our offers, please choose a new one!'

        self.assertEqual(expected_result, result)

    def test_book_a_trip_with_not_enough_budget_expect_string_return_only(self):
        result = self.trip.book_a_trip('New Zealand')
        expected_result = 'Your budget is not enough!'

        self.assertEqual(expected_result, result)

    def test_book_a_trip_with_enough_budget_and_valid_destination_expect_result_booked_trip_and_decreased_budged(self):
        destination = 'Bulgaria'
        result = self.trip.book_a_trip('Bulgaria')

        expected_result = f'Successfully booked destination {destination}! Your budget left is {self.trip.budget:.2f}'
        self.assertEqual({'Bulgaria': 1350.0}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(expected_result, result)

    def test_book_a_trip_without_discount_for_non_family_tourists(self):
        destination = 'Bulgaria'
        self.trip.travelers = 3
        self.trip.is_family = False
        self.trip.budget = 1480  # 20 below the required

        result = self.trip.book_a_trip(destination)
        expected_result = 'Your budget is not enough!'

        self.assertEqual(expected_result, result)

    def test_booking_status(self):
        self.trip.booked_destinations_paid_amounts = {}

        result = self.trip.booking_status()
        expected_result = f'No bookings yet. Budget: {self.trip.budget:.2f}'

        self.assertEqual(expected_result, result)

    def test_booking_status_sorting_trips(self):
        self.trip.booked_destinations_paid_amounts = {'Bulgaria': 5000, 'Australia': 15000}
        sorted_bookings = sorted(self.trip.booked_destinations_paid_amounts.items())

        expected_result = []

        for booked_destination, paid_amount in sorted_bookings:
            expected_result.append(f"""Booked Destination: {booked_destination}
Paid Amount: {paid_amount:.2f}""")
        expected_result.append(f"""Number of Travelers: {self.trip.travelers}
Budget Left: {self.trip.budget:.2f}""")
        expected_result = '\n'.join(expected_result)

        result = self.trip.booking_status()

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
