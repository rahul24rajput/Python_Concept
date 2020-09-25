def equilibrium(arr):
    ar_sum = 0
    # get the total sum of the array
    for i in range(len(arr)):
        ar_sum = ar_sum+arr[i]
    # get the right sum and compare with left sum
    left_sum = 0

    # for i, num in enumerate(arr):
    #     print(i,num)    
    for j in range(len(arr)):
        
        ar_sum = ar_sum-arr[j]
        print("----------",ar_sum,left_sum)
        if ar_sum==left_sum:
            print(j)
            exit()
        left_sum = left_sum+arr[j]



# driver code 
arr = [-7, 1, 5, 2, -4, 3, 0] 
print (equilibrium(arr)) 

