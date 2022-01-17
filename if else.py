# basics of if else statements
is_male=False
is_tall=False
if is_male and is_tall:
    print("you are a male and tall")
elif is_male and not(is_tall):
    print("you are a male but not tall")
elif not(is_male) and is_tall:
    print("you are not male but you are tall")
else :
    print("not male not tall")

# if else and comparisions
def max_num(num1,num2,num3):
    if(num1>=num2 and num1>=num3):
        print("num1 is biggest")
    maxi=max(num1,num2,num3)
    print(str(maxi)+" is the biggest of all")
max_num(2,4,1)


