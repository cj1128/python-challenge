# -*- coding: utf-8 -*-
# @Author: CJ Ting
# @Date:   2017-03-25 19:14:07
# @Last Modified by:   CJ Ting
# @Last Modified time: 2017-04-30 00:12:18

# 这题实在是一头雾水，作者只给了一句提示
# `peak hell sounds familiar ?`
# 作为中国人，我实在是不知道再暗示啥
# 网页里藏了一个数据，`banner.p`，里面是一段杂乱的编码
# 看着像二进制数据的某种编码
# 到此我卡住了，只能求助Google了
# 原来是提示用`pickle`来解析`banner.p`

import pickle

banner = pickle.load(open("banner.p", "rb"))

for i in banner:
  line = ""
  for j in i:
    line += j[0]*j[1]
  print(line)

# 打印出一副字符画，是一个单词： channel
