class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = len(numbers)
        m = 0
        n = t - 1
        while m < n:
            tmp = numbers[m] + numbers[n]
            if tmp == target:
                break
            elif tmp < target:
                m += 1
            else:
                n -= 1
        return [m+1, n+1]


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        adic = {}
        for k, v in enumerate(numbers):
            if v in adic:
                return [adic[v] + 1, k + 1]
            else:
                adic[target - v] = k
