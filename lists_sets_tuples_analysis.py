# =========================================================
# Chapter: Lists, Sets, and Tuples Operations
# =========================================================
import numpy as np
import statistics as st
import random

# --- TUPLES & LISTS DATA LOADING ---
def load_data():
    fNames = ['MeanValue', 'Standard Deviation', 'Skewness', 'Kurtosis']
    class1 = [
        [108.1950, 13.5221, -1.0055, 11.0401],
        [99.8163, 31.3452, -2.6173, 8.696],
        [111.5397, 18.4778, -4.3821, 27.3046],
        [100.6440, 18.9230, -1.8641, 11.7788],
        [105.0272, 29.3023, -2.9349, 10.9273]
    ]
    class2 = [
        [117.5737, 15.3925, 0.7161, 4.5726],
        [135.0317, 30.6515, -3.1319, 14.7424],
        [148.3923, 17.6253, 0.3425, 2.7406],
        [126.0227, 12.5781, 0.2463, 3.3957],
        [151.8639, 15.5172, -0.4474, 2.5267]
    ]
    return class1, class2, fNames

class1, class2, fNames = load_data()
c1_np = np.array(class1)
c2_np = np.array(class2)

# Max/Min operations
print('Max Value of 1st column (Class 1): %.4f' % np.max(c1_np[:, 0]))
print('Min Value of 2nd column (Class 2): %.4f' % np.min(c2_np[:, 1]))

print('Row with Max in Class 1:', c1_np[np.argmax(c1_np[:, 0])])
print('Row with Min in Class 2:', c2_np[np.argmin(c2_np[:, 1])])

# Combine classes
class3 = class1[:4] + class2[-4:]
X_combined = class1 + class2

# Compute and print stats for a given dataset using Tuples logic
def compute_column_stats(dataset, column_idx):
    col_data = [row[column_idx] for row in dataset]
    print(f"\nStats for Column {column_idx}:")
    print(f"Mean: {np.mean(col_data):.4f}")
    print(f"Median: {st.median(col_data):.4f}")
    print(f"Std Dev: {st.stdev(col_data):.4f}")
    print(f"Max: {np.max(col_data):.4f}")
    print(f"Min: {np.min(col_data):.4f}")

compute_column_stats(X_combined, 1)

# --- SETS OPERATIONS ---
names = ['Giorgos', 'Giannis', 'Maria', 'Eleni', 'Sophia', 'Nicholas']
surnames = ['Argyrou', 'Basileiou', 'Iliou', 'Theodorou', 'Spyrou']

def create_patient_group(size=20): # Reduced size for testing
    patients = set()
    while len(patients) < size:
        patients.add(f"{random.choice(names)} {random.choice(surnames)}")
    return patients

ultrasound_unit = create_patient_group()
ct_unit = create_patient_group()

only_one_unit = ultrasound_unit ^ ct_unit
both_units = ultrasound_unit & ct_unit

print(f'\nPatients that visited only ONE unit: {len(only_one_unit)}')
print('Names:\n' + '\n'.join(only_one_unit))

print(f'\nPatients that visited BOTH units: {len(both_units)}')
print('Names:\n' + '\n'.join(both_units))
