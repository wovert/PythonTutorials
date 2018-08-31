import time

'''
f：被装饰的函数
'''
def wrapper(f): # 装饰器函数
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
def func(a): # 被装饰的函数
  time.sleep(0.01)
  print('Hi boss~~', a)

# func = timer(func) 等于  @timer
# func() = inner()
#func = timer(func)
func(10)
func(1)

@wrapper # 语法糖，@装饰器函数名
def func2(a,b): # 被装饰的函数
  time.sleep(0.01)
  print('hello father~~', a, b)

# func = timer(func) 等于  @timer
# func() = inner()
#func = timer(func)
func2(10,20)

func2(3,b='bb')

