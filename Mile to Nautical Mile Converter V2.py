print('''This Program Is like my other ones where I convert
different measurements. As you can tell by the title,
 it is what this program does. Just enter your measurement and the system of measurement you entered
 and you will get your answer in the other measurement system. ''')

length = int(input("LENGTH: "))
unit = input("(M)iles or (N)m : ")

if unit.upper == 'M':
    converted = length * 0.868976
    print(f"It is {converted} Nautical Miles.")
else:
    convert = length / 0.868976
    print(f"It is {convert}")