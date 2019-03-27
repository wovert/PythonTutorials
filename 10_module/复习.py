# 序列化模块
    # 数据类型转化成字符串的过程就是序列化
    # 为了方便存储和网络传输
    # json
        # dumps
        # loads
        # dump  和文件有关
        # load  load不能load多次
 
# import json
# data = {'username':['李华','二愣子'],'sex':'male','age':16}
# json_dic2 = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=False)
# print(json_dic2)
 
    # pickle
        #方法和json一样
        #dump和load的时候 文件是rb或者wb打开的
        #支持python所有的数据类型
        #序列化和反序列化需要相同的环境
    # shelve
        # open方法
        # open方法获取了一个文件句柄
        # 操作和字典类似
 
# 模块的导入
# import
# from import
# as重命名
# 都支持多名字导入
# sys.moudles记录了所有被导入的模块
# sys.path 记录了导入模块的时候寻找的所有路径