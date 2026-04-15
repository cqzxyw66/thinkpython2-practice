class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if not nums:
            return 0

        fast = slow = 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast +=1
        return nums[:slow]
    
a = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(a))
print(a)