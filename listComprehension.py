my_list = [1,2,3,4,5,6,7,8,9]
new_list = []

# without comprehension
'''for num in my_list:
    new_list.append(num*num)
'''

'''using comprehension'''
#1 square
new_list = [num*num for num in my_list]
print('new list : ' , new_list)

#2 even numbers
even_list = [num for num in my_list if num%2==0]
print('even list : ',even_list)
'''or we can use filter'''
even_list2 = filter(lambda num: num % 2 ==0,my_list)
print('even list2 : ',list(even_list2)) #convert filtered object to list




# I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
new_list2 = []
for letter in 'spam':
   for num in range(4):
       new_list2.append((letter,num))
print(new_list2)

new_list2 = [(letter,num) for letter in 'spam' for num in range(4)]














