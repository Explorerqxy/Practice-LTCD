class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)
        while low < high - 1:
            mid = (low+high)//2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[low] > nums[mid-1]:
                high = mid
            else:
                low = mid
        return nums[0]