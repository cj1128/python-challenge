# -*- coding: utf-8 -*-
# @Author: CJ Ting
# @Date:   2017-05-12 14:20:12
# @Last Modified by:   CJ Ting
# @Last Modified time: 2017-05-12 15:14:31

# 这一题也是完全没有头绪
# 上一题是对图片进行操作，我在想，难不成这一题也是操作图片？
# 可是怎么操作呢？总不能再是奇偶分割了。
# 没办法了，Google
# 事实证明，这是一道非常复杂的题目

# 首先，网页中的链接是`evil1.jpg`，说明还有`evil2`
# 打开`evil2.jpg`，提示更改后缀为`gfx`
# 下载得到`evil2.gfx`

# 接着，继续尝试`evil3.jpg`，提示`no more evils`
# 继续尝试`evil4.jpg`，使用`curl`可以发现，
# 返回了一句话：`Bert is evil! go back!`
# 很有可能是下一关的提示

# 看来数据就藏在`evil2.gfx`中

data = open("evil2.gfx", "rb").read()
print(len(data))

# 发现有67575个字节
# 根据标题的提示`dealing evils`，应该是要分割
# 题目的图片中，牌被分为了5堆，所以我们尝试将数据分成五份

for i in range(5):
  open("%d.jpg" % i, "wb").write(data[i::5])

# 还有一个小插曲
# 在Mac上如果直接试图打开`3.jpg`，会提示图片错误，打开以后一片漆黑
# 我想了很久是不是程序哪里出了问题
# 哪里来说，如果程序出了问题，那么应该所有的图片都打不开才对
# 不会只有一张打不开
# 后来在网上和别人生成的对比以后才发现，一模一样
# 只是图片似乎有点残缺，所以Mac的Preview程序打开不了
# 拖动到Chrome中就可以看到内容了

# 最后，五张图片组在一起，拼成了一个单词
# disproportional
