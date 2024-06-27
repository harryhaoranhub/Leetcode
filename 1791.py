from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        diction = {}
        for e in edges[0]:
            diction[e] = 1
        for d in edges[1]:
            if d in diction:
                diction[d] += 1
            else:
                diction[d] = 1
        for node in diction:
            if diction[node] == 2:
                return node
