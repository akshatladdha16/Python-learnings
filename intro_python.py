print("hello world this is my first python code")

# variables and datatypes
name='john'
age=48
print(name,"and his age is" ,age)

# working with strings
print("giraffe\nacademy")#\n for new line
phrase="this is string phase and can be used later"
print(phrase.lower().isupper())#phrase.upper() .upper is function to be run in phrase
#isupper() this will give us true or false value if that phrase is upper case or not so using is before anyfunction checks its accesbility
print(len(phrase))#len is lenght of string function
print(phrase.index("g"))#index function gives us where a particular things is present in string
print(phrase.replace("this","that"))

#working with numbers
print(3+5.6)
num=48
print(str(num)+" is my fav number")#str function allow us to print number alongisde of any phrase otherwise it will throw error
#abs abs(num) will give absolute value
#pow(3,2) power function it will be 3 raised to power 2
#max(4,6) gives max of all numbers
#round(3.992) will round it to 4
# these are some of the math functions already avaible in python but to include more of that we need to add math library
from math import *
print(floor(3.7))#chop off the decimal number
print(ceil(3.1))#it will give us the next int irrespective of decimal
print(sqrt(36))#give square root

#getting input from users
name_ip=input("enter your name: ")
age_ip=input()
print("hello , welcome to my code "+name_ip,"and your age is "+age_ip)

#basic calculator prject
num1=input("enter a number : ")
num2=input("enter second number : ")
result=float(num1)+float(num2)
#here we used float because when we store something it always stored as string so to perform op on that we have to convert it to int or float
print(result)

#mad libs game
color=input("enter color name: ")
noun=input("enter noun:" )
celeb=input("enter celeb name:")
print("roses are "+ color)
print(noun+" are blue")
print("i love "+celeb)



