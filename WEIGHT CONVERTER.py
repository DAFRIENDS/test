print('''In this program,
 you will need to enter your weight
  in either Pounds or Kilograms. You will then choose which
  measurement you used(lbs or kg). The program will then tell you 
  how much you weigh in the other weight measurement. ''')

weight = int(input("WEIGHT: "))
unit = input("(L)bs or (K)g: ")

if unit.upper == 'L':
    converted = weight * 0.45
    print(f"You are {converted} Kilograms. ")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds. ")