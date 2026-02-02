a = int(input())
for i in range(1,a+1):
    for j in range(1,a+i):
        if(j <= a-i or j >= a+i ):
            print(" ",end="")
        else:
            print("*",end="")
    print()
#TQC+ 程式語言Python 410 繪製等腰三角形