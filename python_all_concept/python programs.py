# s = input('enter the string')

# st = s.split()
# s1=''
# # x=0
# for x in range(len(st)):
#     print(x)
#     x=x+1

# for i in len(st):
    # print(i)
#     if i%2==0:
#         s1.append(st[i][::-1])
#     else :
#         s1.append(st[i])
# print(s1)
#_-------------------------------
# input: ABAABBCA
# output: 4a3b2c
# d = {}
# s = 'ABAABBCA'
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for k,v in sorted(d.items():
#     # print('{}{}'.format(v,k),end='')
#     print('{}{}'.format(k,v),end='')
#======================================================
# find count the occurence of key
#first way
# s='ABCDABXXXBCDABBBBCCCZZZZCDDDDEEEEXxEF'
# d={}
# for i in s:
#         d[i]= d.get(i,0)+1
# for k,v in d.items():
#     print('{}:{}'.format(k,v),end =' ')
# output ==== C:6 E:5 F:1 x:1 Z:4 D:6 A:3 B:7 X:4
#secnd way
# s='ABCDABXXXBCDABBBBCCCZZZZCDDDDEEEEXxEF'
# d = {}
# for i in s:
#     if i in d:
#         d[i] = d[i]+1
#     else:
#         d[i] =  1
# for k,v in d.items():
#     print('{}:{}'.format(k,v),end=' ')

# output ==== C:6 E:5 F:1 Z:4 A:3 x:1 D:6 B:7 X:4
#---------------------------------------------------

# s=input('Enter some string to search for vowels:')
# v=['A','E','I','O','U','a','e','i','o','u']
# d = {}
# for i in s:
#     if i in v:
#         d[i] = d.get(i,0)+1
# for k,v in d.items():
#     print('{} occurs {} times'.format(k,v))
######################################################################################################################################
#################################################################  split function ###############################################33
##################################################################################################################################
# a,b  = input('enter the num').split(',')
# print(a,b)
# note when you eill give input give like below
# by default split funcrion takes space as parameter
# 10,30

################################################################## cmd arguments ###################################################33
# Note2: Within the Python program command line arguments are available in the String
# form. Based on our requirement,we can convert into corresponding type by using type
# casting methods.

######################################################  
