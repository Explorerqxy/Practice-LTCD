class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [0]
 #效率太低8000ms


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mapping:
                return [mapping[complement], i]
            mapping[nums[i]] = i

        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,x in enumerate(nums):
            y=target-x
            if y in hashmap:
                return hashmap[y],i
            hashmap[x]=i
#有待考证
#自己颠倒了一下顺序，原本的enumrate（）函数得到的是序-值，通过循环改为值-序