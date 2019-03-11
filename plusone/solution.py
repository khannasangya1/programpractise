class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits[len(digits)-1] <= 8:
            last_digit = digits[len(digits)-1] + 1
            digits[len(digits)-1] = last_digit
            return digits

        add_carryover = False
        firstTime= True
        for index in range(len(digits)-1,-1,-1):
            if digits[index] == 9 and firstTime:
                digits[index] = 0
                add_carryover = True
                firstTime =False
            elif digits[index] != 9 and add_carryover == True:

                digits[index] = digits[index] + 1
                add_carryover = False
            elif digits[index] == 9 and add_carryover == True:
                digits[index] = 0
                add_carryover = True

        if add_carryover == True:
            new_lst = [1]
            new_lst.extend(digits)
            return new_lst
        return digits


if __name__ == "__main__":
    object = Solution()
    output = object.plusOne([2,4,9,3,9])
    print(output)