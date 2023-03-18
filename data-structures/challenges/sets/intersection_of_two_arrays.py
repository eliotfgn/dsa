from typing import List


class Solution:
    def intersection_set(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sah = set()
        return list(set(nums1) & set(nums2))

    def intersection_array(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res: List[int] = []
        smallest = min(nums1, nums2)
        greatest = max(nums1, nums2)

        for el in smallest:
            if el in greatest and el not in res:
                res.append(el)

        return res


sol = Solution()
print(sol.intersection_array([4, 9, 5], [9, 4, 9, 8, 4]))
