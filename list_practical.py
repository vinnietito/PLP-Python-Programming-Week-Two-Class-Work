list_a = [1, 2, 3, 4, 5]
print(list_a[4])
print(list_a)
list_a[0] = 10
print(list_a)

list_a.insert(len(list_a), 6)
list_a.append(7)
list_a.extend([8, 9])
list_a.pop(8)
del list_a[7]

print(list_a)

list_b = [1, "today", True, 3.0]

list_c = ["Skinny", "Ahmad", 'Mutemi']

list_d = [1, 2, 3, [4, 5], 6, 7]

list_e = []