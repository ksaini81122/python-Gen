# lst = denoted by []
# list is ordered --- mutable
# allow duplicates values and hetrerogeneous
# lst is indexed --- can do slicing and indexing
# lst use in reallife --- songs playlist
list =[1,2,"hello",True,1.2]
print(list)
print(type(list))

lst = ['red','green','blue']
list[0]
print(lst)

lst[0] ='green'
print(lst)

lst[0:2] = [ 'black', 'brown']
print(lst)

lst[0:2] = ['black']
print(lst)

lst[0:2] = ['black','a']
print(lst)


# methods of list
lst = ['red','green','blue','red']
print(lst.count("red"))


print(lst.index("red")) # position of that element in list 

print(lst.clear()) # clear  is usded to delelet the complete list but lsit still present 

lst2 = lst.copy() # copy the previous list in new list 
print(lst2)

lst.append("green")# it is used to add a single item in the list but this item is add in thee end of the list 
print(lst)

lst.extend(["green","a","b"])# it is usedd to add multiple item in the list
print(lst)

lst.index(0,"greeen")# it is used to add item at perticular location
print(lst)

lst.pop()# agr es ko apn khaale chlta h tb ya last element ko remov kr dta ha list ma sa
print(lst)

lst.pop(1)# esma valu pass krrta h tb us perticular value pr jo element h usko remove kr dta h
print(lst)

lst.remove("red")# esma perticula item ko remove kr dta h 
lst.remove()# khale chltaa h to phla jo meel jyga usko remov kr dta h

lst.reverse() # reverce the list 
print(lst)

lst.sort()# khale ma accending order m print hoge values 
lst.sort(reversed=True)
print(lst)

print(lst[:-1])# reverce the list with the help of slicing

