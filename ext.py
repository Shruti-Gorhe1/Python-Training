#TUPLES
t = (10,20,30)
print(t)


#1. Ordered
#2.Immutable
#t1 = (1,2,3)
#t1[0] = 100

#3.Allow duplicates
t1 = (1,2,2,3,3)
print(t1)

#4.diff data types
t2 = (10,"Shruti" , True, 3,14)
print(t2)

t3 = 1,2,3
print(t3)

t4 = (10)
print(t4)

t =() #empty tuple

#TUPLE INDEXING
#Positive
t5 = (10,20,30,40)
print(t5[2])

#Negative
print(t5[-1])


# Tuple slicing
t6 = (10,20,30,40,50)
print(t6[1:4])

print(t6[:3])
print(t6[::2])


#TUPLE OPERATIONS
#1. Concatenation
t7 = (1,2)
t8 = (3,4)

print(t7+t8)

#2.Repition
print(t7*3)

#Built-in functions
#1 len()
print(len(t7))

#2 max() & min()
t9 = (10,5,20)
print(max(t9))
print(min(t9))

#sum()
print(sum(t9))

#methods
#1.count
t10 = (1,2,3,2)
print(t10.count(2))

#2.index
print(t10.index(3))

#Unpacking
a,b,c = (1,2,3)
print(a,b,c)

#tuple to list
t11 = (1,2,3)
l= list(t11)

#list to tuple
t12 = [4,5,6]
t = tuple(t12)
