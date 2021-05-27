"""
regex.py re模塊 功能函數
"""

import re

# 目標字符串
s="Alex:1994,Sunny:1996"
pattern=r"\w+:\d+"#正則表達示

# re模塊調用findall 返回值是列表
l=re.findall(pattern,s)
print(l)

# compile對象調用findall
regex=re.compile(pattern)
l=regex.findall(s,0,12)
print(l)

# 按照正則表達示匹配內容切割字符串
l=re.split(r'[:,]',s)#用上面的字符集的：和,切割
print(l)

# 替換目標字符串 把：用-替換掉 後面如果傳個1 表示最多替換一處
s=re.subn(r':','-',s,1)
print(s)
