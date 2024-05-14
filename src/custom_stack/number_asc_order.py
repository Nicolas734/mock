from src.custom_stack.custom_stack_class import CustomStack, StackEmptyException

class NumberAscOrder:
    def sort(self, stack: CustomStack) -> list:
        breakpoint()
        if stack.isEmpty():
            raise StackEmptyException
        stack_values = list()
        while not stack.isEmpty():
            stack_values.append(stack.pop())
        stack_values.sort()
        return stack_values