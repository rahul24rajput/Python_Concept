# recursive function
# def fact(n):
#     if n == 0:
#         result =1
#     else:
#         result=n*fact(n-1)

#     return result

# x = fact(3)
# print(x)
# ____________________________________________________
# python allow max recursion depth till 998 times.

# ___________________________________________________
# count = 0
# def call_me(n):
#     global count
#     count = count+1
#     if n==0:
#         x = 1
#     else :
#         x= n+call_me(n-1)
#     return x

# print(call_me(998))  # O/P -- Error RecursionError: maximum recursion depth exceeded
# print(count)

#___________________________________# Anonymous function#_______________________________________________________


# anyonums function are used only only for one time use. also named as lambda functiom
# NAmeless function

# how to write lambda function define below 
# def squareit(n):
#     return n*n

# can be written as in lambda as

# lambda input arg : return Value

# x = lambda n:n*n  #  lambda function for getting square

############### calling lambda function
# s = lambda a,b: a+b
# print(s(10,20 ))

################ lambda function for finding two bigger number

# great = lambda a,b : a if a >b else b
# print(great(5,32))

#########function as argument to another functiom  
# filter , map ,reduce they will always take function as argument

############################  filter function#########################################
# if you wana to have top 5 student in 100 student class. then you
# can use filter function

# filter definitation 
# _________________________________________________________________
# filter (function, sequence)
# 1 arg --- fiunction 
# 2 arg --- from wich sequence we need to filter



# filter only even function
# l = [0,1,2,3,4,5,6,7,8,9]
# # case 1  without filter  functionn
# def iseven(n):
#     if n%2==0:
#         return True
#     else:
#         return False          # normal program to find even program

# l1 = []
# for i in l:
#     x =iseven(i)
#     if x:
#         l1.append(i)
# print(l1)

# using the same program with filter function

# l = [0,1,2,3,4,5,6,7,8,9]

# l1 = filter(iseven,l)  # return type of filter function is filter object only
# print(list(l1))  # has to covert to list object so the value can be gets.

#______________________________________________________________________________________filter with lambda function _____________________________________________________________
# l = [0,1,2,3,4,5,6,7,8,9]

# l1 = filter(lambda i:i%2==0, l)
# print(list(l1))
# EX-------------------1
# take the number which are divisble by 3 and odd: using lambda and filter function
# l = [0,1,2,3,4,5,6,7,8,9]

# val =filter(lambda x: x%3==0 and x%2!=0, l)
# print(list(val))

# ex------2
# write a lambda function weather the name start with k or not
# heroiens = ['Katrina', 'Kareena', 'anushka', 'deepeika', 'Sunny leone'] 

# name = filter (lambda a: a[0]=='K', heroiens)
# print(list(name))

#name kength is divisble by 5
# heroiens = ['Katrina','akaka', 'Kareena', 'anushka', 'deepeika', 'Sunny leone'] 
# name_len = filter(lambda a:len(a)%5==0, heroiens)
# print(list(name_len))

#_________________________________________________________________________________________MAP_)______________________________________________________________________________________
# To generate new values by doing some manipulation or modification 

# in map in input contain 5 element then output should contain 5 element too
# l = [1,2,3,4,5]
# map function for getting square the list
# def squareit(l):
#     return l*l

# k=map(squareit, l) # It will take input as l and iterate over it and send the value to square function
# print(list(k))

#### using lambda function

# lamb = map(lambda a : a*a, l)
# print(list(lamb))


# EX _________________ 2 
# l1 = [1,2,3,4,5]
# l2 = [5,10,15,20,12]

# requirement needed output like [1*5 = 5, 10*2=20, 15*3=45, 20*4=80 .... ]
# so for this use map function

# mul_of_l1_and_l2 = map(lambda a,b : a*b, l1,l2) # here lambda function is taking two input instead of one
# print(list(mul_of_l1_and_l2))

# _______________________________________________________________________REDUCE_______________________________________________________________________________

# filter  if input 10  elements  then output <=10 elements
# map     if input 10 elements then output =10  elements
# reduce if input 10 elements then output =  1 elements
# reduce is not inbuilt function has to be import explictily
# from functools import reduce
# l = [10,20,30,40,50]

