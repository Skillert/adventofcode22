import sys

def max_calories(filename):
    # Create an empty list
    calories = []

    # Open file
    with open(filename, 'r') as data:
        # Set sum to 0
        calories_sum = 0

        # For each line in the input file sum the values together unless it's a newline, then we add the value to our list and go through next
        for line in data:
            if line[0] != '\n':
                calories_sum += int(line)
            else:
                calories.append(calories_sum)
                calories_sum = 0

    return calories

def find_top_elfs(calories):
    # Sort calories in descending order
    calories.sort(reverse=True)

    # Top three calorie elfs
    top_elfs = 0

    # Add top 3 calorie elfs to our list
    for elf in range(3):
        top_elfs += calories[elf]

    return top_elfs

if len(sys.argv) == 2:
    # Read input
    calories = max_calories(sys.argv[1])

    # Find top 3 calorie elfs
    top_elfs = find_top_elfs(calories)

    print(f'King elf: {max(calories)}')
    print(f'The three kings: {top_elfs}')
else:
    print("calories.py inputfile")
