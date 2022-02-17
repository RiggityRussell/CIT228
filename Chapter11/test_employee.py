from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        first_name = "Russell"
        last_name = "Arlt"
        annual_salary = 50000
        self.test_time = Employee(first_name, last_name, annual_salary)

    def test_give_default_raise(self):
        self.assertEqual(self.test_time.annual_salary, 50000)

    def test_give_custom_raise(self, payRaise = 4000):
        self.test_time.annual_salary += payRaise
        self.assertEqual(self.test_time.annual_salary, 54000)

if __name__ == "__main__":
    unittest.main()