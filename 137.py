class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b


#骚操作
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums)) - sum(nums))//2