square_list=[]
def cal_square(number):
  global square_list ###defining the variable as global so we can use it outside
  for n in number:
    time.sleep(.5)
    print("square_result"+str(n*n))
    square_list.append(n*n)
Then call the function from outside
