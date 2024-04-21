#LIST 

names=["mammu","mufi","sufi"]
print(names)

#change first value
names[0]="Muhammed"
print("\nafter updation : "+str(names))

#last position
print(names[-1])

#last two values
print(names[-2:])

#add new value
names=names+["Suri"]
print(names)

names.append("Sid")
print(names)

names.insert(0,"Jamee")
print(names)


#read from user
names.append(input("Enter name: "))
print(names)

print("\nLength: "+ str(len(names))+"\n")
print("Type: "+ str(type(names)))


"""List allows dupliction
changeable 
ordered"""

