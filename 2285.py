from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        diction = {}
        for r in roads:
            for e in r:
                if e not in diction:
                    diction[e] = 0
                diction[e] += 1

        # diction.sort()
        diction = sorted(diction.items(), key=lambda item: item[1], reverse=True)
        
        importance = [0] * n
        for i,_ in diction:
            importance[i] = n
            n = n - 1

        result = 0
        for u, v in roads:
            result += importance[u] + importance[v]
        
        return result
        
