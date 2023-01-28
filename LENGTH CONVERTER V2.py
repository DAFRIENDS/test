print('''Last time in my Length converter V1, I converted km to miles and vice versa. 
This time I will be converting metres to yards and metres to feet. 
Thank you for viewing my project. ''')

metres = int(input("Type the length in metres:  "))
yard = metres * 1.0936133
print(f"{yard} yards.")

yards = int(input("Type the length in yards:  "))
metre = yards / 1.0936133
print(f"{metre} metres.")



metres_2 = int(input("Type the length in metres again:  "))
feet = metres_2 * 3.2808399
print(f"It is {feet} ft. ")

feet_2 = int(input("Now type the length in Feet:  "))
metres_3 = feet_2 / 3.2808399
print(f"It is {metres_3} metres. ")



print('''I will also be converting Centimetres to inches.
Thank You. ''')
cm = int(input("Type the Length in Centimetres:  "))
inch = cm / 2.54
print(f"It is {inch} inches. ")

inch_2 = int(input("Type the Length in Inches:  "))
cm_2 = inch_2 * 2.54
print(f"It is {cm_2} CM. ")

print('''THANK
            
              YOU
                    FOR
                          RUNNING
                                    THIS
                                           PROGRAM.........''')