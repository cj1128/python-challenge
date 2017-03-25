# -*- coding: utf-8 -*-
# @Author: CJ Ting
# @Date:   2017-03-25 18:12:53
# @Last Modified by:   CJ Ting
# @Last Modified time: 2017-03-25 19:00:04

# 这道题只给了一张图
# 查看源码，可以发现，图片是可以点击的，并且有一句注释，`Don't try all nothings`
# 点击图片，可以得到一个文本，文本里面给了一个`nothing`数
# 替换掉url中的`nothing=`查询字符串，可以得到一个新数
# 结合这一道题的名字，`linkedlist`，肯定是编程不停的获取`nothing`，直到循环

import requests
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?"
def run(start_nothing):
  nothing = start_nothing
  regexp = re.compile(r'\d+$')
  for _ in range(400):
    res = requests.get(url, {"nothing": nothing})
    res.raise_for_status()
    # 返回的数据长度不稳定
    # 可能是： `and the next nothing is 44827`
    # 也可能是：`Your hands are getting tired and the next nothing is 94485`
    # 所以不能依据位置来提取nothing
    text = res.text
    # this is for debug
    print("data fetched:", text)
    nothing = re.search(regexp, text).group(0)

# run("12345")

# 先用题目提供的初始值12345跑
# 到了`16044`以后无法解析了，根据文本，下一个nothing是`8022`，手动输入，接种跑
# run("8022")

# 到了`63579`有触发了解析失败，手动输入，再跑
# run("63579")
# 好了，到头了，文本提示，下一题是`peak.html`

# first run log:
# data fetched: and the next nothing is 44827
# data fetched: and the next nothing is 45439
# data fetched: <font color=red>Your hands are getting tired </font>and the next nothing is 94485
# data fetched: and the next nothing is 72198
# data fetched: and the next nothing is 80992
# data fetched: and the next nothing is 8880
# data fetched: and the next nothing is 40961
# data fetched: and the next nothing is 58765
# data fetched: and the next nothing is 46561
# data fetched: and the next nothing is 13418
# data fetched: and the next nothing is 41954
# data fetched: and the next nothing is 46782
# data fetched: and the next nothing is 92730
# data fetched: and the next nothing is 89229
# data fetched: and the next nothing is 25646
# data fetched: and the next nothing is 74288
# data fetched: and the next nothing is 25945
# data fetched: and the next nothing is 39876
# data fetched: and the next nothing is 8498
# data fetched: and the next nothing is 34684
# data fetched: and the next nothing is 62316
# data fetched: and the next nothing is 71331
# data fetched: and the next nothing is 59717
# data fetched: and the next nothing is 76893
# data fetched: and the next nothing is 44091
# data fetched: and the next nothing is 73241
# data fetched: and the next nothing is 19242
# data fetched: and the next nothing is 17476
# data fetched: and the next nothing is 39566
# data fetched: and the next nothing is 81293
# data fetched: and the next nothing is 25857
# data fetched: and the next nothing is 74343
# data fetched: and the next nothing is 39410
# data fetched: and the next nothing is 5505
# data fetched: and the next nothing is 27104
# data fetched: and the next nothing is 54003
# data fetched: and the next nothing is 23501
# data fetched: and the next nothing is 21110
# data fetched: and the next nothing is 88399
# data fetched: and the next nothing is 49740
# data fetched: and the next nothing is 31552
# data fetched: and the next nothing is 39998
# data fetched: and the next nothing is 19755
# data fetched: and the next nothing is 64624
# data fetched: and the next nothing is 37817
# data fetched: and the next nothing is 43427
# data fetched: and the next nothing is 15115
# data fetched: and the next nothing is 44327
# data fetched: and the next nothing is 7715
# data fetched: and the next nothing is 15248
# data fetched: and the next nothing is 61895
# data fetched: and the next nothing is 54759
# data fetched: and the next nothing is 54270
# data fetched: and the next nothing is 51332
# data fetched: and the next nothing is 63481
# data fetched: and the next nothing is 12362
# data fetched: and the next nothing is 94476
# data fetched: and the next nothing is 87810
# data fetched: and the next nothing is 6027
# data fetched: and the next nothing is 47551
# data fetched: and the next nothing is 79498
# data fetched: and the next nothing is 81226
# data fetched: and the next nothing is 4256
# data fetched: and the next nothing is 62734
# data fetched: and the next nothing is 25666
# data fetched: and the next nothing is 14781
# data fetched: and the next nothing is 21412
# data fetched: and the next nothing is 55205
# data fetched: and the next nothing is 65516
# data fetched: and the next nothing is 53535
# data fetched: and the next nothing is 4437
# data fetched: and the next nothing is 43442
# data fetched: and the next nothing is 91308
# data fetched: and the next nothing is 1312
# data fetched: and the next nothing is 36268
# data fetched: and the next nothing is 34289
# data fetched: and the next nothing is 46384
# data fetched: and the next nothing is 18097
# data fetched: and the next nothing is 9401
# data fetched: and the next nothing is 54249
# data fetched: and the next nothing is 29247
# data fetched: and the next nothing is 13115
# data fetched: and the next nothing is 23053
# data fetched: and the next nothing is 3875
# data fetched: and the next nothing is 16044
# data fetched: Yes. Divide by two and keep going.

