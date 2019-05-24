class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = len(nums)
        if t < 2:
            return 0
        nums.sort()
        res = 0
        for i in range(1,t):
            tmp = nums[i] - nums[i-1]
            if tmp > res:
                res = tmp
        return res