print('Lambdas Exercise')
#1 print sum
sum1 = lambda a,b:a+b
print(sum1(4,3))
print('sum is : ',(lambda a,b,c:a+b+c)(1,2,3))
print((lambda *args:sum(args))(1,20,30,40,10))

#2
'''def fun1(name,arg2):
   return name.strip().title()+':'+arg2.strip().title()
print(fun1('mufEEdHa k P','dEMO'))'''
lambda1 = lambda name,arg2: name.strip().title()+':'+arg2.strip().title()
print(lambda1('mufEEdHa k P','dEMO'))

#3 Lambda: to join two lists without duplication
list_a = [1,2,3,4,5,9]
list_b = [3,4,5,6,7,8]
join_list_no_duplicates = lambda list1,list2 : list(set(list1+list2))
print(join_list_no_duplicates(list_a,list_b))

#4 sorting
names = ['mammu mamz','sufi zidh','fathi ufee','mufee khid']
print('Before sorting : ',names)
#[-1] for sorting last name
names.sort(key=lambda name:name.split(' ')[-1])
print('After sorting : ',names)
#5 put comma instead of space
new_l=lambda names:','.join(names.split(' '))
print(new_l(names[0]))

#6
def fun2(n):
   return lambda a:a*n
mymul = fun2(5)
print(mymul(4))

#7
signups = ['MPF1074', 'MPF20', 'MPF2', 'MPF17', 'MPF34', 'MPF45','MPF701']
print(signups) # Lexicographic sort
#write sorting by integer
print(sorted(signups,key=lambda x:int(x.strip('MPF'))))
#print(sorted(signups,key=lambda x:int(x[3:])))