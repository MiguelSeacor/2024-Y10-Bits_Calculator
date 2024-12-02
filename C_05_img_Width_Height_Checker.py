def int_check(question, low):
    error = f"Please enter an integer that is above or equal to {low}\n"
    error2 = "Please enter an integer (does not have a decimal part)\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check if the number is more than aero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error2)

# Main Routine goes here
for item in range(0, 2):
    width = int_check("Width: ", 1)
    print(width)
    print()

for item in range(0, 2):
    height = int_check("Height: ", 1)
    print(height)
    print()