import sys
import re

NetAddr=str(input())
print(re.match('https://www',NetAddr,re.I).span())


#re库函数用于字符匹配
# re.search()	在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
# re.match()	从一个字符串的开始位置起匹配正则表达式，返回match对象
# re.findall()	搜索字符串，以列表类型返回全部能匹配的子串
# re.split()	将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
# re.finditer()	搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
# re.sub()	在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串

#re.match(pattern,string,flags=0)
# pattern : 正则表达式的字符串或原生字符串表示
# string : 待匹配字符串
# flags : 正则表达式使用时的控制标记

#控制标记
# re.I	使匹配对大小写不敏感，忽略正则表达式的大小写，[A‐Z]能够匹配小写字符
# re.L	做本地化识别（locale-aware）匹配
# re.M	正则表达式中的^操作符能够将给定字符串的每行当作匹配开始
# re.S	正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。


# Match对象的方法
# .group(0)	获得匹配后的字符串
# .start()	匹配字符串在原始字符串的开始位置
# .end()	匹配字符串在原始字符串的结束位置
# .span()	返回(.start(), .end())
