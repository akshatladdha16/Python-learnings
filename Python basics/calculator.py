# advanced calculator
num1=float(input("enter 1st number: "))
num2=float(input("enter 2nd number: "))
op=input("enter operation : * , + , - , % , / ")
def calculator(num1,num2,op):
    if(op=='*'):
        return num1*num2
    elif(op=='+'):
        return num1+num2
    elif(op=='-'):
        return abs(num1-num2)
    elif(op=='%'):
        return num1%num2
    elif(op=='/'):
        return num1/num2
result=calculator(num1,num2,op)
print(result)
