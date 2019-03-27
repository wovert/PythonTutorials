from functools import wraps

def wahaha():
  print('哇哈哈')


'''
f：被装饰的函数
'''
def wrapper(f): # 装饰器函数
  @wraps(f)
  def inner(*args,**kwargs): # 接受元租
    '''
    被装饰函数之前的执行的代码
    '''
    start = time.time()

    f(*args,**kwargs) # 被装饰的函数
    
    '''
    被装饰函数之后的执行的代码
    '''
    end = time.time()
    print(end - start)
  return inner

@wrapper # 语法糖，@装饰器函数名
def holiday(day):
  ''' 这是一个放假通知 '''
  print('全体放假%s天'%day)
  return '好开心'

print(wahaha.__name__) # 查看字符串格式的函数名 wahaha
print(holiday.__name__) # inner



print(holiday.__doc__) # 这是一个放假通知