class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSums = [0] * (n+1)
        for i in range(n):
            prefixSums[i+1] = prefixSums[i] + nums[i]
        
        for i in range(n):
            leftSum = prefixSums[i]
            rightSum = prefixSums[n] - prefixSums[i+1]
            if leftSum == rightSum:
                return i
        return -1 
        