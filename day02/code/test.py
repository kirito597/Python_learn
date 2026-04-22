#1. 判断两个数是否能除尽
print("1. 判断两个数是否能除尽")
num1, num2 = 10, 3
if num1 % num2 == 0:
    print(f"{num1} 能被 {num2} 除尽")
else:
    print(f"{num1} 不能被 {num2} 除尽")

num1, num2 = 10, 5
if num1 % num2 == 0:
    print(f"{num1} 能被 {num2} 除尽")
else:
    print(f"{num1} 不能被 {num2} 除尽")
print()

#2. 判断年龄是否符合当兵要求
print("2. 判断年龄是否符合当兵要求")
age = int(input("请输入年龄: "))
if 18 <= age <= 25:
    print("符合当兵要求")
else:
    print("不符合当兵要求")
print()

#3. 判断输入的年份是否为闰年
print("3. 判断闰年")
year = int(input("请输入年份: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} 年是闰年")
else:
    print(f"{year} 年不是闰年")
print()

#4. 用户登录模拟
print("4. 用户登录模拟")
PRESET_USERNAME = ("hc")
PRESET_PASSWORD = "123456"

username = input("请输入用户名: ")
password = input("请输入密码: ")

if username == PRESET_USERNAME:
    if password == PRESET_PASSWORD:
        print("登录成功！")
    else:
        print("密码错误！")
else:
    print("用户不存在！")
print()

#5. 判断是否可以参加比赛
print("5. 判断是否可以参加比赛")
age = int(input("请输入年龄: "))
height = int(input("请输入身高(cm): "))

if 16 <= age <= 30 and height >= 170:
    print("可以参加比赛")
else:
    print("不可以参加比赛")