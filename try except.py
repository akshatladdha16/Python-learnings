num=int(input("enter a number: "))
print(num)
#everything will work fine if user enters a number
# problem arises when user enter wrong thing for eg a string in place of a number
# so we use try and except to not crashing our program
try:
    value= 10 / 0
    num=int(input("enter your number:"))
    print(num)
except ValueError:#it will take up any kind of error in try section
    # to make it specific to some errors make different excepts
    print("Invalid input")
except ZeroDivisionError as err:
    print(err)
    #so now err will give us the actual error from python and not actually crash our program