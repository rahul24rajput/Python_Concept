# Maximum difference between two elements such that larger element appears after the smaller number

def maxDiff (arr, n):
    max_diff = 0
    small_elem = arr[0]

    for i in range(n):
        if small_elem>arr[i]:
            small_elem = arr[i]
            # print("******",small_elem,)
        if arr[i]>  small_elem:
            max_diff = arr[i]-small_elem
            # print("------",max_diff,arr[i])
    return max_diff,arr[i],small_elem
        
# arr = [80, 2, 6, 3, 100]
# arr = [1, 2, 90, 10, 110] 
# arr = [1, 2, 6, 80, 100] 
arr = [1, 2, 90, 10, 110] 
n = len(arr) 
print("Maximum difference is", maxDiff(arr, n)) 
