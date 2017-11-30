<<<<<<< HEAD
import re 
=======
#coding=utf-8
import re         #正则表达式(regular expression)模块

#[a-zA-Z0-9]   匹配大小写字母与数字
#[a-zA-Z]      匹配大小写字母
#\@    a\@b     a@b   (字符转义)
#\.    a\.b     a.b   (字符转义)
#这是个测试文件
>>>>>>> c2efc9a4b96a3486cfaaa18638fbebb5469b50bc

def emails(e):
    if len(e)>= 5:
        if re.match("[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]",e) !=None:
            return '邮箱格式正确！'
    return '邮箱格式有误'

<<<<<<< HEAD
mail = input("请输入email: ")
print(mail)
a = emails(mail)
=======
ss = "zhengshuo"

s1 = input("请输入email: ")
print(s1)
print(s1)
a = emails(s1)

print(a)
>>>>>>> c2efc9a4b96a3486cfaaa18638fbebb5469b50bc
print(a)