arr = [1,7,6,9,5,3,2,4,8,0]

def merge_sort(arr):
    if len(arr)>1:
        L_arr = arr[:len(arr)//2]
        R_arr = arr[len(arr)//2:]
        
        #recursion
        merge_sort(L_arr)
        merge_sort(R_arr)
     
        #merge
        i = 0 #left arr idx
        j = 0 #right arr idx
        k = 0 #merged arr idx
        while i<len(L_arr) and j<len(R_arr):
            if L_arr[i]<R_arr[j]:
                arr[k]= L_arr[i]
                i += 1
            else:
                arr[k]= R_arr[j]
                j += 1
            k += 1
        
        while i < len(L_arr):
            arr[k]=L_arr[i]
            i +=1
            k += 1
        
        while j < len(R_arr):
            arr[k]=R_arr[j]
            j +=1
            k += 1

merge_sort(arr)
print(arr)