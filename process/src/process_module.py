from multiprocessing import Process
import os,time

def func(money):
  print('子进程：', os.getpid()) # 子进程
  print("父进程：", os.getppid())
  print("取钱:%d" %money)

if __name__ == '__main__':
  p = Process(target=func, args=(1,)) # 创建进程对象

  print('主进程：', os.getpid()) # 主进程
  
  p.start() # 启动进程，运行func函数。告诉OS启动新的进程，OS响应该进程我无法控制
  print("去取钱")

  # time.sleep(10) # 异步阻塞, 同步阻塞？
  
  # 等待子进程结束
  p.join() # 主进程阻塞，等待子进程p结束
  print("取完钱了")

  print('主进程：', os.getpid()) # 主进程

'''
同一个程序中从上到下执行
'''