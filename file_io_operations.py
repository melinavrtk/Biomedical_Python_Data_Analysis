# =========================================================
# Chapter: File Input/Output Operations
# =========================================================
import numpy as np

# Exercise 12.3a: Write Temperatures to File
with open("tempC.txt", "w") as fid:
    for i in range(3):  # Adjust range for real usage
        t = float(input('Patient temperature (32-42 °C): '))
        while t < 32 or t > 42:
            t = float(input('Error! Enter valid temperature (32-42 °C): '))
        fid.write("%f\n" % t)

# Exercise 12.3b: Read, Convert to Fahrenheit, and Write
with open("tempC.txt", "r") as fid1, open("tempF.txt", "w") as fid2:
    for line in fid1:
        line = line.strip()
        if line:
            celsius = float(line)
            fahrenheit = celsius * (9/5) + 32
            fid2.write("%.2f\n" % fahrenheit)

# Exercise 12.3e: ASCII Character Table Output
with open("ascii.txt", "w") as fid:
    for i in range(32, 127):
        fid.write("%s\t%d\n" % (chr(i), i))

# Exercise 12.3f: Read ASCII Table into Arrays
char_array = [''] * 95
code_array = np.zeros(95, dtype=int)

with open("ascii.txt", "r") as fid:
    for i in range(95):
        line = fid.readline().split('\t')
        if len(line) == 2:
            char_array[i] = line[0]
            code_array[i] = int(line[1].strip())
            print("%s\t%d" % (char_array[i], code_array[i]))
