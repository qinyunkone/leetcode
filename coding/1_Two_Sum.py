class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        # 穷举法
        # for i, v1 in enumerate(nums):
        #     for j, v2 in enumerate(nums[i+1:]):
        #         if v1 + v2 == target:
        #             return [i, j+i+1]

        # 判断 target-v1 是否在 nums[i+1:]中
        # for i, v1 in enumerate(nums):
        #     if target - v1 in nums[i+1:]:
        #         return [i, nums[i+1:].index(target-v1)+i+1]

        # 使用哈希表查找 target-v1
        hashtable = dict()
        for i, v1 in enumerate(nums):
            if target - v1 in hashtable:
                return [hashtable[target - v1], i]
            else:
                hashtable[v1] = i
        return []
