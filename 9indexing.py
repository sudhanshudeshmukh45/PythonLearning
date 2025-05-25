#Indexing: Accessing elements of sequence using [] (Indexing Operator)
#          [start:end:step]

creditNumber = "0897-3739-2111-4444"

a = creditNumber[0:4]
print(a)

b = creditNumber[0:5]
print(b)

c = creditNumber[::2]
print(c)

d = creditNumber[::-1]
print(d)

e = creditNumber[-4:-2]
print(e)


last_digits = creditNumber[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")