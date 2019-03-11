class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)


if __name__ == "__main__":
    object = Solution()
    output = object.removeDuplicates([1,2,2])
    print(output)







