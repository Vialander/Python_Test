#coding = utf-8

import time

print("开始")
for i in range(101):
    a = '*'*(i//10)
    b = '-'*(10-(i//10))
    c = str(i)
    print("[{}{}] {}% ".format(a,b,c))
    time.sleep(0.1)
print("结束")
    
        
