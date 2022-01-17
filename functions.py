# colllection of code and also to organise our code
def say_hi(name,age):
    print("hello user your name is "+name+" your age is : "+str(age))#we always use str when we have to use any datatype other than char in print function
    #whqatever goes in these continous lines are considered as functions part
say_hi("akshat",24)
say_hi("mike",34)

def cube(n):
    cube=n*n*n
    return cube#we can use this return statement to get info from function
result=cube(4)
print(result)