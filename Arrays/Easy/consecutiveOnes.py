from typing import List

nums1 = [1,1,0,1,1,1]
nums2 = [1,0,1,1,0,1]
nums3 = [1,1,0,1]
nums4 = [1,1,0,1,0,0,1,1]
nums5 = [1,1,0,1,1,1,1,0]
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currentCount = 0

        left = 0
        
        if(len(nums)==1 and nums[0] == 1):
            return 1

        for num in nums:
             if num == 1:
                currentCount += 1
                maxCount = max(maxCount, currentCount)
             else:
                currentCount = 0
        return maxCount   
    
solution = Solution()

print(solution.findMaxConsecutiveOnes(nums1))
print(solution.findMaxConsecutiveOnes(nums2))
print(solution.findMaxConsecutiveOnes(nums3))
print(solution.findMaxConsecutiveOnes(nums4))
print(solution.findMaxConsecutiveOnes(nums5))