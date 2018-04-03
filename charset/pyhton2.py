# -*- coding: utf-8 -*-
s = "严"

# Python2 默认是 ASCII 码，所有utf-8代码解码位Unicode码，Unicode 码与 ASCII 兼容
# utf-8 => ASCII 
# utf-8 解码之后就是 Unicode 编码
unicode_s = s.decode('utf-8')
gbk_s = unicode_s.encode('GBK')

print("Unicode:%s"%unicode_s)
print("GBK:%s"%gbk_s)
print("Unicode:",unicode_s)
print("GBK:", gbk_s)