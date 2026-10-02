# =========================================================
# Chapter: Basic Python Operations & Control Flow
# =========================================================

# Exercise 4.3a: Student Grade Evaluation
x = float(input('Student grade: '))
if x >= 5:
    print('The student passed the course.')
else:
    print('The student failed the course.')

# Exercise 4.3b: BMI Calculation and Warning
name = input('Name: ')
weight = float(input('Weight (kg): '))
height = float(input('Height (m): '))
bmi = weight / (height**2)

# Normal weight: 18.5 <= bmi < 25
if bmi < 18.5 or bmi >= 25:
    print('The Body Mass Index of patient %s is not normal.' % name)

# Exercise 4.3c: Degree Classification
name = input('Graduate name: ')
grade = float(input('Degree grade: '))

print('Name: %s\nGrade: %.2f (' % (name, grade), end="")
if 5 <= grade <= 6.49:
    print('Good', end="")
elif 6.5 <= grade <= 8.49:
    print('Very Good', end="")
else:
    print('Excellent', end="")
print(')\n')

# Exercise 6.3a: Celsius to Fahrenheit Table
print('C\tF\n------\n')
for c in range(0, 101, 5):
    f = c * (9/5) + 32
    print('%d\t%d' % (c, f))

# Exercise 6.3b: Factorial Calculation
N = int(input('Enter N for factorial: '))
s = 1
for i in range(1, N + 1):
    s = s * i
print('%d! = %d' % (N, s))

# Exercise 6.3c: Normal Temperature Counter
normal_count = 0
temp_sum = 0
for i in range(1, 6):
    temp = float(input(f'Patient {i} temperature: '))
    if 35.5 <= temp <= 37:
        normal_count += 1
        temp_sum += temp

if normal_count > 0:
    mean_temp = temp_sum / normal_count
    print('Number of patients with normal temperature: %d' % normal_count)
    print('Mean normal temperature: %.2f' % mean_temp)
else:
    print('No patients with normal temperature.')

# Exercise 6.3d: Max/Min BMI Tracking
max_bmi = 0; min_bmi = float('inf')
namemax = ""; namemin = ""

for i in range(1, 6):
    print(f'--- Patient {i} ---')
    name = input('Name: ')
    weight = float(input('Weight (kg): '))
    height = float(input('Height (m): '))
    bmi = weight / (height**2)
    
    if bmi > max_bmi:
        max_bmi = bmi
        namemax = name
    if bmi < min_bmi:
        min_bmi = bmi
        namemin = name

print('Maximum BMI: %.1f (Patient: %s)' % (max_bmi, namemax))
print('Minimum BMI: %.1f (Patient: %s)' % (min_bmi, namemin))

# Exercise 7.3a: Weight Input Loop until -1
weight = float(input('Enter weight (-1 to exit): '))
max_w = weight
min_w = weight
total_w = 0
count = 0

while weight != -1:
    total_w += weight
    count += 1
    if weight > max_w: max_w = weight
    if weight < min_w: min_w = weight
    weight = float(input('Enter weight (-1 to exit): '))

if count > 0:
    mean_w = total_w / count
    print('Max weight: %d\nMin weight: %d\nMean Value: %.2f' % (max_w, min_w, mean_w))

# Exercise 7.3b: Infinite Menu
selection = 'A'
while selection != 'E':
    print('\n*** MENU ***')
    print('1. Add a new patient')
    print('2. Remove a patient')
    print('3. List all patients')
    print('E. Exit')
    selection = input('Selection: ').upper()
print('Exiting...')

# Exercise 9.3a: String Space Removal
s = input('Enter a string: ')
space_count = 0
clean_string = ''
for char in s:
    if char == ' ':
        space_count += 1
    else:
        clean_string += char

print('The string has %d spaces.' % space_count)
print('String without spaces: %s' % clean_string)

# Exercise 9.3c: Binary to Decimal Conversion (Robust)
valid = False
while not valid:
    number = input('Input binary number: ')
    valid = all(char in '01' for char in number)
    if not valid:
        print("Invalid input. Please enter only 0s and 1s.")

decimal_value = 0
for i in range(len(number)):
    bit = int(number[i])
    decimal_value += bit * (2 ** (len(number) - i - 1))
print('%s (binary) = %d (decimal)' % (number, decimal_value))

# Exercise 9.3d: Palindrome Checker (Alphanumeric only)
s = input('Enter a word/phrase to check for palindrome: ')
s = s.lower() 
clean_s = ''
for char in s:
    if char.isalnum():
        clean_s += char

reversed_s = clean_s[::-1]  # Pythonic way to reverse a string

if clean_s == reversed_s:
    print('The phrase is a palindrome.')
else:
    print('The phrase is not a palindrome.')
