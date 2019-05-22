class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cMax = cMin = res = nums[0]
        for num in nums[1:]:
            tmp = cMax
            cMax = max(num, num*cMax, num*cMin)
            cMin = min(num, num*tmp, num*cMin)
            res = max(res, cMax)
        return res