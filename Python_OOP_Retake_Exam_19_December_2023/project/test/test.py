from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot(
            'Mountain',
            'Helper',
            100,
            200
        )

        self.robot_with_software = ClimbingRobot(
            "Mountain",
            "Helper",
            100,
            200,
        )

        self.robot_with_software.installed_software = [
            {"name": "Pycharm", "capacity_consumption": 50, "memory_consumption": 30},
            {"name": "VScode", "capacity_consumption": 30, "memory_consumption": 20},
        ]

    def test_correct_init(self):
        self.assertEqual('Mountain', self.robot.category)
        self.assertEqual('Helper', self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)

    def test_set_category_from_valid_type_expect_changed_type(self):
        self.robot.category = 'Mountain'
        self.assertEqual(self.robot.category, 'Mountain')

    def test_set_category_with_invalid_value_raises_value_error(self):
        invalid_category = 'InvalidCategory'
        expected_result = f"Category should be one of {self.ALLOWED_CATEGORIES}"

        with self.assertRaises(ValueError) as ve:
            self.robot.category = invalid_category

        self.assertEqual(expected_result, str(ve.exception))

    def test_get_the_sum_of_the_capacity_of_the_installed_software(self):
        self.assertEqual(80, self.robot_with_software.get_used_capacity())

    def test_get_available_memory_expects_the_difference_between_capacity_and_used_capacity(self):
        expected_result = 20
        result = self.robot_with_software.get_available_capacity()
        self.assertEqual(expected_result, result)

    def test_get_the_sum_of_the_used_memory_for_installed_software(self):
        expected_result = 50
        result = self.robot_with_software.get_used_memory()

        self.assertEqual(expected_result, result)

    def test_get_available_memory_expects_the_diff_between_the_memory_and_used_memory(self):
        expected_result = 150
        result = self.robot_with_software.get_available_memory()

        self.assertEqual(expected_result, result)

    def test_install_software_that_has_lower_memory_and_capacity_than_the_available_expect_success(self):
        software = {"name": "Windows 11", "capacity_consumption": 5, "memory_consumption": 5}

        expected_result = f"Software '{software['name']}' successfully installed on {self.robot.category} part."
        result = self.robot.install_software(software)

        self.assertEqual(expected_result, result)
        self.assertEqual(software, self.robot.installed_software[-1])

    def test_install_software_that_has_equal_memory_and_capacity_levels_with_the_robot_device_expect_success(self):
        software = {"name": "Kali Linux", "capacity_consumption": 100, "memory_consumption": 200}

        expected_result = f"Software '{software['name']}' successfully installed on {self.robot.category} part."
        result = self.robot.install_software(software)

        self.assertEqual(expected_result, result)
        self.assertEqual(software, self.robot.installed_software[-1])

    def test_install_software_which_capacity_exceed_the_robot_one_expects_failure(self):
        software = {"name": "Pinguin", "capacity_consumption": 1000, "memory_consumption": 200}

        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        result = self.robot.install_software(software)

        self.assertEqual(expected_result, result)

    def test_install_software_which_memory_exceed_the_robot_one_expects_failure(self):
        software = {"name": "Pinguin", "capacity_consumption": 100, "memory_consumption": 2000}

        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        result = self.robot.install_software(software)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
