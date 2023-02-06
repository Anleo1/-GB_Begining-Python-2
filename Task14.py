n = int(input("Enter number: "))
for i in range(1000):
    if(2**i>n):
        exit()
    print(2**i)
