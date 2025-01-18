def powerof8(n):
    bitposition=0
    mask=1
    while (bitposition<=63):
        mask<<=bitposition
        if mask==n:
            return True
        bitposition+=3
        mask=1
    return False
n=int(input("Enter a number:"))
if powerof8(n):
    print("Yes the number is a power of 8")
else:
    print("The number is not a power of 8")
    