# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = dict()
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = 1
            else:
                dct[s[i]] += 1
        for i in range(len(s)):
            if dct[s[i]] == 1:
                return i
        else:
            return -1
