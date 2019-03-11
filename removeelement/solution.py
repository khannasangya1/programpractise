class Solution(object):
    def removeElement( nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for x in range(len(nums)-1,-1,-1):
            if nums[x] == val:
                number_removed = nums.pop(x)
        print(nums)

        return len(nums)

if __name__ == "__main__":
    object = Solution()
    output = Solution.removeElement([3,2], 3)
    print(output)
