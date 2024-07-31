from typing import List

nums1 = [3,0,1]
nums2 = [0,1]
nums3 = [9,6,4,2,3,5,7,0,1]

# Brute force
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

       arr = self.sortArray(len(nums), nums)

       for i in range(0, len(arr)):
          if(arr[i] != i):
              return i
        
       return len(arr)

    def sortArray(self, n:int, nums: List[int])->List[int]:
        for i in range(0,n):
            for j in range(i+1, n):
               if(nums[i]>nums[j]):
                  temp = nums[i]
                  nums[i] = nums[j]
                  nums[j] = temp

        return nums          

solution = Solution()
print(solution.missingNumber(nums1))
print(solution.missingNumber(nums2))
print(solution.missingNumber(nums3))