from typing import List
from bisect import bisect_left

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        larr, narr = sorted(nums), []
        for num in nums:
            i = bisect_left(larr,num)
            narr.append(i)
            del larr[i]

        return narr

ss = Solution()

print(ss.countSmaller([5,2,6,1]))
print(ss.countSmaller([-1]))
print(ss.countSmaller([-1,-1]))
