def main():

    import math

    from datetime import datetime

    today = str(datetime.now())

    date_strip = today.strip()
    date = date_strip.split(" ")

    print(today)
    print(date[0])

    wMin = 180
    wMax = 400
    wvalid = False
    while not wvalid:
        width = input(f"Enter the width of the tire in mm (ex 205): ")

        if width.isdecimal():
    
            winteger = int(width)

            if winteger < wMin:
                print(f"{winteger} is too small. Please enter a positive integer between", wMin, "and", wMax,".")
            elif winteger > wMax:
                print(f"{winteger} is too large. Please enter a positive integer between", wMin, "and", wMax,".")
            else:
                wvalid = True
        else:
            print(f"'{width}' is not a positive integer." " Please enter a positive integer.")

    arMin = 45
    arMax = 70
    arvalid = False

    while not arvalid:
        ar = input(f"Enter the aspect ratio of the tire (ex 60): ")

        if ar.isdecimal():
            arinteger = int(ar)

            if arinteger < arMin:
                print(f"{arinteger} is too small. Please enter a positive integer between", arMin, "and",arMax,".")
            elif arinteger > arMax:
                print(f"{arinteger} is too large. Please enter a positive integer between", arMin, "and",arMax,".")
            else:
                arvalid = True
        else:
            print(f"'{ar}' is not a positive integer." " Please enter a positive integer.")

    diMin = 12
    diMax = 28
    divalid = False

    while not divalid:
        di = input(f"Enter the diameter of the tire in inches (ex 15): ")

        if di.isdecimal():
            diinteger = int(di)
            if diinteger < diMin:
                print(f"{diinteger} is too small. Please enter a positive integer between", diMin, "and",diMax,".")
            elif diinteger > diMax:
                print(f"{diinteger} is too large. Please enter a positive integer between", diMin, "and",diMax,".")
            else:
                divalid = True
        else:
            print(f"'{di}' is not a positive integer." " Please enter a positive integer.")

    widthf = float(width)
    arf = float(ar)
    dif = float(di)
    vone = widthf * arf + 2540 * dif
    vtwo = math.pi * (widthf ** 2) * arf
    v = round((vone * vtwo) / 10000000, 1)

    print("The approximate volume of space in your tire is ", v,", Thank you for using my Tire Program!") 

    print(f"The dementions of your tire are {width}/{ar}R{di}.")
    purchase = input("Would you like to buy these tires? ")
    if purchase == "yes":
        print("Here is the phone number to order your tires: (208)555-6255")
        print("Come back again! ")
    else:
        print("That is okay! Have a nice Day!")

    restart = input("Do you want to enter another tire size? ").lower()
    if restart == "yes":
        main()
    else:
        print("Thank you, please come again. Have a nice day!")
        exit() 

main()