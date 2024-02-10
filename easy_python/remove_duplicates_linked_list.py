# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        node = head
        while node.next:
            next_node = node.next #
            if next_node.val == node.val:
                node.next = next_node.next
                next_node.next = 0
            else:
                node = next_node
        return head