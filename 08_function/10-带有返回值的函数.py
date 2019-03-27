def get_wendu(a):
    wendu = 22
    print("当前的室温是:%d"%wendu)
    return wendu

def get_wendu_huashi(wendu):
    print("------4------")
    wendu = wendu + 3
    print("------5------")
    print("当前的温度(华氏)是:%d"%wendu)
    print("------6------")

print("------1------")
result = get_wendu(1000000)
print("------2------")
get_wendu_huashi(result)
print("------3------")
