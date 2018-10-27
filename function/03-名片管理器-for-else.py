card_infors = [{"name":"laowang","age":18},{"name":"laoli", "age":19},{"name":"laozhao","age":20}]

find_name = input("请输入要查询的名字：")

for temp in card_infors:
    if temp['name']==find_name:
        print("找到了．．．．．")
        break
else:
    #只要ｆｏｒ循环的过程中没有执行到break，那么就会执行else里面的代码
    print("没有找到....")
