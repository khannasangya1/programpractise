class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = []

        for char in s:
            if char in left:
                stack.append(char)
            elif char in right:
                if len(stack) <= 0:
                    return False
                popped_char = stack.pop()
                if left.index(popped_char) != right.index(char):
                    return False
        print(len(stack))
        if len(stack) != 0:
            return False


if __name__ == "__main__":
    object = Solution()
    #output = object.isValid('{()}')
    output = object.isValid('()')
    print(output)


