sum = int(input("Enter x+y : "))
prod = int(input("Enter x*y: "))
for x in range(1,1001):
    for y in range (1,1001):
        if(x+y==sum and x*y==prod):
            print("X = ", x,"Y = ", y)

