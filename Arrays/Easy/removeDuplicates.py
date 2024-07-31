from typing import List

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]
nums3 =  [9,9,10,11,11,11,11,12,13,14]

def removeDuplicates(nums: List[int]) -> int:
        left = 0

        for i in range(1, len(nums)):
            if(nums[left]<nums[i]):
                temp = nums[left+1]
                nums[left+1] = nums[i]
                nums[i] = temp

                left +=1
        
        print(nums[0:left+1])
        return left+1      

print(removeDuplicates(nums1))
print(removeDuplicates(nums2))
print(removeDuplicates(nums3))
