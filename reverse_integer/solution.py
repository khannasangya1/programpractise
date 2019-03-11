class Solution(object):
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        while x >0:

            rem = x % 10
            x = x // 10
            rev = rev * 10 + rem
        return rev



if __name__ == "__main__":
    a = Solution.reverse(567)
    print(a)