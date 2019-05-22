class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        """这里其实借用了上一题的函数,如果有解才进行递归搜索
        但是实际上在动态规划的时候已经进行了一次搜索,就是在动态规划的时候不好出结果
        而且但是测试例里面有不能分割的,如果过程中进行保存操作反而浪费时间
        """
        if not wordDict:
            return []
        self.res, self.max_length, self.min_length, self.word_set = [], 0, len(wordDict[0]), set(wordDict)
        # 后续搜索时没有必要搜索所有长度,只需要搜索从字典中字符最短长度到最大长度的字符串就行了
        for word in wordDict:
            self.max_length = max(self.max_length, len(word))
            self.min_length = min(self.min_length, len(word))
        # 动态规划的列表第一个默认是True,后面默认是False,第一个是True表示空的字符应该认为可以被分割
        res_list = [not i for i in range(len(s)+1)]
        # 这里i不是直接的位置,而是位置+1,因为还有一个空的
        for i in range(1, len(s)+1):
            for j in range(self.min_length, self.max_length+1):
                # 小于0了注意别再处理了
                if i - j < 0:
                    break
                # 如果某个串在wordDict里,并且这个串开头是True,就说明到这个位置是可分割的
                # 还是要注意因为i是加过1的,所以索引容易弄错
                if s[i-j:i] in self.word_set and res_list[i-j]:
                    res_list[i] = True
                    break
        # 只有可分割才进行递归分割
        if res_list[-1]:
            self.find_and_add(s, [])
        return self.res

    def find_and_add(self, s_in, list_in):
        for i in range(self.min_length, self.max_length+1):
            if s_in[:i] in self.word_set:
                # 一开始返回写在了下一层里面,然后发现结果会重复,但是如果每次加都判断速度就会变慢
                # 所以返回没有像一般递归一样独立出来,而是写在了函数体里面
                if not s_in[i:]:
                    self.res.append(" ".join(list_in + [s_in[:i]]))
                    return
                self.find_and_add(s_in[i:], list_in+[s_in[:i]])