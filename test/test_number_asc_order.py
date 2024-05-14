import unittest
from unittest.mock import Mock
from src.custom_stack.custom_stack_class import CustomStack, StackEmptyException
from src.custom_stack.number_asc_order import NumberAscOrder



class TestNumberAscOrder(unittest.TestCase):
    def setUp(self):
        self.number_asc_order = NumberAscOrder()

    def test_sort_empty_stack(self):
        stack_mock = Mock(spec=CustomStack)
        stack_mock.isEmpty.return_value = True
        with self.assertRaises(StackEmptyException):
            self.number_asc_order.sort(stack_mock)

    def test_sort_non_empty_stack(self):
        stack = CustomStack(3)
        stack.push(3)
        stack.push(1)
        stack.push(2)
        self.assertEqual(self.number_asc_order.sort(stack), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
