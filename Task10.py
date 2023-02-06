num = int(input("Enter number: "))
c = 0
for i in range(1, num+1):
    b = int(input())
    i+=1
    if b==0:
        c+=1
if c<= (num/2):
    print("Answer: ",c)
else:
    print("Answer: ", num-c)