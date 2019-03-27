def login(func):
  def inner(arg):
    print('验证用户登录')
    func(arg)

  return inner


@login
def home(name):
  print("Welcome [%s] to home page" % name)

@login
def tv(name):
  print("Welcome [%s] to TV page" % name)

def movie(name):
  print("Welcome [%s] to movie page" % name)

tv('alex')