# second run log:
# data fetched: and the next nothing is 25357
# data fetched: and the next nothing is 89879
# data fetched: and the next nothing is 80119
# data fetched: and the next nothing is 50290
# data fetched: and the next nothing is 9297
# data fetched: and the next nothing is 30571
# data fetched: and the next nothing is 7414
# data fetched: and the next nothing is 30978
# data fetched: and the next nothing is 16408
# data fetched: and the next nothing is 80109
# data fetched: and the next nothing is 55736
# data fetched: and the next nothing is 15357
# data fetched: and the next nothing is 80887
# data fetched: and the next nothing is 35014
# data fetched: and the next nothing is 16523
# data fetched: and the next nothing is 50286
# data fetched: and the next nothing is 34813
# data fetched: and the next nothing is 77562
# data fetched: and the next nothing is 54746
# data fetched: and the next nothing is 22680
# data fetched: and the next nothing is 19705
# data fetched: and the next nothing is 77000
# data fetched: and the next nothing is 27634
# data fetched: and the next nothing is 21008
# data fetched: and the next nothing is 64994
# data fetched: and the next nothing is 66109
# data fetched: and the next nothing is 37855
# data fetched: and the next nothing is 36383
# data fetched: and the next nothing is 68548
# data fetched: and the next nothing is 96070
# data fetched: and the next nothing is 83051
# data fetched: and the next nothing is 58026
# data fetched: and the next nothing is 44726
# data fetched: and the next nothing is 35748
# data fetched: and the next nothing is 61287
# data fetched: and the next nothing is 559
# data fetched: and the next nothing is 81318
# data fetched: and the next nothing is 50443
# data fetched: and the next nothing is 1570
# data fetched: and the next nothing is 75244
# data fetched: and the next nothing is 56265
# data fetched: and the next nothing is 17694
# data fetched: and the next nothing is 48033
# data fetched: and the next nothing is 56523
# data fetched: and the next nothing is 51253
# data fetched: and the next nothing is 85750
# data fetched: and the next nothing is 42760
# data fetched: and the next nothing is 11877
# data fetched: and the next nothing is 15962
# data fetched: and the next nothing is 75494
# data fetched: and the next nothing is 87283
# data fetched: and the next nothing is 40396
# data fetched: and the next nothing is 49574
# data fetched: and the next nothing is 82682
# data fetched: There maybe misleading numbers in the
# text. One example is 82683. Look only for the next nothing and the next nothing is 63579
# data fetched: You've been misleaded to here. Go to previous
# one and check.

