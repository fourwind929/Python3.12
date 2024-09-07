import re

# #findall()函数用于查找字符串中所有匹配正则表达式的子串，并返回一个列表。
# lst = re.findall(r"\d+", "123 abc 456 789 def") 
# print(lst)



# #finditer()函数用于查找字符串中所有匹配正则表达式的子串，并返回一个迭代器。
# it = re.finditer(r"\d+", "123 abc 456 789 def") 
# # print(it)
# for i in it:
#     print(i.group())



# #search()函数用于查找字符串中《第一个》匹配正则表达式的子串，并返回一个Match对象。
# #search 返回match对象，包含了匹配的字符串，以及匹配的位置等信息。拿数据需要用.group()方法。
# s = re.search(r"\d+", "123 abc 456 789 def")
# print(s.group())



# #.match是从头开始匹配，如果字符串开头不匹配，则返回None。
# s = re.match(r"\d+", "dcba 123 abc 456 789 def")
# print(s)



# #预加载正则表达式
# obj = re.compile(r"\d+")
# ret = obj.finditer("123 abc 456 789 def")
# for i in ret:
#     print(i.group())

# ret = obj.findall("123 abc 456 dfg 789 def 101112")
# print(ret)



# s = """
# <div class='jay'><span id='1'>郭麒麟</span></div>
# <div class='jj'><span id='2'>宋铁</span></div>
# <div class='jolin'><span id='3'>大聪明</span></div>
# <div class='sylar'><span id='4'>范思哲</span></div>
# <div class='tory'><span id='5'>胡说八道</span></div>
# """
# # 匹配所有包含class='.*?'><span id='.*?'>.*?</span></div>的字符串
# obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<starname>.*?)</span></div>", re.S) # re.S表示让“.”能匹配包括换行符在内的所有字符
# result = obj.finditer(s)
# for it in result:
#     print(it.group("id"))
#     print(it.group("starname"))