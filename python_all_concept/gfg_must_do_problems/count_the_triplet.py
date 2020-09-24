def findTriplet(arr, n):
    arr.sort()
    count = 0
    for i in range(n):
        k = n-1
        j = 0
        # print(i,k,j)
        while (k>j):
            if arr[i] == arr[j]+arr[k]:
                return "got the number{}{}{}".format(arr[i] ,arr[j],arr[k])  
            if arr[i]>arr[j]+arr[k]:
                j = j+1
            if arr[i]<arr[j]+arr[k]:
                k = k-1
            

# driver program 
arr = [ 5, 32, 1, 7, 10, 50, 19, 21, 2 ] 
# [1, 2, 5, 7, 10, 19, 21, 32, 50]
n = len(arr) 
print(findTriplet(arr, n))

