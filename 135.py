class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        if not length:
            return 0
        if length == 1:
            return 1
        if length == 2:
            if ratings[0] == ratings[1]:
                return 2
            return 3
        done = False
        candys = [1] * length
        for i in range(1, length):
            if ratings[i - 1] < ratings[i] and candys[i - 1] >= candys[i]:
                candys[i] = candys[i - 1] + 1
        for i in range(length - 1, 0, -1):
            if ratings[i - 1] > ratings[i] and candys[i - 1] <= candys[i]:
                candys[i - 1] = candys[i] + 1

        return sum(candys)


#解法2
class Solution:
    def candy(self, ratings: List[int]) -> int:
        s = 0
        n=len(ratings)
        s+=n
        tmp =[0]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                tmp[i] = tmp[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                tmp[i]=max(tmp[i],tmp[i+1]+1)
        s+=sum(tmp)
        return s