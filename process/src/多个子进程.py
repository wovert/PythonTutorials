import time,os
from multiprocessing import Process

def func(i):
  time.sleep(1)
  print("%d: 子进程%d 干的事儿，父进程：%d" % (i, os.getpid(), os.getppid()))

if __name__ == '__main__':
  p_list = []
  for i in range(10):
    p = Process(target=func, args=(i,))
    p.start()
    p_list.append(p)
   
  for p in p_list:
    p.join()
  print('------------主进程----------')
