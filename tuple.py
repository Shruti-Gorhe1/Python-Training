
#print all the elements in tuple
t = (10, 20, 30, 40)

for i in t:
    print(i)

#Print tuple elements in same line
t = (10, 20, 30, 40)
for i in t:
    print(i, end=" ")

#Print elements with index
t = (10, 20, 30, 40)

for i in range(len(t)):
    print("Index:", i, "Value:", t[i])


#. Print elements in reverse order
t = (10, 20, 30, 40)

for i in range(len(t)-1, -1, -1):
    print(t[i], end=" ")

#Count even numbers in tuple
t = (1, 2, 3, 4, 5, 6)

count = 0
for i in t:
    if i % 2 == 0:
        count += 1

print("Even count:", count)


#Print only odd numbers
t = (1, 2, 3, 4, 5)

for i in t:
    if i % 2 != 0:
        print(i, end=" ")


#Create new tuple with squares
t = (1, 2, 3, 4)

result = ()

for i in t:
    result = result + (i*i,)

print(result)


#Print characters of tuple of strings
t = ("hi", "ok")

for word in t:
    for ch in word:
        print(ch, end=" ")

# Print only strings from mixed tuple
t = (10, "hi", 20, "python")

for i in t:
    if type(i) == str:
        print(i)

