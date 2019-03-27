# 1. 什么事固定长度的 bytes
# 2. 为什么要转成固定长度的 bytes

import struct

# 把一个数字转换成固定长度的 bytes 类型
res = struct.pack('i', 4096)
print(res) # 4个字节
