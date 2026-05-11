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

# #函数的返回值
# #全局变量
# name1 = '王五'
# def fn():
#     #局部变量
#     name2 = '张三'
#     print(name2)
#     #可以通过函数的返回值把内部数据返回给外部
#     return name2
#
# #函数名加括号就可以拿到返回值
# result = fn()
# print(name1)
# print(result)

# #求和
# def get_sum(num1, num2):
#     return num1 + num2
#
# result = get_sum(1, 2)
# print(result)

# def fn():
#     print("start")
#     #终止函数执行
#     return
#     print("end")
#
# fn()

#案例一
def shopping_fn():
    sp_id = input('请输入商品id:')
    if sp_id != '001':
        print('进行商品搜索')
        return
    print('后续操作逻辑')

shopping_fn()