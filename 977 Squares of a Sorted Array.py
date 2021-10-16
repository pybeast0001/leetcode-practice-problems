# Link to the problem statement > https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg_squares = list()
        i = 0
        while i < len(nums) and nums[i] < 0:
            neg_squares.append(nums[i]**2)
            i += 1
        neg_squares.reverse()
        
        pos_squares = list()
        while i < len(nums):
            pos_squares.append(nums[i]**2)
            i += 1
            
        res = list()
        n_len = len(neg_squares)
        p_len = len(pos_squares)
        
        i = 0
        j = 0
                
        while i < n_len and j < p_len:
            if neg_squares[i] < pos_squares[j]:
                res.append(neg_squares[i])
                i += 1
            elif pos_squares[j] < neg_squares[i]:
                res.append(pos_squares[j])
                j += 1
            else:
                res.append(pos_squares[j])
                res.append(neg_squares[i])
                i += 1
                j += 1
        
        while i < n_len:
            res.append(neg_squares[i])
            i += 1
        while j < p_len:
            res.append(pos_squares[j])
            j += 1
        
        return res
