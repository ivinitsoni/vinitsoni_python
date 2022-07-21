import udf

sname = input("Write the output file's name: ")
file = open(sname+('.txt'),'w')

while True:

    print("*"*50)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Pattern")
    print("7. Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice : "))
    print("*"*50)

    if choice==1:
        a=int(input("Enter Value : "))
        udf.OddEven(a)
        file = open(sname+('.txt'),'a')
        file.write("\nYou Opted OddEven Function\n")
        file.write(str(a))
        print("*"*50)

    elif choice==2:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        udf.MaxOfTwo(a,b)
        file.write("\nYou Opted MaxofTwo Function\n")
        file.write(str(a))
        file.write('\n')
        file.write(str(b))
        print("*"*50)

    elif choice==3:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        c=int(input("Enter Value : "))
        udf.MaxOfThree(a,b,c)
        file.write("\nYou Opted MaxOfThree Function\n")
        file.write(str(a))
        file.write('\n')
        file.write(str(b))
        file.write('\n')
        file.write(str(c))
        print("*"*50)

    elif choice==4:
        a=int(input("Enter Value : "))
        udf.Fibonacci(a)
        file.write("\nYou Opted Fibonacci Function\n")
        file.write(str(a))
        print("*"*50)

    elif choice==5:
        a=int(input("Enter Value : "))
        udf.Prime(a)
        file.write("\nYou Opted Prime Function\n")
        file.write(str(a))
        print("*"*50)

    elif choice==6:
        a=int(input("Enter Value : "))
        udf.Pattern(a)
        file.write("\nYou Opted Pattern Function\n")
        file.write(str(a))
        print("*"*50)

    else:
        file.write("\nYou Opted Exit")
        file.close()
        print("Thank You. Good Bye")
        break