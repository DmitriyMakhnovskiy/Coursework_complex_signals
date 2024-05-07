#
# A coursework on complex signals.
# Calculation of the current waveform in a LR-circuit for a given voltage waveform with harmonics
#
# Dr. Dmitriy Makhnovskiy, City College Plymouth, England.
# 07.05.2024

import math  # math library

pi = math.pi  # pi = 3.1415926535897932384626433832795

print('')
R = float(input('Resistance (Ohm) = '))
L = float(input('Inductance (Henry) = '))
w = float(input('Angular frequency (rad/s) = '))
mode = (input('Are the harmonics odd/even/both? Enter the key word = ')).lower()  # lower case input string
N = int(input('Number of harmonics in addition to the DC offset = '))

# Calculating the index of a harmonic from its ordinal number, for example, "first odd harmonic = 3w",
# "second odd harmonic = 5w", etc. Or, "first even harmonic = 2w", "second even harmonic = 4w", etc.
# Here, w is the angular frequency.
def index(m, mode):
    return {'odd': 2 * m - 1, 'even': 2 * m, 'both': m}.get(mode)

V, Z, vphase, I, iphase = [0] * (2 * N + 1), [0] * (2 * N + 1), [0] * (2 * N + 1), [0] * (2 * N + 1), [0] * (2 * N + 1)
V[0] = float(input('DC offset (V) = '))
Z[0] = R  # impedance for the DC offset
I[0] = V[0] / R  # current zero harmonic
I[0] = round(I[0], 3)  # rounding to three decimal places
for m in range(1, N + 1):
    k = index(m, mode)
    message = f'Amplitude (V) of the {k}-th voltage harmonic = '
    V[k] = float(input(message))
    message = f'Phase (degrees) of the {k}-th voltage harmonic = '
    vphase[k] = float(input(message))  # phase (degrees) of the k-th voltage harmonic
    vphase[k] = (vphase[k] * pi) / 180.0  # converting degrees to radians
    Z[k] = (R**2 + (k * w * L)**2)**0.5  # impedance module for the k-th current harmonic

# Current harmonic amplitudes and phases
for m in range(1, N + 1):
    k = index(m, mode)
    I[k] = V[k] / Z[k]
    iphase[k] = -math.atan((k * w * L) / R)  # lagging phase for an inductive load

# RMS voltage and current amplitudes, and power dissipated
Vrms = math.sqrt(sum(V[k]**2 / 2.0 for m in range(1, N + 1) for k in [index(m, mode)]) + V[0]**2)
Irms = math.sqrt(sum(I[k]**2 / 2.0 for m in range(1, N + 1) for k in [index(m, mode)]) + I[0]**2)
Pw = Irms**2 * R  # power dissipated
print('')
print('Vrms = ', round(Vrms, 3))  # rounding to three decimal places
print('Irms = ', round(Irms, 3))  # rounding to three decimal places
print('Power dissipated (W) = ', round(Pw, 3))

print('')
print('Amplitudes of the current harmonics:')
print('I[0] = ', I[0])
for m in range(1, N + 1):
    k = index(m, mode)
    value = round(I[k], 3)
    print(f'I[{k}] = {value}')

print('')
print('Impedance modules for the current harmonics:')
print('Z[0] = ', Z[0])
for m in range(1, N + 1):
    k = index(m, mode)
    value = round(Z[k], 3)
    print(f'Z[{k}] = {value}')

print('')
print('Phases for the current harmonics with respect to the voltage harmonics, rad (degrees):')
for m in range(1, N + 1):
    k = index(m, mode)
    rad = round(iphase[k], 3)
    deg = iphase[k] * 180 / pi
    deg = round(deg, 3)
    print(f'Current phase[{k}] = {rad}, ({deg})')

print('')
print('Final phases for the current harmonics, rad (degrees):')
for m in range(1, N + 1):
    k = index(m, mode)
    rad = vphase[k] + iphase[k]
    deg = rad * 180 / pi
    rad = round(rad, 3)
    deg = round(deg, 3)
    print(f'Current phase[{k}] = {rad}, ({deg})')










