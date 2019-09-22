import functions

print("Welcome to the first ever Python Excel Database")
print("Type 'HELP' for help")
print("Type 'EXIT' to leave")

while True:
    # Input of the command
    BaseCommand = input("> ")
    BaseCommand = BaseCommand.split(' ')

    functions.BasicAllocation(BaseCommand)