# x = reduce(lambda a,b:a+b, l) 
# print(x)
####################################################################################################################
# __________________________________________________________MODULE________________________________________________
#####################################################################################################################
# module naming conflicts
# if two module is having same function then which module function will be imported ?
# from module1 import add
# from module2 import add

# so here module2 add function will be imported. this will override the first one module function 
# so for using both function we can do like this

# import module1
# import module2
# OR__________________________
# form module1 import add as a1
# from module2 import add as a2 
# a1(10,20) ------------------------> from module 1
# a2(20,30)-------------------------> from module 2
##############################################################################################################################
#################################  FINDING MEMBER OF MODULE BY USING DIR() FUNCTION ##########################################
##############################################################################################################################

# DIR() -- list out all members of current module
# DIR(module) -- list out all members of specified module
# # return type of module is list  
# dir function just list out all members of the given module
# help function provides document related to that module
# import math
# print(dir(math))
# OUTPUT
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'fact
# orial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh',
#  'sqrt', 'tan', 'tanh', 'trunc']

# print(help (math))
# output =================================
# NAME
#     math

# DESCRIPTION
#     This module is always available.  It provides access to the
#     mathematical functions defined by the C standard.

# FUNCTIONS
#     acos(...)
#         acos(x)
        
#         Return the arc cosine (measured in radians) of x.
# inbuilt variable added by python interpreter for uses


# default module member added to printython module
# ex -- 
# __doc__,  contains builtin document
# __file__, it will let you know that in which file module exist
#########################################################################################################################################333
########################################################### __name__ ####################################################################33
###########################################################################################################################################

#  if i defined a module like this below 

#### file named as module1.py 
# def f1():
#     pass
# def f2():
#     pass
# def f3():
#     pass
# f1()
# f2()
# f3()

# and in my different file names as test.py i have imported module1.py like below
#import module1  ## Only this line will execute the function f1,f2,f3 in mudule1.py bcz we are importing module1 just bcz of import statement
#module1.f1()  ## again this line will execute the f1()

# so i dont want f1,f2 and f3 function be executed means i dont want total module to be executed. so for that this below condition needs to be 
# done

# def f1():
#     pass
# def f2():
#     pass
# def f3():
#     pass

# if __name__ == '__main__':
#     f1()
#     f2()
#     f3()
# so now if anyone executig directly this module1 then only called f1,f2 and f3
# and this is being called indirectly or from other file then dont execute f1,f2 and f3

########################################################################################################################
############################################################## MATH MODULE #############################################
########################################################################################################################

# import math 
# print(fabs(-10.6)) o/p will nbe 10.6 absolute means dont consider the -ve sign just see the value

# in choice () ypu can pass indexible sequences , like list, tuplle and string but dict and set can not be passed bcz. no order is mainted  
# from random import *
# digits = '789564123'
# for i in range(5):
#     print(choice(digits))

# $ generating a randon password with alternative sequence of numner and alphabet
# from random import *
# alaphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# NUMER = '0123456789'
# print(choice(alaphabet),choice(NUMER),choice(alaphabet),choice(NUMER),choice(alaphabet),choice(NUMER),sep='')
# O/P -------------- >>>> L7K7W5

######################################################################################################################################################################
###########################`##################################### PYTHON PACKAGES #####################################################################################
######################################################################################################################################################################
# a grp of related module is called package 
# if you want to consider any folder or directory consider as a package then should contain ####  __init__.py  #### then the folder will consider as python package.
# using package we can reslove naming conflicts, 

# at the time of using a package if we want to perform activity automatically then we have to define that activity inside
# this     __init__.py 
# Hemce __init__.py meant for initalize activity
# if i write anything inside the init package then it will bw automatically executed.

###################################################################################################
##################################################  sep ##########################################3]
#####################################################################################################

# by defaulr print output comes with space seprator
# so this can be given explictily
# a,b,c = 10,50,60
# print(a,b,c, sep=',')
# o/p --  10,50,60
# print(a,b,c)
# o/p --  10 50 60
###########################################################################
################ FOR - ELSE. ################################################
#############################################################
for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything..
    not_found_in_container()
