#Требуется вывести все целые степени двойки (т.е. числа
#вида 2k
#), не превосходящие числа N.
n = int(input("Enter number: "))
for i in range(1000):
    if(2**i>n):
        exit()
    print(2**i)
