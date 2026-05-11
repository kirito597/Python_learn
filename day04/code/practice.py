#检测密码强度
def check_password_strength(password):
    if len(password) < 8:
        return "密码强度不足：长度少于8位"

    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return "密码强度合格"
    else:
        missing = []
        if not has_upper:
            missing.append("大写字母")
        if not has_lower:
            missing.append("小写字母")
        if not has_digit:
            missing.append("数字")
        return f"密码强度不足：缺少{'、'.join(missing)}"


# 测试
password = input("请输入要检测的密码：")
result = check_password_strength(password)
print(result)


#统计元音字母数量
def count_vowels(text):
    """
    统计字符串中元音字母（a, e, i, o, u）的数量
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# 测试
text = input("请输入要统计的字符串：")
result = count_vowels(text)
print(f"元音字母数量：{result}")



#成绩分布统计
scores = [85, 92, 78, 96, 88, 73, 65, 90, 82, 79]
grades = {"优秀": 0, "良好": 0, "中等": 0, "及格": 0, "不及格": 0}

for score in scores:
    if 90 <= score <= 100:
        grades["优秀"] += 1
    elif 80 <= score <= 89:
        grades["良好"] += 1
    elif 70 <= score <= 79:
        grades["中等"] += 1
    elif 60 <= score <= 69:
        grades["及格"] += 1
    else:
        grades["不及格"] += 1

print("成绩统计结果：", grades)



# 学生信息管理
students = {
    "001": ["小明", 80, 85, 78],
    "002": ["小红", 90, 88, 92],
    "003": ["小刚", 75, 80, 82]
}

print("初始学生信息：", students)

# 1. 添加新学生（三科成绩一起输入）
print("\n添加新学生")
stu_id = input("请输入学号（例如：004）：")
name = input("请输入姓名：")
scores_input = input("请输入成绩（用空格分隔，例如：88 92 85）：")
scores = [int(x) for x in scores_input.split()]  # 一次性转换成三个成绩

students[stu_id] = [name] + scores
print(f"添加学生后：{students}")

# 2. 修改学号002学生的数学成绩为95
print("\n修改学生成绩")
if "002" in students:
    students["002"][2] = 95  # 索引2代表数学成绩
    print(f"修改数学成绩后：{students}")
else:
    print("学号002不存在")

# 3. 删除学号003的学生
print("\n删除学生")
if "003" in students:
    del students["003"]
    print(f"删除学生后：{students}")
else:
    print("学号003不存在")

# 4. 计算每个学生的平均分并打印
print("\n每个学生的平均分")
for student_id, info in students.items():
    name = info[0]
    scores = info[1:]  # 语文、数学、英语
    avg_score = sum(scores) / len(scores)
    print(f"学号：{student_id}，姓名：{name}，平均分：{avg_score:.2f}")

# 5. 找出平均分最高的学生姓名
print("\n平均分最高的学生")
max_avg = 0
best_student = ""
for student_id, info in students.items():
    name = info[0]
    scores = info[1:]
    avg_score = sum(scores) / len(scores)
    if avg_score > max_avg:
        max_avg = avg_score
        best_student = name

print(f"平均分最高的学生：{best_student}，平均分：{max_avg:.2f}")




#商品信息管理
# 商品列表，每个商品是一个字典
products = []

def add_product(name, price, stock):
    """新增商品"""
    product = {
        "名称": name,
        "价格": price,
        "库存": stock
    }
    products.append(product)
    print(f"商品 '{name}' 添加成功！")
    show_products()

def delete_product(name):
    """删除商品"""
    for product in products:
        if product["名称"] == name:
            products.remove(product)
            print(f"商品 '{name}' 删除成功！")
            show_products()
            return
    print(f"未找到商品 '{name}'")

def update_product(name, field, new_value):
    """修改商品信息
    field: 要修改的字段（"名称"、"价格"、"库存"）
    """
    for product in products:
        if product["名称"] == name:
            if field in product:
                product[field] = new_value
                print(f"商品 '{name}' 的 {field} 已修改为 {new_value}")
                show_products()
            else:
                print(f"字段 '{field}' 不存在")
            return
    print(f"未找到商品 '{name}'")

def show_products():
    """显示所有商品"""
    if not products:
        print("暂无商品")
        return
    print("\n当前商品列表：")
    for i, product in enumerate(products, 1):
        print(f"  {i}. 名称：{product['名称']}, 价格：{product['价格']}, 库存：{product['库存']}")
    print()


print("1. 新增商品")
add_product("手机", 2999, 50)
add_product("电脑", 5999, 30)
add_product("耳机", 199, 100)

print("\n2. 修改商品信息")
update_product("手机", "价格", 2799)
update_product("手机", "库存", 45)

print("\n3. 删除商品")
delete_product("耳机")

print("\n4. 尝试修改不存在的商品")
update_product("平板", "价格", 3000)

print("\n5. 尝试删除不存在的商品")
delete_product("平板")