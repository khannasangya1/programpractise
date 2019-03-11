class Solution(object):
    def strStr( haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(not haystack and not needle):
            return 0

        if haystack:
            if needle:
                len_needle = len(needle)
                for counter in range(0, len(haystack) - 1, 1):
                    sliced = haystack[counter:counter + len_needle]
                    if sliced == needle:
                        return counter
                return -1
            else:
                return 0
        else:
            return -1


if __name__ == "__main__":
    object = Solution()
    output = Solution.strStr("khanna","nn")
    print(output)





