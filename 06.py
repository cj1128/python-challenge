# 不得不说这个题目太烧脑了
# 这一题没有任何提示，只有一句注释`zip`
# 我首先想，难道是用要压缩或者解压缩什么东西吗？但是没有找到相应的数据呀
# 想了一会，不如直接用`zip`替换URL试试，系统提示了一句
# `yes, find the zip`
# 看来，我们要找到zip文档
# 回到之前的url，改变后缀为`channel.zip`，果然，数据有了！

# 将zip文件解压以后，和之前网络请求是一样的套路，不停的寻找下一个nothing就行了

import os
import re

regexp = re.compile(r'\d+$')

nothings = ["90052"]

def run(start_nothing):
  nothing = start_nothing
  while True:
    f = open(os.path.join("channel", "{}.txt".format(nothing)))
    content = f.read()
    match = re.search(regexp, content)
    if match:
      nothing = re.search(regexp, content).group(0)
      nothings.append(nothing)
      print("Next nothing is", nothing)
    else:
      print(content)
      break

# 根据readme的提示，我们从90052开始跑
run("90052")
# 一直跑到`46145.txt`，提示是`collect the comments`
# 看来是要提取zip文件的comment

from zipfile import ZipFile
with ZipFile("channel.zip") as zip:
  for nothing in nothings:
    info = zip.getinfo("{}.txt".format(nothing))
    c = info.comment.decode("utf-8")
    print(c, end="")

# 答案出来了: HOCKEY
# 输入hockey，提示字符在`air`中，所以答案应该是`oxygen`
