class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum=nums[0]
        for i in nums[1:]:
            if i<minNum:
                minNum=i
        return minNum