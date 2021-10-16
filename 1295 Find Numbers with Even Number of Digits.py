# Link to the problem statement > https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def countDigits(self, num):
        cnt = 0
        while num > 0:
            cnt += 1
            num //= 10
        return cnt
    
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if self.countDigits(i) % 2 == 0:
                res += 1
        return res
