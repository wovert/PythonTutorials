class Foo:
  def __repr__(self):
    return 'bbb'

f = Foo()
print(ascii(f)) # 自动运行 __repr__
