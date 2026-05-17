# name = "张三"
# age = 123
# height = 175.5
# is_hero = True
# print("名字:%s,年龄:%d,身高:%.1f" % (name,age,height))

# password = input("请输入银行卡密码：")
# print("你输入的密码为: %s" % password)

# score = int(input("请输入分数："))
# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("良好")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")

# pwd = input("请输入密码：")
# if pwd == "123456":
#     print("密码正确！")
# else:
#     print("密码错误！")
# try:
# a = float(input("请输入a边："))
# b = float(input("请输入b边："))
# c = float(input("请输入c边："))
#
# if a <= 0 or b <= 0 or c <=0:
#     print("❌️错误：边长必须为正数！")
# elif a + b <= c or a + c <= b or b + c <= a:
#     print("❌️错误：任意两边之和必须大于第三遍，不能构成三角形！")
# elif a == b == c:
#     print("✅️等边三角形")
# elif a == b or b == c or a == c:
#     print("✅️等腰三角形")
# else:
#     print("✅️一般三角形")
#
# except ValueError:
#     print("❌️输入无效！请输入数字")


# for i in range(1,101):
#     print(i)

# for n in range(1,101):
#     if n % 2 == 0:
#         print(f"{n}是偶数")
#     else:
#         print(f"{n} 是奇数")

# total = sum(range(1,101))
# odd_sum = sum(range(1,101,2))
# even_sum = sum(range(0,101,2))
#
# print("综合：",total)
# print("奇数和:",odd_sum)
# print("偶数和:",even_sum)



# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(f"{j}*{i}={i*j:2}",end=" ")
#     print()



# arr = [20,50,65,12,55,58,100]
#
# n=len(arr)
# for i in range(n-1):
#     for j in range(n-1):
#         for j in range(n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
# print("排序后：",arr)
#


# user={"账号":"123456","密码":"123456"}
# for key,value in user.items():
#     print(key,":",value)


# def multiply(a,b,c):
#     return  a*b*c
# print(multiply(2,3,4))

# def greet(name="游客"):
#     print(f"欢迎你,{name}!")
#
# greet("小明")
# greet()


# class Calculator:
#     def divide(self,a,b):
#         if b==0:
#             return "除数不能为0"
#         return a/b
# calc = Calculator()
# print(calc.divide(100,0))



# s=input("请输入一个字符串：")
# if s==s[::-1]:
#     print("是回文！")
# else:
#     print("不是回文。")


# sentence="hello world python"
# reversed_world=' '.join(sentence.split()[::-1])
# print(reversed_world)



# import random
# num = random.randint(1,100)
# print("随机数：",num)



import random
import string
charset=string.ascii_letters+string.digits

length=8

random_str=''.join(random.choices(charset,k=length))

print("随机字符串：",random_str)