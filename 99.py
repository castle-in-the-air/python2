weight = int(input('weight:'))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight*0.45
    print(f" You are {converted } kilos.")
elif unit.upper() == "K":
    converted = weight//0.45
    print(f" You are {converted} pounds.")
else:
    print('Please enter L or K')
