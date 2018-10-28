class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re

        ret = re.match(r"[^-+\d]*([-]?[\d]+)", str)
        if ret:
            print(ret.group(1))
            if ret.group()[0].isdigit() or ret.group(1)[0] == "-" or ret.group(1)[0] == "+" or ret.group(1).isdigit():
                if int(ret.group(1)) > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                elif int(ret.group(1)) < -2 ** 31:
                    return -2 ** 31
                else:
                    return int(ret.group(1))
            else:
                return 0
        else:
            return 0


test = "words and 987"
print(Solution().myAtoi(test))