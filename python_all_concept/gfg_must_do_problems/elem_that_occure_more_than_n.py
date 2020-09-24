# Python program for finding out majority 
# element in an array 

def findMajority(arr, size):
    k = 0
    count = 1
    for i in range(1,size):
        if arr[k]==arr[i]:
            count = count+1
        else:
            count = count-1
        if (count==0):
            k = i
            count = 1
    check_max(arr[k],arr,size)

def check_max(num,arr,size):
    # print("checkmax")
    max_c = 0
    for j in range(size):
        if num == arr[j]:
            max_c = max_c+1
    # print("-----",max_c,size//2,num)
    if (max_c>size/2):
        print("we got the number {}".format(num))
    else:
        print(" ma chudao")


# Driver code 
arr = [2, 2, 2, 3, 5, 2, 2, 3, 3] 
# arr = [ 1, 3, 3, 1, 2]
n = len(arr) 

# Function calling 
findMajority(arr, n) 
