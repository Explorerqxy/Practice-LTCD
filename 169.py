
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums)//2]


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = set(nums)
        a = 0
        c = 0
        for i in b:
            n = nums.count(i)
            if a < n:
                a = n
                c = i
        return c