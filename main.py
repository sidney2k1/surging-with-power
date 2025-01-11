def power2(num):
    if num==0:
        return 0
    if ((num&(~(num-1)))==num):
        return 1
    return 0
num=int(input("eNTER A NUMBER:"))
if (power2(num)):
    print("It is a power of 2")
else:
    print("It is not a power of 2")