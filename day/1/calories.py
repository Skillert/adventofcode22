import sys

def readInput(filename):
    # Set sum to 0
    sum = 0

    # Create an empty list
    calories = []

    # Top three calorie elfs
    top_elfs = 0

    # Open file
    data = open(filename,'r')

    # For each line in the input file sum the values together unless it's a newline, then we add the value to our list and go through next
    for line in data.readlines():
        if (line[0] != '\n'):
            sum+=int(line)
        else:
            calories.append(sum)
            sum = 0
            continue

    # Sort calories
    calories.sort()

    print(calories)
    print(f'King elf: {max(calories)}')

    # Add top 3 calorie elfs to our list
    for elf in range(3):
        top_elfs+=max(calories)
        calories.pop()

    print(f'The three kings: {top_elfs}')

    # Close file
    data.close()

if len(sys.argv) == 2:
    lines = readInput(sys.argv[1])
else:
    print("calories.py inputfile")
