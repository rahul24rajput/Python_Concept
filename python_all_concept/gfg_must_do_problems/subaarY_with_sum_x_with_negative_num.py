# Find subarray with given sum | Set 2 (Handles Negative Numbers)
# https://www.geeksforgeeks.org/find-subarray-with-given-sum-in-array-of-integers/





# Function to print subarray with sum as given sum 
def subArraySum(arr, n, Sum):
    curr_sum = {}
    
    for i in range(n):
        sum = sum+arr[i]
        curr_sum.append(sum)

        if(curr_sum-Sum) in curr_sum:
            

arr = [10, 2, -2, -20, 10] 
n = len(arr) 
Sum = -10
	
subArraySum(arr, n, Sum) 
	

