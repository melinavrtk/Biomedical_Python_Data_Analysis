# =========================================================
# Chapter: Object-Oriented Programming (Classes)
# =========================================================
import numpy as np

# Exercise 11.3a: Patient Cholesterol Class
class Patient:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.value = [0, 0]

def print_max_cholesterol(values):
    if values[0] > values[1]:
        print('Higher cholesterol before diet: ', values[0])
    elif values[0] < values[1]:
        print('Higher cholesterol after diet: ', values[1])
    else:
        print('Cholesterol level is the same: ', values[0])

# Example Usage:
# p = Patient()
# p.name = input('Name: ')
# p.age = float(input('Age: '))
# p.value[0] = float(input('Cholesterol Value 1: '))
# p.value[1] = float(input('Cholesterol Value 2: '))
# print_max_cholesterol(p.value)


# Exercise 11.3b & 11.3c: Student Class with Array Initialization
class Student:
    def __init__(self, name='', weight=0.0, height=0.0):
        self.name = name
        self.weight = weight
        self.height = height
        self.bmi = self.calculate_bmi()
        self.grades = np.zeros(10)
        self.mean_grade = 0.0

    def calculate_bmi(self):
        if self.height > 0:
            return self.weight / (self.height ** 2)
        return 0

    def calculate_mean(self):
        self.mean_grade = np.mean(self.grades)
        return self.mean_grade

# Example for 100 Students (Truncated loop for demonstration)
# students_array = np.empty(100, dtype=object)
# for i in range(2): # Test with 2
#     students_array[i] = Student()
#     students_array[i].name = input(f'Student {i+1} Name: ')
#     students_array[i].weight = float(input('Weight (kg): '))
#     students_array[i].height = float(input('Height (m): '))
#     students_array[i].bmi = students_array[i].calculate_bmi()
#     print('Student %s has %.2f BMI' % (students_array[i].name, students_array[i].bmi))