# third run log:
# data fetched: and the next nothing is 37278
# data fetched: and the next nothing is 53548
# data fetched: and the next nothing is 66081
# data fetched: and the next nothing is 67753
# data fetched: and the next nothing is 56337
# data fetched: and the next nothing is 3356
# data fetched: and the next nothing is 94525
# data fetched: and the next nothing is 89574
# data fetched: and the next nothing is 4413
# data fetched: and the next nothing is 82294
# data fetched: and the next nothing is 56060
# data fetched: and the next nothing is 95493
# data fetched: and the next nothing is 80865
# data fetched: and the next nothing is 66242
# data fetched: and the next nothing is 16065
# data fetched: and the next nothing is 62145
# data fetched: and the next nothing is 23147
# data fetched: and the next nothing is 83763
# data fetched: and the next nothing is 62381
# data fetched: and the next nothing is 76841
# data fetched: and the next nothing is 91706
# data fetched: and the next nothing is 9268
# data fetched: and the next nothing is 64814
# data fetched: and the next nothing is 80809
# data fetched: and the next nothing is 14039
# data fetched: and the next nothing is 73355
# data fetched: and the next nothing is 81905
# data fetched: and the next nothing is 36402
# data fetched: and the next nothing is 27221
# data fetched: and the next nothing is 79607
# data fetched: and the next nothing is 91763
# data fetched: and the next nothing is 11631
# data fetched: and the next nothing is 76396
# data fetched: and the next nothing is 69905
# data fetched: and the next nothing is 11073
# data fetched: and the next nothing is 71281
# data fetched: and the next nothing is 54345
# data fetched: and the next nothing is 19047
# data fetched: and the next nothing is 34376
# data fetched: and the next nothing is 3193
# data fetched: and the next nothing is 74258
# data fetched: and the next nothing is 62712
# data fetched: and the next nothing is 1823
# data fetched: and the next nothing is 21232
# data fetched: and the next nothing is 87890
# data fetched: and the next nothing is 21545
# data fetched: and the next nothing is 37136
# data fetched: and the next nothing is 23060
# data fetched: and the next nothing is 5385
# data fetched: and the next nothing is 4620
# data fetched: and the next nothing is 39111
# data fetched: and the next nothing is 35914
# data fetched: and the next nothing is 60310
# data fetched: and the next nothing is 19178
# data fetched: and the next nothing is 44671
# data fetched: and the next nothing is 45736
# data fetched: and the next nothing is 9216
# data fetched: and the next nothing is 12585
# data fetched: and the next nothing is 11302
# data fetched: and the next nothing is 33096
# data fetched: and the next nothing is 13967
# data fetched: and the next nothing is 57004
# data fetched: and the next nothing is 64196
# data fetched: and the next nothing is 73929
# data fetched: and the next nothing is 24800
# data fetched: and the next nothing is 25081
# data fetched: and the next nothing is 90033
# data fetched: and the next nothing is 45919
# data fetched: and the next nothing is 54827
# data fetched: and the next nothing is 73950
# data fetched: and the next nothing is 56978
# data fetched: and the next nothing is 8133
# data fetched: and the next nothing is 61900
# data fetched: and the next nothing is 47769
# data fetched: and the next nothing is 631
# data fetched: and the next nothing is 2284
# data fetched: and the next nothing is 60074
# data fetched: and the next nothing is 35959
# data fetched: and the next nothing is 57158
# data fetched: and the next nothing is 90990
# data fetched: and the next nothing is 27935
# data fetched: and the next nothing is 99927
# data fetched: and the next nothing is 41785
# data fetched: and the next nothing is 32660
# data fetched: and the next nothing is 4328
# data fetched: and the next nothing is 42067
# data fetched: and the next nothing is 8743
# data fetched: and the next nothing is 38613
# data fetched: and the next nothing is 21100
# data fetched: and the next nothing is 77864
# data fetched: and the next nothing is 6523
# data fetched: and the next nothing is 6927
# data fetched: and the next nothing is 82930
# data fetched: and the next nothing is 35846
# data fetched: and the next nothing is 31785
# data fetched: and the next nothing is 41846
# data fetched: and the next nothing is 72387
# data fetched: and the next nothing is 59334
# data fetched: and the next nothing is 65520
# data fetched: and the next nothing is 93781
# data fetched: and the next nothing is 55840
# data fetched: and the next nothing is 80842
# data fetched: and the next nothing is 59022
# data fetched: and the next nothing is 23298
# data fetched: and the next nothing is 27709
# data fetched: and the next nothing is 96791
# data fetched: and the next nothing is 75635
# data fetched: and the next nothing is 52899
# data fetched: and the next nothing is 66831
# data fetched: peak.html
