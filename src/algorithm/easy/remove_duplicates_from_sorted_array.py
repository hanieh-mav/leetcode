class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        if not len(nums):
            return 0

        pointer_1, pointer_2 = 0, 1
        counter = 1
        while pointer_1 is not None and pointer_2 is not None and not (
                pointer_1 == len(nums) or pointer_2 == len(nums)):
            if nums[pointer_1] == nums[pointer_2]:
                pointer_2 += 1
            if nums[pointer_1] < nums[pointer_2]:
                pointer_1 += 1
                nums[pointer_1] = nums[pointer_2]
                counter += 1
                pointer_2 += 1

        return counter +1
