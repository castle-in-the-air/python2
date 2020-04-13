try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid value. Please enter the number of your age")
except ZeroDivisionError:
    print("Sorry, the age cannot be 0.")
