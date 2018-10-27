# 1/0
# name
# 2+'3'
# [][3]
#{}['k']
# try:
#     print('1111')
#     # 1/0
#     print('2222')
#     # name
#     # 2+'3'
#     # [][3]
#     # {}['k']
#     ret = int(input('number >>>'))
#     print(ret*'*')
# except ValueError:
#     print('输入的数据类型有误')
# except Exception:
#     print('你错了，老铁')
# else:
#     print('没有异常的时候执行else中的代码')
# print('===========')
# def func():
#     try:
#         f = open('file','w')
#         ''''''
#         return True
#     except:
#         return False
#     finally:
#         print('执行finally了')
#         f.close()
#
# print(func())
 
 
 
 
 
# 程序一旦发生错误，就从错误的位置停下来了，不在继续执行后面的内容
# 使用try和except就能处理异常
    #try是我们需要处理的代码
    #except 后面跟一个错误类型 当代码发生错误且错误类型符合的时候 就会执行except中的代码
    #except支持多分支
    #有没有一个能处理所有错误的类型 : Exception
        # 有了万能的处理机制仍然需要把能预测到的问题单独处理
        # 单独处理的所有内容都应该写在万能异常之前
    # else : 没有异常的时候执行else中的代码
    # finally : 不管代码是否异常，都会执行
        # finally和return相遇的时候 依然会执行
        # 函数里做异常处理用,不管是否异常去做一些收尾工作
 
 
# try:
#     main()
# except Exception:
#     pass
 
try:
    print('1111')
    # 1/0
    print('2222')
    # name
    # 2+'3'
    # [][3]
    # {}['k']
    ret = int(input('number >>>'))
    print(ret*'*')
except Exception as error:
    print('你错了，老铁',error)