# Link to the problem statement > https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        i = 0
        n = len(nums)
        while i < n:
            cnt = 0
            while i < n and nums[i] == 1:
                cnt += 1
                i += 1
            if cnt > res:
                res = cnt
            i += 1
        return res
