import random

arr = [x**2 for x in range(1,20)]
random.shuffle(arr)


for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]


print(arr)