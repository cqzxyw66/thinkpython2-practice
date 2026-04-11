class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new_list = list()
            new_list.append(i)
            else_num = target - nums[i]
            try:
                a = nums.index(else_num, i+1)
            except:
                a = False
            while a:
                new_list.append(a)
                return new_list


a = Solution()
a_result = a.twoSum([3, 3], 6)
print(a_result)