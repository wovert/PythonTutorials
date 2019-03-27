def cash_out(amount): # 函数是生成器
  while amount > 0:
    amount -= 100
    yield 100
    print("擦，又来取钱了...败家子")

ATM = cash_out(500) # ATM 是迭代器
print(type(ATM)) # <class 'generator'>
print("取到钱 %s 万" %ATM.__next__()) # 100万
print("取到钱 %s 万" %ATM.__next__()) # 100万
print("取到钱 %s 万" %ATM.__next__()) # 100万
print("取到钱 %s 万" %ATM.__next__()) # 100万
print("取到钱 %s 万" %ATM.__next__()) # 100万