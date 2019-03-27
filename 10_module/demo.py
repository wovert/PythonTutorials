__all__ = ['read','read2']
money = 100
def login():
    print('正在执行登录程序')
 
def read():
    print('in read1',money)
 
def read2():
    print('in read2')
 
if __name__ == '__main__':
    ret = login()
    print(ret)