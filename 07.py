# 这里只给了一张图片，所以我们第一想法就是解析这张图片
# 图片中间位置有一系列纯色块的像素，我们将颜色取出来看看

from PIL import Image

img = Image.open("oxygen.png")

width, height = img.size

y = height // 2

# for x in range(width):
#   r, g, b, a = img.getpixel((x, y))
#   if r == g == b:
#     print(r)

# 取出颜色发现，颜色值似乎是ASCII码
# 去重，转换成ASCII打印看看

s = ""

for x in range(width):
  r, g, b, a = img.getpixel((x, y))
  if r == g == b:
    c = chr(r)
    if len(s) != 0 and s[-1] == c:
      continue
    s += c

print(s)

# 字符串内容为：
# smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]

# 这个看着像ASCII code，但是其中的16以及10都不是可打印的ASCII
# 想了一会，突然想到，我们上面的算法对于连续两个色块在一起这种情况无法处理
# 比如，作者想编码连续的两个`a`字符，那么我们解析出来肯定只有一个a
# 同样的道理，这里面，`10`,`16`,`14`,`16`完全可能是`110`,`116`,``114`,``116`

code = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in code:
  print(chr(i), end="")

# 打印结果：integrity
