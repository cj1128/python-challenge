# 这题同样是完全没有头绪，主要是这个数组实在看不懂
# Google，原来这个数组叫做`look-and-say sequence`
# 也就是，后面的数字用来描述前面的数字
# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211
# 知道数字的规律以后，写程序生成就不难了

def make_look_and_say_seq():
  value = 1
  def process(v):
    digits = str(v)
    last_digit = digits[0]
    count = 1
    result_str = ""
    for digit in digits[1:]:
      if digit == last_digit:
        count += 1
      else:
        result_str += f"{count}{last_digit}"
        last_digit = digit
        count = 1
    result_str += f"{count}{last_digit}"
    return int(result_str)
  while True:
    yield value
    value = process(value)


seq = make_look_and_say_seq()

for _ in range(30):
  next(seq)

print(len(str(next(seq))))
