# For a given array, find the largest element in it
# [2,3,45,98,10] --> Output : 98

from typing import List

arr = [2,3,45,98,10]

def findLargest(n:int, arr: List[int]):
    largest = arr[0]
    for i in range(1,n):
        if(arr[i]>largest):
            largest = arr[i]

    return largest
        


print(findLargest(5, arr))
