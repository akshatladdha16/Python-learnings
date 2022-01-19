#program to convert any vowel in a phrase or list to g
def translator(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation=translation+letter
    return translation
phrase=input("enter the phrase to get coded translation: ")
result=translator(phrase)
print(result)

