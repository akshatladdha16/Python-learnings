# reading from external files eg text,html,csv etc
prediction_file=open("prediction.csv","r")
#  file name when present in same directory
# r= read mode ; a= append mode(can add info but cannot change existing ones); r+ = gives read and write allowance; w = overwriting everything in file
# and if u want to make a new file just have w in type and name a new file
print(prediction_file.readable())#this function tells us that file is readable or not
print(prediction_file.read())
#print(prediction_file.readlines())#this funct will put content in array
# print(prediction_file.write("")in this way you can add infoin file
prediction_file.close()# to close file its a good practice to close any file you open

