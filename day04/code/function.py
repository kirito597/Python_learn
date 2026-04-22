# def fu():
#     print("函数")
#
# fu()

# #a和b是形参
# def fn(a, b):
#     print(a, b)
# #1和2是实参
# fn(1, 2)

# #函数参数默认值
# def fn(name, age = 18):
#     print(name, age)
#
# fn('张三')

# #函数的关键字参数
# def get_sum(num1, num2):
#     print(num1 + num2)
#
# get_sum(1, 2)

# #获取信息
# def get_info(name, age, like):
#     info = {
#         "name" : name,
#         "age" : age,
#         "like" : like
#     }
#     print(info)
#
# # get_info('张三', 18, ['篮球'])
# #使用关键字参数
# get_info(
#     age = 18,
#     name='张三',
#     like=['鸡鸡']
# )

#函数的返回值
#全局变量
name1 = '王五'
def fn():
    #局部变量
    name2 = '张三'
    print(name2)
    return name2

fn()
print(name1)
print(fn())

