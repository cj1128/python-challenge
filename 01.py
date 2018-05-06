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

  return new_str

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(transform(input))
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

print(transform("map"))
# ocr
