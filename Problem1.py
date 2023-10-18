#Write a command to take above list as an input and find in the squares of a number and return a list

lst = [1,2,3,4,5,6,7,8,9]
lst2 = [x**2 for x in lst]
print(lst2)

#ye wala to easy tha...ek pehle v try kiye the 
#dictionary m merge in kr pa rhe h to google kiye to function mila ek 'zip' wo try kiye h

lst3 = dict(zip(lst,lst2))
print(lst3)
