def length(string):
    count = 0
    for i in string:
        if(i==""):
            count =0
        else:
            count=count+1    
            return count
           
if __name__ == "__main__":
    a=input()
    print (length