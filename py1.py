#coding=utf-8
import re         #正则表达式(regular expression)模块

#[a-zA-Z0-9]   匹配大小写字母与数字
#[a-zA-Z]      匹配大小写字母
#\@    a\@b     a@b   (字符转义)
#\.    a\.b     a.b   (字符转义)

def emails(e):
    if len(e)>= 5:
        if re.match("[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]",e) !=None:  #re.match(pattern, string) 尝试从字符串string的开始匹配一个模式。
            return '邮箱格式正确！'
    return '邮箱格式有误'


s1 = input("请输入email:")
print(s1)
a = emails(s1)
print(a)