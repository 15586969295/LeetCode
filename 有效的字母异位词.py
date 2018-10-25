# Given two strings s and t , write a function to determine if t is an anagram of s.
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted("".join(s)) == sorted("".join(t))
