#defaultarguments : A default value for certain parameters.
# Default is used when certain arguments is omitted.
#makes function more flexible , reduces # no of arguments
#positional 2. Default 3.Keyword 4.arbitrary


#Now in below function when we call function it will require 3 arguments, but most of the time
# we can say discount is constant and tax is constant for most of the customers let say,
# so in order to make function more flexible we will pass default value.

def net_price(list_price,discount=0,tax=0.05):
    return list_price * (1-discount) * (1 + tax)

print(net_price(200))

#Now this code can handle also other condition
#if some customer has different discount or tax, by just passing argument while calling function.
print(net_price(500,0.2,0.3))

#-----------------------------------------------------------------------------------------------------------------------


import time

# def count(start=0,end):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!!")
#
# count(1,10)

#Let say here user always want to begin at zero, so we can make it default but above code will
#throw error as parameter without a default follows parameter with a default. So it should be like
#below code


def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!!")

count(10,5)

#-----------------------------------------------------------------------------------------------------------------------
