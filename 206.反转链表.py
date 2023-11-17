#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):      
    def reverseList(self, head):
        def helper(pre,now):
            if(now == None):
                return pre
            else:
                tmpNext = now.next
                now.next = pre
                return helper(now,tmpNext)
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return head
        tmpNext = head.next
        head.next = None
        return helper(head,tmpNext)
    


# @lc code=end

