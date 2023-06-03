class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort(set(nums))
        smallest = 1

        for i in range(len(nums)):
            if nums[i] <= 0:
                continue

            if nums[i] == smallest:
                smallest += 1
            else:
                return smallest

        return smallest
    

    def firstMissingPositiveOptimized(self, nums: list[int]) -> int:
        smallest = 1
        


sol = Solution()
print(sol.firstMissingPositive([7, 8, 9, 11, 12]))
