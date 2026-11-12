class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        # for each number in nums we need index
        for i in range(len(nums)):
            # if complement exists
                comp = target - nums[i]
                if comp in result:
                # return sorted indexes
                    return sorted([result[comp], i])
                # else
                else:
                    # add value, index to results
                    result[nums[i]] = i
        