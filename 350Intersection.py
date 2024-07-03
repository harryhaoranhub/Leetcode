from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        left, right = 0, len(nums2) - 1
        result = []
        for i in nums1:
            left, right = 0, len(nums2) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] == i:
                    result.append(i)
                    nums2.pop(mid)
                    break
                elif nums2[mid] < i:
                    left = mid + 1
                else:
                    right = mid - 1

        return result


# A better solution with two-pointers
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         intersection = []
#         nums1.sort()
#         nums2.sort()
#         i = 0
#         for num in nums1:
#             if i >= len(nums2):
#                 break
#             while i < len(nums2) - 1 and nums2[i] < num:
#                 i += 1
#             if nums2[i] == num:
#                 i += 1
#                 intersection.append(num)

#         return intersection
