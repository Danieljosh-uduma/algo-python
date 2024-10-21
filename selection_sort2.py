arr = [1,6,3,4,2,5]

for i in range(0, len(arr)-1):
    cur_min_idx = i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[cur_min_idx]:
            cur_min_idx=j
    arr[i],arr[cur_min_idx]=arr[cur_min_idx],arr[i]
    
print(arr)