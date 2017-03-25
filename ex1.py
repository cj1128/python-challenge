# -*- coding: utf-8 -*-
# @Author: cj
# @Date:   2017-03-25 17:19:56
# @Last Modified by:   CJ Ting
# @Last Modified time: 2017-03-25 17:33:11

# 根据提示，这是一个简单的字符位移加密，每个字母应该向后移动两位
def transform(s):
  new_str = ""

  for c in s:
    code = ord(c)
    if "a" <= c <= "z":
      code += 2
      if code >= ord("z"):
        code = code - ord("z") + ord("a") - 1
    new_str += chr(code)
  print(new_str)
