#coding=utf-8
 
try:
    num = input("xxx:")
    int(num)
    #11/0
    #open("xxx.txt")
    #print(num)
    print("-----1----")
 
except (NameError,FileNotFoundError):
    print("如果捕获到异常后做的 处理....")
except Exception as ret:
    print("如果用了Exception,那么意味着只要上面的except没有捕获到异常,这个except一定会捕获到")
    print(ret)
else:
    print("没有异常才会执行的功能")
finally:
    print("------finally-----")
 
print("-----2----")