# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))
# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
print(len(subjects))

#prints the list
for subject in subjects:
    print(subject)

#prints all but stops history
for subject in subjects:
    if subjects[2]:
        break
print(subject)

#prints all but skips science
for subject in subjects:
    if subjects[1]:
        continue
print(subject)

for index in range(len(subjects)):
    print("Subject " + str(index) + ": " + subjects[index])

# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"


# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.


total_sum = 0 # store the number in a variable (baseline)


for num in numbers: #loop to iterate through every index in the list
    total_sum += num #For the variable we created, adds up the numbers from each index and saves it to the total_sum

print("total: ", total_sum)

#challenge
#sum all the numbers up and print the total
new_numbers = list(range(1,600001))

num1 = 0

for num in new_numbers:
    num1 += num
print("total ", num1)

#challenge3

list = list(range(5,26))

base_line = 0

for num in list:
    base_line += num

print("total ", base_line)