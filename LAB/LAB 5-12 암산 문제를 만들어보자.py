import random

while True:
    e = random.randint(0,1)        
    x = random.randint(1,100)
    y = random.randint(1,100)

    if e == 0:
        print(x,"+",y,"= ")
        r = int(input(" "))
        if r == x+y:
            print("잘했어요!!")
        else:
            print("정답은",x+y,"입니다. 다음번에는 잘 할 수 있죠?")
    else:
        print(x,"-",y,"= ")
        r = int(input(" "))
        if r == x-y:
            print("잘했어요!!")
        else:
            print("정답은",x+y,"입니다. 다음번에는 잘 할 수 있죠?")
        
        
