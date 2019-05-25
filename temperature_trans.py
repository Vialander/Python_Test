#coding = utf-8
def trans_temperature():
    TempStr = input("请输入温度值")
    if TempStr[-1] in ['F','f']:
        Num = (eval(TempStr[0:-1])-32)/1.8
        print("结果是{:.2f}C".format(Num))
    elif TempStr[-1] in ['C','c']:
        Num = eval(TempStr[0:-1])*1.8+32
        print("结果是{:.2f}F".format(Num))
    else:
        print("格式错误")

counter = 10
for counter in range(20):
    print(counter)
