from unittest import TestCase
import pytest
from unittest.mock import MagicMock, patch
from src.custom_stack.custom_stack_class import CustomStack, StackEmptyException, StackFullException


class CustomStackTest(TestCase):

    @patch('src.custom_stack.custom_stack_class.CustomStack')
    def test_push_value(self, MockCustomStack):
        custom_stack = MockCustomStack(1)
        custom_stack.size.return_value = 1
        custom_stack.push(10)
        custom_stack.push.assert_called_once_with(10)
        assert custom_stack.size() == 1

    @patch('src.custom_stack.custom_stack_class.CustomStack')
    def test_stack_is_full(self, MockCustomStack):
        custom_stack = MockCustomStack(1)
        custom_stack.push.side_effect = [None, StackFullException]
        custom_stack.push(10)
        with pytest.raises(StackFullException):
            custom_stack.push(10)
        assert custom_stack.push.call_count == 2

    @patch('src.custom_stack.custom_stack_class.CustomStack')
    def test_pop_but_stack_is_empty(self, MockCustomStack):
        custom_stack = MockCustomStack(1)
        custom_stack.pop.side_effect = StackEmptyException
        with pytest.raises(StackEmptyException):
            custom_stack.pop()
        custom_stack.pop.assert_called_once()

    @patch('src.custom_stack.custom_stack_class.CustomStack')
    def test_remove_element(self, MockCustomStack):
        custom_stack = MockCustomStack(1)
        custom_stack.pop.return_value = 10
        custom_stack.push(10)
        assert custom_stack.pop() == 10
        custom_stack.push.assert_called_once_with(10)
        custom_stack.pop.assert_called_once()

    @patch('src.custom_stack.custom_stack_class.CustomStack')
    def test_stack_size(self, MockCustomStack):
        custom_stack = MockCustomStack(2)
        custom_stack.size.return_value = 2
        custom_stack.push(10)
        custom_stack.push(10)
        assert custom_stack.size() == 2
        assert custom_stack.push.call_count == 2

    @patch('src.custom_stack.custom_stack_class.CustomStack')
    def test_stack_is_empty(self, MockCustomStack):
        custom_stack = MockCustomStack(1)
        custom_stack.isEmpty.return_value = True
        assert custom_stack.isEmpty() == True
        custom_stack.isEmpty.assert_called_once()

    @patch('src.custom_stack.custom_stack_class.CustomStack')
    def test_get_top_but_stack_is_empty_exception(self, MockCustomStack):
        custom_stack = MockCustomStack(1)
        custom_stack.top.side_effect = StackEmptyException
        with pytest.raises(StackEmptyException):
            custom_stack.top()
        custom_stack.top.assert_called_once()

    @patch('src.custom_stack.custom_stack_class.CustomStack')
    def test_top_of_stack(self, MockCustomStack):
        custom_stack = MockCustomStack(1)
        custom_stack.top.return_value = 10
        custom_stack.push(10)
        assert custom_stack.top() == 10
        custom_stack.push.assert_called_once_with(10)
        custom_stack.top.assert_called_once()
