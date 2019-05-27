class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num



#第二种解法
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if any(nums):
            from functools import cmp_to_key
            nums = sorted([str(x) for x in nums], key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)
            return ''.join(nums)
        return '0'