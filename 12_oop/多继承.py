class Base(object):
    def test(self):
        print("----Base")
 
class A(Base):
    def test(self):
        print("-----A")
 
class B(Base):
    def test(self):
        print("-----B")
 
class C(A,B):
    pass
    #def test(self):
    #    print("-----C")
 
 
c = C()
c.test()
 
print(C.__mro__)