import multiprocessing
result = []
def calc_square(numbers):
    global result
    for n in numbers:
        result.append(n*n)
    print("inside process"+str(result))

if __name__=="main":
    numbers=[2,3,4]
    p=multiprocessing.Process(target=calc_square,args=(numbers))
    p.start()
    p.join()

    print("outside process"+str(result))
#Now this program will print
#    iside process[4 9 25]
#    outside process[]
# so here the actual thing is global result variable is not shareble to other process.
#Beacuse in multiprocess variable are not shared
#whenever u create a new process the new process will get its own address space
#Address space ---> Meaning the soace where it stores all the variable
#so for  Sharing Data Between Processes we have to Use Array 
