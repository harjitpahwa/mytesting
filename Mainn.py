import mm
print(mm.PI)
print(mm.GRAVITY)

'''PI = 3.14
GRAVITY = 9.8'''

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))



a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

s="hello harjit"
print(s[0:4])

d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1]);
