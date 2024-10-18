while True:
    print()
    try:
        age = int(input("Age: "))
        income = 20000
        risk = income / age
        print(f'Risk: {risk}')

    except ZeroDivisionError:
        print("Age cannot be 0.")
    except ValueError:
        print("Please enter an Integer.")
