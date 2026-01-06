# print("hello world")
# print("hello world")

# print("hello world")


# dir(__builtins__) // 查看所有的内置函数

# 幸运数 = 566
# print(幸运数) //变量是字母数字向下滑线或者中文



# xx=100
# print(xx)
# yy=200
# print(yy)
# xx, yy = yy, xx # 交换变量的值

# print(xx, yy)



# #都是对的，空格
# xx=11
# print(xx)
# yy=22
# print(yy)
# xx,yy = yy,xx # 交换变量的值

# print(xx,yy)

# print("x\'x,yy")
# print('2,ff')

print("""hello world""")
print("hello world")
#在Python中，字符串可以用单引号(')、双引号(")或三引号("""或''')来表示

print("hello \nworld") #换行
print("hello \tworld") #制表符
# 但是在前面加上r可以取消转义
print(r"hello \nworld") #取消转义
# 打印：hello 	world hello \nworld

str=""" ABC
1132 
345  56"""
print(str)
# 三引号可以表示多行字符串，不需要用\n来换行，自动添加换行符
# 打印：
#  ABC
# 1132 
# 345  56


#字符串的加法，就是拼接
str1="hello"
str2="world"
print(str1+str2)
# 打印：helloworld
#字符串的乘法，就是重复
print(str1*3)
# 打印：hellohellohello
#字符串的索引和切片
str3="abcdefghij"
print(str3[0]) #a
print(str3[1:5]) #bcde
print(str3[1:]) #bcdefghij
print(str3[:5]) #abcde

# #输入函数input
# name=input("请输入你的名字：")
# print("你好，"+name)

#运算符
# 加法
print(1+2) #3
# 减法
print(2-1) #1
# 乘法
print(2*3) #6
# 除法
print(4/2) #2.0
# 取余
print(5%2) #1
# 取整
print(5//2) #2
# 幂运算
print(2**3) #8
# 运算符优先级：幂运算 > 乘除取余 > 加减 > 取整
print(2+3*4) #14
# 比较运算符
print(1==2) #False
print(1!=2) #True
print(1<2) #True
print(1<=2) #True
print(1>2) #False
print(1>=2) #False


#random模块
import random #导入random模块
print(random.random()) #打印0.0到1.0之间的随机浮点数#
print(random.randint(1,10)) #打印1到10之间的随机整数
print(random.choice([1,2,3,4,5])) #打印1到5之间的随机整数
print(random.choice("hello")) #打印h,e,l,l,o中的随机字符
print(random.choice(["hello","world"])) #打印hello或world中的随机字符串
print(random.choice(["hello","world"])) #打印hello或world中的随机字符串
#为什么import random 要放在最前面？#因为random模块是Python内置的模块，所以不需要安装，直接导入即可
#.random()是什么？#生成0.0到1.0之间的随机浮点数
#.randint(1,10)是什么？#生成1到10之间的随机整数
#.choice([1,2,3,4,5])是什么？#生成1到5之间的随机整数
