#dictionary = a collection of {key:value} pairs, ordered and changeable . No Duplicates

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "France":"Paris"}


#print(dir(capitals))
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
print(help(capitals))

#print(capitals.clear())  -->clear()	Removes all the elements from the dictionary


#get()	Returns the value of the specified key
a = capitals.get("USA")
print(a)

#pop()	Removes the element with the specified key
capitals.pop("India")
print(capitals)

#popitem()	Removes the last inserted key-value pair

capitals.popitem()
print(capitals)

#values()	Returns a list of all the values in the dictionary

print(capitals.values())

#keys()	Returns a list containing the dictionary's keys
print(capitals.keys())


#update()	Updates the dictionary with the specified key-value pairs
capitals.update({"Germany":"Berlin"})
print(capitals)


#items()	Returns a list containing a tuple for each key value pair

print(capitals.items())

for key,value in capitals.items():
    print(f"{key}:{value}")
