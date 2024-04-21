'''TUPLE - immutable (can't change once defined a value)'''

tup1 = ("Fathi", "Mufee", "Aliya")
print("tuple1: ",tup1)
print("First value, tuple[0]: ",tup1[0])

tup2 : tuple[int | str, ...] = (1,72,34,"Fathima","Mufzz")
print("\nTuple of int or string: ",tup2)
print("Reverse: ",tup2[::-1])
print("Index 2:4 : ",tup2[2:4])
"""
this tuple consists of either int or st
‘…’  hold more than one int or str """

'''
tuple with a single element:
make sure to add a comma'''
mytuple = ("Mufeedha",) 
print("\nType of tuple: ",type(mytuple))

#concatenating 2 tuples 
tuple1 = (0, 1, 2, 3, 4)
tuple2 = ('python', 'java')
print("\nAfter concatenation: ",tuple1 + tuple2)

#Nested tuples
tuple3 = (tuple1, tuple2)
print("\nNested tuples: ",tuple3)
print("\nReverse: ",tuple3[::-1])

#tuple with repetition
tuple3 = ('python',)*3
print(tuple3)

#string to tuple
print(tuple('python'))


'''
cannot add items to a tuple once it is created. 
cannot be appended or extended.
cannot remove items from a tuple once it is created.
'''
