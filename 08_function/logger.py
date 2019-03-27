import time

def logger(n):
  time_format = '%Y-%m-%d %X'
  time_current = time.strftime(time_format)

  with open('日志记录','a') as f:
    f.write('%s end action%s\n'%(time_current, n));