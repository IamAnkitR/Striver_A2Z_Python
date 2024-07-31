from typing import List

def secondLargest(arr: List[int]):
    largest = arr[0]
    secondLargest = 0

    for i in range(1, len(arr)):
        if(arr[i]> largest):
            secondLargest = largest
            largest = arr[i]
        elif(arr[i]<largest and arr[i]>secondLargest):
            secondLargest = arr[i] 

    return secondLargest


arr = [10,20,44,32,59,78]

print(secondLargest(arr))

