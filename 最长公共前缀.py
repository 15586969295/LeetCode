# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs):
            for i in range(len(strs[0])):
                res += strs[0][i]
                if False not in [string.startswith(res) for string in strs]:
                    continue
                else:
                    res = res[:-1]
        return res
