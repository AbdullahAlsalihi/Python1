

#Input
age_input = input("Enter your age: ")

#processing
if age_input.isdigit():
    age = int(age_input)

    if age > 0:
        if age < 18:
            print("Minor")
        elif 18 <= age <= 65:
            print("Adult")
        else:
            print("senior citizen")
    else:
        print("Error: Age must be a postive number")

else:
    print("Error: Invalid input. Please enter a postive number")


