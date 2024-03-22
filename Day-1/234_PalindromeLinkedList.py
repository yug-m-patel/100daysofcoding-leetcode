# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        temp = head
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        temp1 =head
        while temp1 is not None:
            if stack.pop() != temp1.val:
                return False
            temp1 = temp1.next
        return True
