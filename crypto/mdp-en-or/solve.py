encrypted = "L4o2pgZ@yIg«"

l = [ord(c) for c in encrypted]

a = 0
b = 1

j = []

for i in range(len(l)):
    j.append(chr(l[i] - a))
    a,b = b, a+b

print("".join(j))
