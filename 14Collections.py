# Collection: Single variable used to store multiple values

# List = [] Ordered and changeable. Duplicates OK
# Set = {} Unordered and immutable, but ADD/REMOVE Ok. No Duplicates
#Tuple = () ordered and unchangeable, Duplicates OK, faster

#-------------Lists----------------------------

fruits = ["Apple", "Banana", "Orange", "Kiwi"]

#print(dir(fruits))
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'


#Description of available functions
#print(help(fruits))


#Length of fruits

print(len(fruits))


# To find a value in list and other collections tuples,set
print("Apple" in fruits)

#Index starts with 0
#print(fruits[1])
#print(fruits[0:2])

# Explicitly assigning fruits[0] = "Pineapple" , so at 0 index the value of apple will change to pineapple


#fruits.append("Guava")  -->The append() method appends an element to the end of the list.
#fruits.remove("Apple")  -->The remove() method removes the first occurrence of the element with the specified value.
#fruits.insert(2,"Lime") --> The insert() method inserts the specified value at the specified position.
#fruits.sort() -->The sort() method sorts the list ascending by default.
#fruits.reverse() -->The reverse() method reverses the sorting order of the elements.
#fruits.clear() --> The clear() method removes all the elements from a list.
#print(fruits.index("Apple"))  -->Returns the index of the first element with the specified value
#print(fruits.count("Apple")) -->The count() method returns the number of elements with the specified value.
#fruits.pop(1) -->The pop() method removes the element at the specified position.
for fruit in fruits:
    print(fruit)


#------------------------Sets-------------------
#Unordered, immutable, no duplicates

fruits = {"apple","banana","coconut","orange","orange"}

print(fruits)

#The values are unordered can change in every execution

#print(dir(fruits))
#print(help(fruits))
print(len(fruits))
print("Apple" in fruits)

#No Indexing

#fruits.add("Pineapple")  --> add()	 	Adds an element to the set
#fruits.remove("apple")   -->Removes the specified element
#fruits.pop()               -->pop()	 	Removes an element from the set (Random)
#fruits.clear()   -->	Removes all the elements from the set
print(fruits)


#------------------------Tuple-------------------
#ordered and unchangeable, Duplicates OK, faster than list
#Tuples are faster than lists in Python primarily due to their immutability.
# Once a tuple is created, its contents cannot be modified, whereas lists are mutable,
# allowing for changes like adding or removing elements

fruits = (("apple","kiwi","coconut","coconut","lime"),("apple","banana","coconut","coconut","lime"))
print(fruits)
print(fruits[1])
#Not many methods
#print(fruits.count("coconut"))
#print(fruits.index("coconut"))