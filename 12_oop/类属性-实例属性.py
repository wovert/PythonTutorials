class Tool(object):
 
    #类属性
    num = 0
 
    #方法
    def __init__(self, new_name):
        #实例属性
        self.name = new_name
        #对类属性+=1
        Tool.num += 1
 
 
tool1 = Tool("铁锹")
tool2 = Tool("工兵铲")
tool3 = Tool("水桶")
 
print(Tool.num)