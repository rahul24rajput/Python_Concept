# Python3 code for Find the two repeating 
# elements in a given array 

# Method 1 using minus (-)  karke 
def printRepeating(arr, size):
    for i in range(size):
        arr[arr[i]] = arr[arr[i]]*-1
        if arr[arr[i]]>0:
            print("repeting nu,m",arr[arr[i]])

# Driver code 
arr = [4, 2, 4, 5, 2, 3, 1] 
arr_size = len(arr) 
printRepeating(arr, arr_size) 
