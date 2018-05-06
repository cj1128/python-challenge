# 同样，没有任何头绪，总之肯定是图片操作了
# Google，原始标题`odd even`是提示按照奇偶来切割图片

from PIL import Image
image = Image.open("cave.jpg")
w, h = image.size

even = Image.new("RGB", (w // 2, h // 2))
odd = Image.new("RGB", (w // 2, h // 2))

for row in range(w):
  for col in range(h):
    pixel = image.getpixel((row, col))
    if (row + col) % 2 == 0:
      even.putpixel((row // 2, col // 2), pixel)
    else:
      odd.putpixel((row // 2, col // 2), pixel)

even.save("even.jpg")
odd.save("odd.jpg")

# 打开`even.jpg`，可以看到`evil`
