#for loop

cinema=["Joker.mp4","Payya.mp4","Three.mp4","Sulaikha manzil.mp4"]
for x in cinema:
    print(x)

print("\nRemoves last 4 char")
for x in cinema:
    print(x[0:-4])

print("\nNumbers from 0 to 10")
for x in range(11): 
    print(x) 

print("\nNumbers from 5 to 10")
for x in range(5,11):
    print(x)

print("\nNumbers from 5 to 10 with 2 difference")
#multiplication purpose
for x in range(5,11,2):
    print(x)
