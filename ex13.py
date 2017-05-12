# -*- coding: utf-8 -*-
# @Author: CJ Ting
# @Date:   2017-05-12 16:19:58
# @Last Modified by:   CJ Ting
# @Last Modified time: 2017-05-12 17:25:08

# 首先，点击`5`号按键来到`phonebook.php`页面
# 但是返回的是一段奇怪的XML文档
# 文档看起来像是某种协议的返回结果
#
# Google一下这个XML文档的关键字，发现是XMLRPC协议
#
# 查阅一下XMLRPC，是使用XML文档编码请求方法和请求参数
#
# 所以，首先，我们获取系统支持的所有方法

import requests

def call(payload):
  res = requests.post("http://www.pythonchallenge.com/pc/phonebook.php", data=payload)
  res.raise_for_status()
  print(res.text)

payload = """<?xml version="1.0"?>
<methodCall>
  <methodName>system.listMethods</methodName>
</methodCall>"""
# call(payload)


# 系统返回结果如下
# <?xml version="1.0"?>
# <methodResponse>
# <params>
# <param>
# <value><array>
# <data>
# <value><string>phone</string></value>
# <value><string>system.listMethods</string></value>
# <value><string>system.methodHelp</string></value>
# <value><string>system.methodSignature</string></value>
# <value><string>system.multicall</string></value>
# <value><string>system.getCapabilities</string></value>
# </data>
# </array></value>
# </param>
# </params>
# </methodResponse>

# 很明显，`phone`这个方法是我们要的，先来看看这个方法的帮助

payload = """<?xml version="1.0"?>
<methodCall>
  <methodName>system.methodHelp</methodName>
  <params>
    <param><value>
      <string>phone</string>
    </value></param>
  </params>
</methodCall>"""
# call(payload)

# <?xml version="1.0"?>
# <methodResponse>
# <params>
# <param>
# <value><string>Returns the phone of a person</string></value>
# </param>
# </params>
# </methodResponse>

# phone方法是返回一个人的电话用的，说了跟没说一下，
# 我们接着使用`methodSignature`来确定一下phone这个方法怎么调用

payload = """<?xml version="1.0"?>
<methodCall>
  <methodName>system.methodSignature</methodName>
  <params>
    <param><value>
      <string>phone</string>
    </value></param>
  </params>
</methodCall>"""
# call(payload)

# <?xml version="1.0"?>
# <methodResponse>
# <params>
# <param>
# <value><array>
# <data>
# <value><array>
# <data>
# <value><string>string</string></value>
# <value><string>string</string></value>
# </data>
# </array></value>
# </data>
# </array></value>
# </param>
# </params>
# </methodResponse>

# 查阅XMLRPC文档可以知道，这段返回表示`phone`方法接收一个string参数，
# 返回一个string的值

# 我们来试着使用上一关得到的`Bert is evil`提示来调用`phone`方法

payload = """<?xml version="1.0"?>
<methodCall>
  <methodName>phone</methodName>
  <params>
    <param><value>
      <string>Bert</string>
    </value></param>
  </params>
</methodCall>"""
# call(payload)

# <?xml version="1.0"?>
# <methodResponse>
# <params>
# <param>
# <value><string>555-ITALY</string></value>
# </param>
# </params>
# </methodResponse>

# 555-ITALY, 555-48259
# 终于拿到电话号码了，接下来就是尝试
# 我试了`555-ITALY`,`555-48259`,`48259`
# 终于试到`ITALY`的时候成功了！多么感动！
