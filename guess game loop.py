#looping guess game
secret_word="akshat"
guess=""
count=0
limit=3
out_of_guess=False
while(guess!="akshat" and not(out_of_guess)):
    if (limit > count):
        guess = input("enter your guess for my name: ")
        count = count + 1
    else:
        out_of_guess=True
if(out_of_guess):
    print("you are out of guesses You Lose")
else:
    print("You WON ! correct guess.")