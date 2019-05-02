

x = int(input("Enter a Number"))

i=2
while i<x:
    y=x%i
    if y==0:
        print("It is not a Prime Number")
        break

    i=i+1
    print(i)
print("Bye")