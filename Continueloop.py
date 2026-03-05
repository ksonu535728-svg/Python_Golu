print(" Weclcome to Continuse Loops")
num = int(input("Enter Number:"))
i=0
while i<=num:
    if(i==5):
        i+=1
    elif(i==10):
        i+=1

        continue
    print(i)
    i+=1