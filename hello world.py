import random
secret = random.randint(1,10)
temp = input("1-10,输入数字：")
guess = int(temp)
while guess != secret:
    if guess < secret:
        print("小了")
    else:
        print("大了")
    temp = input("1-10,输入数字：")
    guess = int(temp)
guess = secret
print("你好腻害哦")
print("游戏结束")




teacher = "罗"
print(teacher)
first = 3
second = 8
third = first + second
print(third)

mytheacher = "xiaojiayu"
yourtheacher = "heiy\'e"
ourtheacher = mytheacher + yourtheacher
print(ourtheacher)

www = r"c:\now"
print(str)
stw = "c:\now"
print(stw)
stqsra = """我i哇大大你，
大赛的纳斯的撒旦你看三,
大卡萨丁大撒大撒"""
print(stqsra)
sada = "的撒大江南萨迪克·，\n大青蛙达瓦地区·"
print(sada)
a = 0.00000000000000000000000025
print(a)
print(True+True)
print(True+False)
a = 5.99
c = int(a)
print(c)
b = float(c)
print(b)
d = str(b)
print(d)
print(type(c))
print(isinstance(c,int))
w = 8/3
print(w)
w = 8//3
print(w)
w = 11 % 2
print(w)
w = 3 ** 5
print(w)
print(not False)


scorce = int(input("请输入一个分数:"))
while scorce > 100 or scorce < 0:
    print("输入错误，请重新输入")
    scorce = int(input("请输入一个分数:"))
if 100 >= scorce >= 90:
    print("优秀")
elif 90 > scorce >= 70:
    print("良好")
elif 70 > scorce >= 60:
    print("合格")
else:
    print("不合格")


favourite = "fishC"
for i in favourite:
    print(i, end="")

member = ["都比，弟弟，儿子啊"]
for each in member:
    print(each, len(member))


range(5)
list(range(5))
for i in  range(5):
    print(i)
for i in range(2, 9):
    print(i)
for i in range(1, 10, 2):
    print(i)


bigo = "丢你螺母"
anwser = input("你猴犀利啊：")
while True:
    if anwser == bigo:
        break
    anwser = input("请输入 丢你螺母")
print("叻仔")


for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 2
    print(i)


member=["啥子", "都比", "逗逗"]
number = [1, 2, 3, 4, 5]
mix = [1, "傻逼逼", 3, 5, [1, 2, 3, ]]
empty = []
number.append("你加我干嘛")
print(member, number, mix, empty)
print(len(number))
number.extend(mix)
print(len(number))
number.insert(1, "裤裆")
number.insert(0, "我才是第一")
print(number)
print(number[5])
number[0] = number[4]


print(number)
del number[2]
print(number)
number.pop()
print(number)
name = number.pop()
print(name)
number.pop(5)
print(number)
print(number[1:3])
print(number[:3])
print(number[:])

list1 = [123]
list2 = [234]
print(list1 > list2)
list3 = list1+list2
print(list3)
print(list3*3)

print(123 in list3)
print(444 not in list3)

list5 = [123,[2222.3333]]
print(2222 in list5[1])
dir(list)
print(list5.count(123))
print(list5.index(123))

list5.reverse()
print(list5)
list7 = [1231, 656, 1514, 45]
list7.sort()
print(list7)
list7.sort(reverse=True)
print(list7)
list6 = list7[:]

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple1)
print(tuple1[1])

temp = (1,)
type(temp)
print(8*(8,))
temp = ("小弟弟,", "都比")
temp = temp[:2] + ("意境",) + temp[2:]
print(temp)

str1 = "i love you"
print(str[:6])
str1[:6] + "插入" + str1[6:]
print(str1)

str2 = "xiaoxie"
print(str2.capitalize())
str2 = "XUAIXU"
print(str2.casefold())
print(str1.center(50))
print(str2.count("xi"))
str3 = "i\tsda\tdastt\.com"
print(str3.expandtabs(10))

print(str3.isalnum())
print(str3.islower())

str4 = "fish"
str4.istitle()
str4.ljust(50)
str4.rstrip()
str4.partition("ish")
str4.replace("ish", "love")

str6 ="i love you"
str6.split("i")
str7 = "    aaaa     "
str7.strip("a")
str7.title()
print(str1, str2, str3, str4, str6, str7)

print("{0} love {1}. {2}".format("i", "fish", "ccc"))
print("{a} love {b}. {c}".format(a="i", b="fish", c="ccc"))
print("\ta")
print("{0:.1f}{1}").format(27.658, "GB")

print("%c" % 97)
print("%c", "%c", "%c" % (97, 98, 99))
print("%s" % "i love u")
print("%5.1f" % 25.556)


































