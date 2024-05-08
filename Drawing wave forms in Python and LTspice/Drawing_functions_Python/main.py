#
# Drawing several waveforms mentioned in "LTspice for complex signals.pdf"
#

import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f1(x):
    return x**2

def f2(x):
    result = np.zeros_like(x)  # Create an array to store results with the same shape as x
    mask = (0.0 <= x) & (x <= 0.5)  # Boolean mask for the condition

    result[mask] = np.cos(np.pi * x[mask])  # Calculate only for elements satisfying the condition
    return result

# Define the ranges for both functions
x_values_f1 = np.linspace(-np.pi, np.pi, 1000)  # [-pi, pi] for f1(x)
x_values_f2 = np.linspace(0, 1, 1000)  # [0, 1] for f2(x)

# Calculate periodical continuations for both functions
f1_extended = np.tile(f1(x_values_f1), 3)  # Extend f1(x) for six periods
f2_extended = np.tile(f2(x_values_f2), 3)  # Extend f2(x) for three periods

# Generate x-values for the extended range for both functions
x_extended_f1 = np.linspace(-np.pi, 5 * np.pi, len(f1_extended))  # Generate x-values for extended range for f1(x)
x_extended_f2 = np.linspace(0, 3, len(f2_extended))  # Generate x-values for extended range for f2(x)

# Plotting f1(x) and its periodical continuation for [-pi, 5pi]
plt.figure(figsize=(8, 6))

# Plotting f1(x)
plt.plot(x_extended_f1, f1_extended, label='f1(x) = x^2 (Periodic)', color='blue')
plt.title('Periodical Continuation of f1(x) for [-pi, 5pi]')
plt.xlabel('x')
plt.ylabel('f1(x)')
plt.legend()
plt.grid(True)
plt.show()

# Plotting f2(x) and its periodical continuation for [0, 3]
plt.figure(figsize=(8, 6))

# Plotting f2(x) = exp(-x)
plt.plot(x_extended_f2, f2_extended, label='f2(x) = cos(pi * x), x = [0, 0.5] & f2(x) = 0, x = [0.5, 1] (Periodic)', color='orange')
plt.title('Periodical Continuation of f2(x) for [0, 3]')
plt.xlabel('x')
plt.ylabel('f2(x)')
plt.legend()
plt.grid(True)
plt.show()
