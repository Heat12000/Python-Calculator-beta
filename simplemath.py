def start():
    def run():
        def add():
            my_list =[]
            my_list1 =[]
            c=int(input("how many number would you like to add: "))
            if c==c:
                x=0
                y=0
                t=0
                for i in range(0,c):
                    t=t + 1
                    my_list1.append(t)
                    a=int(input("Enter number "+str(my_list1[t-1])+": " ))
                    my_list.append(a)
                    x=x+(my_list[y])
                    y=y + 1
                print ("Your answer is " +str(x) )
        def subtract():
                my_list =[]
                my_list1 =[]
                c=int(input("how many number would you like to subtract: "))
                if c==c:
                    t=0
                    x=0
                    y=0
                    z=0
                    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
                    print("Make sure number 1 is the number you are subtracting from")
                    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
                    for i in range(0,c):
                        t=t + 1
                        my_list1.append(t)
                        a=int(input("Enter number "+str(my_list1[t-1])+": " ))
                        my_list.append(a)
                        z=(my_list[0])
                        x=x-(my_list[y])
                        y=y + 1
                    x=x+z*2
                    print ("Your answer is: " +str(x) )
        def multiply():
                my_list =[]
                my_list1 =[]
                c=int(input("how many number would you like to multiply: "))
                if c==c:
                    x=1
                    y=0
                    t=0
                    for i in range(0,c):
                        t=t + 1
                        my_list1.append(t)
                        a=int(input("Enter number "+str(my_list1[t-1])+": " ))
                        my_list.append(a)
                        x=x*(my_list[y])
                        y=y + 1
                print ("Your answer is " +str(x) )
        def divide():
                my_list =[]
                my_list1 =[]
                c=int(input("how many number would you like to multiply: "))
                if c==c:
                    y=0
                    t=1
                    x=float(input("Enter number 1: "))
                    for i in range(1,c):
                        t=t+1
                        my_list1.append(t)
                        a=int(input("Enter number "+str(my_list1[t-2])+": " ))
                        my_list.append(a)
                        x=x/(my_list[y])
                        y=y + 1
                print ("Your answer is " +str(x) )
        if selection == "add":
                add()
        if selection == "subtract":
                subtract()
        if selection == "multiply":
                multiply()
        if selection == "divide":
                divide()
    selection= input("would you like to add, subtract, multiply, or divide: ")
    run()
        
