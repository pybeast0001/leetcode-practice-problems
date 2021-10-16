# Link to the problem statement > https://leetcode.com/problems/contains-duplicate/submissions/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return True
        return False
