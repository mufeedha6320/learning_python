num=int(input("Enter a number: "))
i=1
while(i<=num):
    print(i)
    i=i+1
else:
    print("loop finished\n")

    
"""

names=["mammu","mufee","sufi"]
i=0
while(i<len(names)):
    print(names[i])
    i=i+1
else:
    print("finished\n")
    
"""

#printing pattern of STARS

def triangle(n):
    s=n-1  #spaces
    #outerloop
    i=0
    while(i<n):
        #innerloop for spaces
        j=0
        while(j<s):
            print(end=" ")
            j=j+1
        s=s-1

        #no.of columns
        j=0
        while(j<i+1):
            print("* ",end="")
            j=j+1

        #end line
        print("\r")
        i=i+1

triangle(5)
