# a = 0
# for i in range(101):
#     if i % 2 == 0:
#         print(i)
#         a += i
#     else:
#         if i <= 10:
#             print(i)
# print(a)

a = [1,1,1,1,3,4,5,6,7]
print(a[0:6])
print(a[:6])
print(a[6:])
print(a[0:9:3])
print(a[-3])
print(a[-1:-8:-2])
print(a[::])
print(a[::-1])

a.append(0)
print(a)
a.insert(0, 98)
print(a)
a.remove(98)
print(a)
print(len(a))
print(sum(a))
print(max(a))
print(min(a))
