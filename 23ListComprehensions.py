#List Comprehension = A concise way to create lists in Python
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]



#Traditional
doubles = []

for x in range(1,11):
    doubles.append(x*2)

print(doubles)


#List Comprehension
doubles = [x * 2 for x in range(1,11)]

print(doubles)

fruits = ["apple","kiwi","orange"]

fruits = [fruit.upper() for fruit in fruits]
print(fruits)

#First Character of each string

fruits = ["apple","kiwi","orange"]

fruits = [fruit[0] for fruit in fruits]
print(fruits)


numbers = [2,3,5,6,12]

even_nums = [number for number in numbers if number % 2 == 0]
    #[numbers[i] for i in range(0,len(numbers)) if numbers[i]%2==0]
print(even_nums)


grades = [55,66,90,100,34,62,77]

passed_exam = [num for num in grades if num >=75]

print(passed_exam)