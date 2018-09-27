def print_info(*args, **kwargs):
  print(args)
  print(kwargs)

print_info('aaaa','abc', 'efg', a=12, b='b', c='c')