#集合，里面元素不能重复
#会自动把重复元素给删除
s = {'a','b','c','d','a'},
print(s)

list1 = ['a', 'b', 'c', 'd', 'b', 'a']
s = set(list1)
list2 = list(s)
print(list2)

#元组，里面元素数据无法被修改
t1 = (10,20,30,40)
print(t1)
