class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for x in range(len(nums)-1,-1,-1):
            if nums[x] == target:
                element_removed = nums.pop(x)
                return x
        if target > nums[len(nums)-1]:
            index = len(nums)
            return index
        if target < nums[0]:
            index = 0
            return index

        for x in range(len(nums)-1,-1,-1):
            if target < nums[x] and target > nums[x-1]:
                index = x

                return index


if __name__ == "__main__":
    object = Solution()
    output = object.searchInsert([2,3,5],4)
    print(output)

