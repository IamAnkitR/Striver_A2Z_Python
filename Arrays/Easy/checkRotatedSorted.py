from typing import List
nums1 = [3,5,6,1,2]
nums2 = [1,2,3]
nums3 = [2,1,3,4]

def checkRotatedSorted(arr: List[int]):
   spike = 0

   if(arr[0]<arr[len(arr)-1]):
      spike +=1

   for i in range(1, len(arr)):
      if(arr[i]<arr[i-1]):
         spike+=1

   if(spike>1):
      return False
   
   return True

print(checkRotatedSorted(nums1))
print(checkRotatedSorted(nums2))
print(checkRotatedSorted(nums3))