from functools import reduce

l1=[2,4,5,6,8,10]
l2=[x*3 for x in l1]
print("original list :",l1)
print("new list :",l2)
sum = reduce(lambda a,b : a+b,l1)
print ("The sum of the original list elements is :",sum)
sum = reduce(lambda a,b : a+b,l2)
print ("The sum of the new list elements is :",sum)
