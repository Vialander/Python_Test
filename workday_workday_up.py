# coding = utf-8

def calculate(num):
    result = 1;
    for i in range(365):
        if(i%7 in [6,0]):
            result = result*(1 - 0.01)
        else:
            result = result*(1 + num)
    return result

num = 0.01
while calculate(num)<37.78:
    num +=0.001

print("应该有{:.5f}".format(num))
