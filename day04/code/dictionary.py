# #字典基本操作
# stu_info = {
#     'stu_id' : '001',
#     'name' : '张三',
#     'age' : 18,
#     'tel' : 8327496274,
#     'email' : 'jett@qq.com',
#     'weight' : 65,
#     'height' : 175
# }
# print(stu_info)
#
# #列表和字典组成使用
# students_info = [
#     {'stu_id' : '001', 'name' : '张三', 'age' : 18},
#     {'stu_id' : '002', 'name' : '王五', 'age' : 19}
# ]
#
# #不同打印方式
# print(students_info)
#
# print(students_info[0])
#
# for stud_info in students_info:
#     print(stud_info)
#
#
# #直接打印和使用get()函数的区别
# print(stu_info['name'])
# print(stu_info.get('weight'))
#
# print(stu_info.get('like', '没有这个属性'))
# print(stu_info['like'])

#字典的合并
# dc1 = {'a' : 1, 'b' : 2}
# dc2 = {'c' : 3, 'd' : 4}
# #把二放在一里面
# dc1.update(dc2)
# print(dc1)

# #字典的删除
# dc1 = {'a' : 1, 'b' : 2}
# dc1.pop('a')
# print(dc1)

# #字典外部增加属性
# dc1 = {'a' : 1, 'b' : 2}
# dc1['c'] = 3
# print(dc1)





# #案例一：输入一段话，统计每个英文字母出现的次数
# """
# 测试用例：
# Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.
# """
# text = input('请输入要统计的文本：')
#
# counter = {}
#
# #遍历字符串
# for ch in text:
#     #ch表示的是输入的每一个字符
#     if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
#         counter[ch] = counter.get(ch, 0) + 1
#
# print(counter)






# #字典的遍历
# stu_info = {
#     'stu_id' : '001',
#     'name' : '张三',
#     'age' : 18,
#     'tel' : 8327496274,
#     'email' : 'jett@qq.com',
#     'weight' : 65,
#     'height' : 175
# }
# print(stu_info)
#
# #拿键
# for key in stu_info.keys():
#     print(key)
#
# #拿值
# for value in stu_info.values():
#     print(value)
#
# #拿键和值
# for key, value in stu_info.items():
#     print(key, value)







#案例二：算平均分，找最高分学生姓名
students = [
    {"name" : "张三" , "score" : 85},
    {"name" : "坤坤" , "score" : 90},
    {"name" : "王五" , "score" : 96}
]

total = 0

max_score = 0

top_student = ''

for item in students:
    total += item["score"]
    if item["score"] > max_score:
        max_score = item["score"]
        top_student = item["name"]

#计算平均分
avg = total / len(students)
print(avg)
print(top_student)