import time

def timer(f): # 装饰器函数
  def inner():    
    start = time.time()
    f() # 被装饰的函数
    end = time.time()
    print(end - start)
  return inner

@timer # 语法糖，@装饰器函数名
def func(): # 被装饰的函数
  time.sleep(0.01)
  print('Hi boss~~')

# func = timer(func) 等于  @timer
# func() = inner()
#func = timer(func)
func()

