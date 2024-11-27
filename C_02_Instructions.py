# functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
- Instruction 1
- Instruction 2
- etcetera
    ''')


# Main routine goes here

# Response-based Instruction Displayer
want_instructions = input("Please press the enter key for instructions "
                          "or any other key to continue: ")

if want_instructions == "":
    instructions()

print("The program continues...")
