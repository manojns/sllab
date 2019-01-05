def reverse(string):
    string = "".join(reversed(string))
    return string
l=["No 1","I am 2", "not color blind 3","my world 4 ","is black and white 5","try to keep 6"]

print("Even Strings")
for i in range(len(l)):
	if i%2!=0:
		print(l[i])

print("\nUpper Case")
for i in range(len(l)):
	if (i+1)%3==0:
		print(l[i].upper())

print("\nReverse Strings")
l2=[reverse(i) for i in l]
print(l2)

print("\nDigits")
l3=[item for subitem in l for item in subitem.split() if item.isdigit()]
print(l3)
