#variablescope= where variable is visible and accessible
#scope resolution =  (LEGB) Local-->Enclosed-->global--> built in
from textwrap import dedent


# Variable declared inside function have local scope
#Variable a is local to function 1 and variable b is limited to function2

def func1():
    a = 1
    print(a)

def func2():
    b= 2
    print(b)

func1()
func2()

#Function declared in another function  --> Enclosed
#So here local variable will be used that is x=2 then x=1 which is enclosed variable

def func1():
    x = 1

    def func2():
        #x = 2
        print(x)

    func2()

func1()


#Global Scope: Variable Outside any function
z = 6

def func1():
    print(z)

def func2():
    print(z)

func1()
func2()


#built in
from math import e

def func():
    print(e)    

func()