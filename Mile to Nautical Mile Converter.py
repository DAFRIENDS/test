print('''This Program converts Miles To Nautical Miles and vice versa. 
Just input miles first and then nautical miles. ''')

nm = int(input("How many miles do you want to convert? : "))
m = nm / 0.868976
print(f"{m} Nautical Miles")

mile = int(input("How many Nautical Miles do you want to convert? : "))
nm_2 = mile * 0.868976
print(f"{nm_2} Miles")