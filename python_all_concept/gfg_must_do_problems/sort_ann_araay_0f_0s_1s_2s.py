# # Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that
# # sorts the given array. The functions should put all 0s first, then all 1s and all
# # 2s in last
# # https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

def sortArr(arr, n):
    count_0 =0
    count_1 =0
    count_2= 0
    j = 0
    
    for i in range(n):
        if arr[i] == 0:
            count_0 = count_0+1
        if arr[i] == 1:
            count_1 = count_1+1
        if arr[i] == 2:
            count_2 = count_2+1

    while(count_0>0):
        arr[j] = 0
        j = j+1
        count_0 = count_0-1
    
    while(count_1>0):
        arr[j] = 1
        j = j+1
        count_1 = count_1-1
    
    while(count_2>0):
        arr[j] = 2
        j = j+1
        count_2 = count_2-1
        
    return arr
	

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
n = len(arr) 

print(sortArr(arr, n))


