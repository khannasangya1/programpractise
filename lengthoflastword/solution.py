class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        space = " "
        indxofspace = 0
        if s == "" or s == None:
            return 0

        if len(s)-1 == space:
            return 0
        if s == " ":
            return 1


        for counter in range(len(s)-1,-1,-1):
            if s[counter] == space:
                indxofspace = counter
        if indxofspace > 0:
            lngth_lstwrd = len(s) - 1 - indxofspace
            return lngth_lstwrd
        else:
            return len(s)





if __name__ == "__main__":
    object = Solution()
    output = object.lengthOfLastWord(" ")
    print(output)
