

string = "ABCDCDCDCDC"
substring ="CDC"
count = 0

a = len(substring)
for i in range(len(string)-a+1):
    if string[i:a+i]==substring:
        count+=1

print(count)

