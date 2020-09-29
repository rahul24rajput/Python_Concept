# Given an array arr[] of n integers, construct a Product Array prod[] 
# (of same size) such that prod[i] is equal to the product of all the elements of arr[] except arr[i]. 
# Solve it without division operator and in O(n).

# https://www.geeksforgeeks.org/product-array-puzzle-set-2-o1-space/
def solve(arr, n):
    prod = 1
    for i in range(n):
        prod = prod*arr[i]
    print(prod)
    for i in range(n):
        arr[i] = int(prod*(arr[i]**-1))
    print(arr)
 
	



arr = [10, 3, 5, 6, 2] 
n = len(arr) 
solve(arr, n) 
