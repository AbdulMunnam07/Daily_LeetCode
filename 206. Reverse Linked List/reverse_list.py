class Solution:
    def reverseList(head):
        prev = None
        curr = head
        while curr:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next

        return prev