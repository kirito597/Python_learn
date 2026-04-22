# 1. 列表求和
numbers = [10, 2, 6, 20, 6]
total = 0
for num in numbers:
    total += num
print(f"列表内容和为: {total}")

# 2. 找出最大值
numbers = [3, 5, -2, 7, 4]
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print(f"列表中的最大值为: {max_value}")

# 3. 找出偶数并求和
numbers = [10, 19, 1, 2, 8, 2, 12]
even_sum = 0
print("列表中偶数有:", end=" ")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
        even_sum += num
print(f"列表中偶数的和为: {even_sum}")

# 4. 计算下标为奇数的平均数
numbers = [10, 19, 1, 2, 8, 2, 12]
odd_index_sum = 0
odd_index_count = 0
for i in range(len(numbers)):
    if i % 2 != 0:
        odd_index_sum += numbers[i]
        odd_index_count += 1
if odd_index_count > 0:
    average = odd_index_sum / odd_index_count
    print(f"列表中下标为奇数的平均数: {average:.2f}")

# 5. 学生成绩统计
scores = [85, 92, 78, 90, 88, 92]
max_score = scores[0]
min_score = scores[0]
for score in scores:
    if score > max_score:
        max_score = score
    if score < min_score:
        min_score = score

total_score = 0
for score in scores:
    total_score += score
average_score = total_score / len(scores)

above_average = []
for score in scores:
    if score > average_score:
        above_average.append(score)

print(f"最高分: {max_score}")
print(f"最低分: {min_score}")
print(f"平均分: {average_score:.2f}")
print(f"高于平均分的分数: {above_average}")

# 6. Craps赌博游戏
import random


def roll_dice():
    """摇骰子，返回两颗骰子的点数之和"""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

print("6. Craps赌博游戏")
print("=" * 30)

first_roll = roll_dice()
print(f"第一次摇出了: {first_roll}点")

# 判断第一次的结果
if first_roll == 7 or first_roll == 11:
    print("玩家胜！")
elif first_roll == 2 or first_roll == 3 or first_roll == 12:
    print("庄家胜！")
else:
    print(f"游戏继续，目标点数为: {first_roll}")
    point = first_roll

    while True:
        input("按回车键继续摇骰子...")
        current_roll = roll_dice()
        print(f"摇出了: {current_roll}点")

        if current_roll == 7:
            print("庄家胜！")
            break
        elif current_roll == point:
            print("玩家胜！")
            break
        else:
            print(f"没有分出胜负，继续游戏，目标点数是: {point}")
