r1 = 0
r2 = 0

for i in range(1, 101):
    if i % 2 == 1:
        r1 = r1 + i
  
print("1부터 100까지의 합은",r1)


j = 1
while j <= 100:
    if j % 2 == 1:
        r2 =  r2 + j
    j = j + 1
    
print("1부터 100까지의 합은", r2)



