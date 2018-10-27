class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
 
    def test1(self):
        print("-----test1----")
 
    def __test2(self):
        print("-----test2----")
 
    def test3(self):
        self.__test2()
        print(self.__num2)
 
class B(A):
    def test4(self):
        pass
        # self.__test2() # 不被继承
        # print(self.__num2) # 不被继承
 
 
b_obj = B()
#b.test1()
#b.__test2() #私有方法并不会被继承
#print(b.num1)
#print(b.__num2)
b_obj.test3()
b_obj.test4()