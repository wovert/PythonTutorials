i = 1
while i<=5:

    j = 1
    while j<=i:
        print("*",end="")
        j+=1
        break#对里面的这个while起作用
        #continue

    print("")#换行

    i+=1
    break#最外边的while起作用
