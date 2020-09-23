
def subArraySum(arr,n,sum):
    k = 0
    target = 0
    for j in range(n): 
        if(target== sum):
            print("got the sum",arr[k],arr[j])
            print(k,j)
            exit()
        target = target+arr[j]
        print(target)
        while (target>sum):
            # 
            #     print("in while loop got sum")
            #     exit()
            #     print("got the sum",k,j)
            # 
            target = target-arr[k]
            if (target==sum):
                print("got the sum",k,j)
            k = k+1

# Driver program  
arr = [15, 2, 4, 8, 9, 5, 10, 23] 
n = len(arr) 
sum = 33
  
subArraySum(arr, n, sum) 

# def subArraySum(arr, n, sum): 
# 	curr_sum = arr[0] 
# 	start = 0 
# 	i = 1
# 	while i <= n: 
# 		while curr_sum > sum and start < i-1:
#             print("dede")
# 			curr_sum = curr_sum - arr[start] 
# 			start += 1
# 		if curr_sum == sum: 
# 			print ("Sum found between indexes") 
# 			print ("% d and % d"%(start, i-1)) 
# 			return 1
# 		if i < n: 
# 			curr_sum = curr_sum + arr[i] 
# 		i += 1

# 	print ("No subarray found") 
# 	return 0

# # Driver program 
# arr = [15, 2, 4, 8, 9, 5, 10, 23] 
# n = len(arr) 
# sum = 33

# subArraySum(arr, n, sum) 

# # This code is Contributed by shreyanshi_arun. 
