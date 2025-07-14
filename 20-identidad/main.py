a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b) # True
print(a == c) # False

print(a is b)
print(b is c)
print(c is a)

print(id(a))
print(id(b))
print(id(c))

n1 = 2
n2 = 2
print(id(n1))
print(id(n2))

print(n1 is n2)