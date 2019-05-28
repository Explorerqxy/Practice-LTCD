class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # b表示二进制数
        # oribin='{0:032b}'.format(n)
        # reversebin=oribin[::-1]
        # return int(reversebin,2)

        # 将n转化为二进制数，前两个字符为0b，所以从第三个字符取
        return int(bin(n)[2:].zfill(32)[::-1], 2)