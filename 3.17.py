# from typing import Any
# class Node(object):
#     def __init__(self,data: Any, next_node:  Node= None):
#         self.data = data
#         self.next = None
#
#
#
# class LinkedList(object):
#     def __init__(self, head=None) -> None:
#         self.head = None
#
#     def append(self, data: Any) -> None:
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node
#
#
#     def insert(self, data: Any) -> None:
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def print(self): -> None:
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#         current_node = current_node.next
#
#     def remove(self, data: Any) -> Node:
#         current_node = self.head
#
#         if current_node and current_node.data == data:
#             self.head = current_node.next
#             current_node = None
#             return
#
#         previous_node = None
#         while current_node and current_node.data != data:
#             previous_node = current_node
#             current_node = current_node.next
#
#         if current_node is None:
#             return
#
#         previous_node.next = current_node.next
#         current_node = None
#
#     def reverse_iterative(self) -> None:
#         previous_node = None
#         current_node = self.head
#         while current_node:
#
#             next_node = current_node.next
#             current_node.next = previous_node
#
#             previous_node = current_node
#         self.head = previous_node
#
#
#     def reverse_recrsive(self) -> None:
#         def _reverse_recrsive(current_node: Node, previous_node: Node):
#


#
#
#
# if __name__ == '__main__':
#     l = LinkedList()
#     l.append(1)
#     l.append(2)
#     l.append(3)
#     l.append(0)
#     print(l.head.data)
#
#     l.print()
#     l.remov
#     e(2)


from typing import List, Tuple, Optional



def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    # if sum_numbers % 2 != 0:
    #     return
    # half_sum = int(sum_numbers / 2)
    #
    #
    #
    # cache = set()
    #
    # for num in numbers:
    #     cache.add(num)
    #     val = half_sum - num
    #
    #     if val in cache:
    #         return val,　num
#
#     half_sum, remainder = divmod(sum_numbers, 2)
#     if remainder != 0:
#         return
#     cache = set()
#     for num in numbers:
#         cache.append(num)
#         val = sum_numbers - num
#         if val in cache:
#             return val, num
#
#
# if __name__ == '__main__':
#     l = [11, 2, 5, 9, 11,3]
#     print(get_pair_half_sum(l))
#
#
#
#
#
#



from typing import Any

#
# class Stack(object):
#     def __init__(self) -> None:
#         self.stack = []
#
#     def push(self, data) -> None:
#         self.stack.append(data)
#
#     def pop(self) -> Any:
#         if self.stack:
#             return self.stack.pop()
#
# if __name__ == '__main__':
#     stack = Stack()
#     print(stack.stack)
#     stack.push(1)
#     print(stack.stack)
#     stack.push(3)
#     print(stack.stack)
#     print(stack.pop())

#
# class Stack(object):
#     def __init__(self):
#         self.stack = []
#
#     def push(self, data):
#         self.stack.append(data)
#
#     def pop(self) -> Any:
#         if self.stack:
#             return self.stack.pop()
#
# if __name__ == '__main__':
#     stack = Stack()
#     print(stack.stack)
#     print(stack.push(8))
#     print(stack.stack)

#
# def validate_format(chars: str) -> bool:
#     lookup = {'{': '}', '[': ']', '(': ')'}
#     stack = []
#     for char in chars:
#         if char in lookup.keys():
#             stack.append(lookup[char])
#
#         if char in lookup.values():
#             if not stack:
#                 return False
#
#
#             if char != stack.pop():
#                 return False
#
#     if stack:
#         return False
#     return True
#
# if __name__ == '__main__':
#     j = "{'key  '}"


#
#
# import sentry_sdk
#
# sentry_sdk.init('< DSNの値 >')
#




from typing import List
#
# def bubble_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         for j in range(len_numbers - 1 -i):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#     return numbers
#
#
#
#
#
# if __name__ == '__main__':
#     nums = [12,3,4,8,5]
#     print(bubble_sort(nums))


#
# def selection_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         min_idx = i
#         for j in range(i+1, len_numbers):
#             if numbers[min_idx] > numbers[j]:
#                 min_idx = j
#         numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
#     return numbers



def






if __name__ == '__main__':
    nums = [12,3,4,8,5]
    print(selection_sort(nums))


