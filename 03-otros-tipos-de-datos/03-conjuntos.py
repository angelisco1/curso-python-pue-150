un_conjunto = set([1, 2, 3, 4, 4, 4, 4, 4, 5])
print(un_conjunto)
print(len(un_conjunto))

otro_conjunto = {4, 5, 6, 7, 8}

print(type(otro_conjunto))

item = otro_conjunto.pop()
print(item)
print(otro_conjunto)

otro_conjunto.add(item)
otro_conjunto.add(9)
print(otro_conjunto)

un_conjunto.update(otro_conjunto)
print(un_conjunto)

# un_conjunto.remove(10)
un_conjunto.discard(10)

print(un_conjunto.union(otro_conjunto))
print(un_conjunto)

otro_conjunto = {4, 5, 6, 7, 8, 9}
un_conjunto = {1, 2, 3, 4, 5}
print(f"| -> {un_conjunto | otro_conjunto}")


un_conjunto = {1, 2, 3, 4, 5}
otro_conjunto = {4, 5, 6, 7, 8, 9}
print(un_conjunto.intersection(otro_conjunto))

otro_conjunto = {4, 5, 6, 7, 8, 9}
un_conjunto = {1, 2, 3, 4, 5}
print(f"& -> {un_conjunto & otro_conjunto}")

un_conjunto = {1, 2, 3, 4, 5}
otro_conjunto = {4, 5, 6, 7, 8, 9}
print(un_conjunto.difference(otro_conjunto))
print(un_conjunto - otro_conjunto)

un_conjunto = {1, 2, 3, 4, 5}
otro_conjunto = {4, 5, 6, 7, 8, 9}
print(un_conjunto.symmetric_difference(otro_conjunto))
print(un_conjunto ^ otro_conjunto)

