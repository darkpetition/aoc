# Python program to read a txt file and gather the sum of the three largest values with a delimiter of space newline

# Read a file line by line
fileToRead = open('d1input.txt', 'r')
Lines = fileToRead.readlines()

# Set variables for programmatic use
count = 0
current = 0
caloriesList = []

# Loop through the lines in the file
for line in Lines:
    # If a line is empty, calculate a new highest calorie sum
    if line == '\n':
        # Append calorie sum to caloriesList
        caloriesList.append(current)
        # Set current to 0 for next calorie sum
        current = 0
    # Continue to sum calorie amounts if line is not empty
    else:
        current += int(line)
    # Increment the counter of the loop
    count += 1

# Print the highest three calorie amounts summed
print("The three highest calorie amounts summed is: " + str(sum(sorted(caloriesList)[-3:])))

# Exit the program
exit
