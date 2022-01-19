# while loop concpet
i=2
while(i<=10):
    print(i)
    i=i+1#or we can write i+=1
print("done with loop")

# for loops concept
num=[1,2,56,13,9,6]
for num1 in range(3,10):#here num1 is the variable and range(3,10) 10 will not get included
    print(num1)
print("next loop")
for num2 in range(len(num)):
    if(num2==0):
        print("first one")
    else:
        print("not first")
print("next loop")

def exponent_funct(n,p):
    exp = 1
    x = 0
    for x in range(p):
        exp=exp*n
    return exp
# n=input("enter number: ")
# p=input("enter power to which u want to raise: ")
result=exponent_funct(3,3)
print("the final ans is "+str(result))