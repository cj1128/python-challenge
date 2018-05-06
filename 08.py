# 这一题实在是没有任何头绪
# 最终无奈Google，网页说页面提示了`inflate`，我硬是没找到
# 如果找到了这个词，继续能联想到关于压缩的话，这题就很简单了
# 数据只要用bzip2解压缩就行了

import bz2

username = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
password = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

print(bz2.decompress(username))
print(bz2.decompress(password))

