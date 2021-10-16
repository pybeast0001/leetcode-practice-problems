# Link to the problem statement > https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        intersected = False
        point = None
        while headA:
            headA.visited = True
            headA = headA.next
        while headB:
            try:
                if headB.visited == True:
                    return headB
            except:
                pass
            headB = headB.next
        return None
