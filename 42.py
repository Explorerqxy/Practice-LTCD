class Solution:
    def trap(self, height: List[int]) -> int:
        _height = height[1:-1]
        if not _height:
            return 0

        hmax = max(_height)
        hmin = min(height[0], height[-1])

        if hmax < hmin:
            return hmin * len(_height) - sum(_height)

        pos = _height.index(hmax) + 1         #此处需要特别注意，防止首元素与hmax相同而造成递归溢出
        return self.trap(height[:pos + 1]) + self.trap(height[pos:])






#解法二如下



class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h1 = 0
        h2 = 0
        for i in range(len(height)):
            h1 = max(h1,height[i])
            h2 = max(h2,height[-i-1])
            ans = ans + h1 + h2 -height[i]
        return  ans - len(height)*h1