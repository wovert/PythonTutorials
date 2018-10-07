class SweetPotato:
  """定义了一个地瓜类"""
  def __init__(self):
    self.cookedString = "生的"
    self.cookedLevel = 0
    self.condiments = []#为了能够存储多个数据,往往在开发中让一个属性是列表
 
  def __str__(self):
    return "地瓜 状态:%s(%d),添加的作料有:%s"%(self.cookedString, self.cookedLevel, str(self.condiments))
 
  def cook(self, cooked_time):

    #因为这个方法被调用了多次,为了能够在一次调用这个方法的时候 能够 获取到上一次调用这个方法时的cooked_time
    #所以 需要在此,把cooked_time保存到这个对象的属性中,因为属性不会随着方法的调用而结束(一个方法被调用的时候
    #是可以用局部变量来保存数据的,但是当这个方法定义结束之后这个方法中的所有数据就没有了)
    self.cookedLevel += cooked_time

    if self.cookedLevel >=0 and self.cookedLevel<3:
      self.cookedString = "生的"
    elif self.cookedLevel >=3 and self.cookedLevel<5:
      self.cookedString = "半生不熟"
    elif self.cookedLevel >=5 and self.cookedLevel<8:
      self.cookedString = "熟了"
    elif self.cookedLevel>8:
      self.cookedString = "烤糊了"

  def addCondiments(self, item):
    #因为item这个变量指向了一个 作料,所以 接下来需要将item放到append里面
    self.condiments.append(item)
 
 
#创建了一个地瓜对象
di_gua = SweetPotato()
print(di_gua)
 
#开始烤地瓜
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("大蒜")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("番茄酱")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("孜然")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("芥末")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)