
def sortInWave(a, n): 
    for i in range(0,n,2):
        # print(i)
        if i>0 and a[i]<a[i-1]:
            a[i],a[i-1] = a[i-1],a[i]
        if i<n-1 and a[i]<a[i+1]:
            a[i],a[i+1]= a[i+1],a[i]
    return a



# Driver program 
arr = [10, 90, 49, 2, 1, 5, 23] 
x = sortInWave(arr, len(arr)) 
print(x)


