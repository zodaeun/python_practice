x = 1
y = 0
z = 0


for i in range(1,10):
    for j in range(10):
        for k in range(10):
            x = i
            y = j
            z = k
            
            n1 = (100*x) + (10*y) + z
            n2 = x**3 + y**3 + z**3
            
            if n1 == n2:
                print(n1,end = " ")
