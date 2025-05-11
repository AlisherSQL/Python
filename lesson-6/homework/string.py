1. list1=[1,1,2],list2=[2,3,4]
output = [1, 1, 3, 4]

Lista = [x for x in list1 if x < 2] 
Lists = [x for x in list2 if x > 2 ] 
print(Lista+Lists)

2. list1=[1,2,3] 
list2=[4,5,6]
output=[1, 2, 3, 4, 5, 6]

print(list1 + list2)

3. list1=[1,1,2,3,4,2] 
   list2=[1,3,4,5]

output=[2, 2, 5]

a=[x for x in list1 if x not in list2]
b=[x for x in list2 if x not in list1]
print(a+b)






