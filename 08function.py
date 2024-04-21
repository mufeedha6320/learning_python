"""
#function hello
def hello():
    print("Helloo")

hello()

#function hey with one parameter
def hey(name):
    print("Welcome " + name)

value=input("Your name: ")
hey(value)

def hoi(*values):
    print("first value: "+values[0])
    print("last value: "+values[-1]) 

hoi("anu","mufi","bas","sne")

"""

def addition(a,b):
    return(a+b)
x=int(input("no1: "))
y=int(input("no2: "))
z=addition(x,y)
print(z)
