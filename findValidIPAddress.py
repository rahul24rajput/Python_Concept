import re

# 4 numbers seprated by .
# [0-99].[100-199].[200-249].[250-255]

# [0-9][0-9]?
# 1[0-9][0-9]
# 2[0-4][0-9]
# 25[0-5]


# ^ ====> it will strictly start from here
# $ =====> it will strictly ends here

# ^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\.
# (25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\.
# (25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\.
# (25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)$



# importing the module 
import re 

# opening and reading the file 
with open('dummy.txt') as fh:
    string = fh.readlines() 
	
# declaring the regex pattern for IP addresses 
pattern =re.compile('^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)$')

# initializing the list objects 
valid =[] 
invalid=[] 

# extracting the IP addresses 
for line in string:
    line = line.rstrip()

    result = pattern.search(line) 
	# valid IP addresses 
    if result:
        valid.append(line)
    else:
        invalid.append(line) 

# displaying the IP addresses 
print("Valid IPs") 
print(valid) 
print("Invalid IPs") 
print(invalid) 



