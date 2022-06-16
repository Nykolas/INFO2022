'''
Cargue dos listas, y actualice la primer lista con los elementos 
que están en la segunda y no en la primera.
'''

import random

l1 = []
l2 = []

for i in range(100):
	l1.append(random.randint(1,100))
	l2.append(random.randint(1,100))

print(l1)
print(l2)

for elto in l2:
	if elto not in l1:
		print(f"se agrego el elemtno-->{elto}")
		l1.append(elto)

print(l1)
