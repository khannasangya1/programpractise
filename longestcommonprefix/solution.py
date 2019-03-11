class Solution(object):
    def longestCommonPrefix( self,strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        common = strs[0]
        for s in strs:
            while len(common) > 0 and common not in s[:len(common)]:
                common = common[:-1]
            if len(common) == 0:
                break

        return common

if __name__ == "__main__":
    v = Solution()
    a = v.longestCommonPrefix(['none','non2'])
    print(a)
