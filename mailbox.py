#coding=utf-8
import re         #正则表达式(regular expression)模块

#[a-zA-Z0-9]   匹配大小写字母与数字
#[a-zA-Z]      匹配大小写字母
#\@    a\@b     a@b   (字符转义)
#\.    a\.b     a.b   (字符转义)
#这是个测试文件

def emails(e):
    if len(e)>= 5:
        if re.match("[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]",e) !=None:
            return '邮箱格式正确！'
    return '邮箱格式有误'

mail = input("请输入email: ")
print(mail)
a = emails(mail)
print(a)