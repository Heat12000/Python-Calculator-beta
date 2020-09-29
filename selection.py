def run():
    x=1
    while x==1:
        selection = input("Would you like to perform simple or advanced math: ")
        if selection == "simple":
            import simplemath
            x=x-1
            simplemath.start()
