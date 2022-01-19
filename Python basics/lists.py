#lists
list1=["a","b","c","d","e","a","a"]
#indexing in lists or any string always starts from 0
print(list1)
print(list1[3])#how to access any particular value and -1 means 1st element from last
print(list1[1:])#it will print all from 2 to end (this is now index numbers keep in mind)

#list functions
luck_num=[2,3,14,4,5,6,7,8]
list1.append(luck_num)#this will add luck_num list to end of list1
list1.insert(0,"kelly")#to insert any object in middle to list
list1.remove("kelly")#removed the word kelly
print(list1.count("a"))
luck_num.sort()#for sorting any list in alphabetical or ascending order
print(luck_num)
#.reverse for reverse the complete order of the list
list2=list1.copy()
print(list2)

# Tuples
# its a type of datastructure similar to list which is inmutable means can't change this value later
coordinates=[(4,5),(4,4)]
# coordinates[1]=10   #   here we will get error that we cannot change tuple
print(coordinates)
# so its important to use when dealing with important data so that no one can change that
