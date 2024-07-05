# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
from typing import List


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        distance = []
        index = 1
        prev = head
        curr = head.next
        next_node = curr.next
        
        while next_node:
            if (curr.val > prev.val and curr.val > next_node.val) or (curr.val < prev.val and curr.val < next_node.val):
                distance.append(index)
            
            prev = curr
            curr = next_node
            next_node = next_node.next
            index += 1
        
        if len(distance) < 2:
            return [-1, -1]
        
        min_distance = float('inf')
        max_distance = distance[-1] - distance[0]

        for i in range(1, len(distance)):
            min_distance = min(min_distance, distance[i] - distance[i-1])
        
        return [min_distance, max_distance]
