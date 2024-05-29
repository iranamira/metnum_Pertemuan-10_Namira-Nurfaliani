import numpy as np
import time
import matplotlib.pyplot as plt

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode Trapezoid
def trapezoid_integration(a, b, N):
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        integral += f(a + i * h)
    integral *= h
    return integral

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]
errors = []
times = []

# Penghitungan untuk setiap N
for N in N_values:
    start_time = time.time()
    pi_approx = trapezoid_integration(0, 1, N)
    end_time = time.time()

    error = np.sqrt((pi_approx - pi_ref) ** 2)
    elapsed_time = end_time - start_time

    errors.append(error)
    times.append(elapsed_time)

    print(f"N = {N}, Approximated pi = {pi_approx}, Error = {error}, Time = {elapsed_time}")

# Plot galat RMS dan waktu eksekusi
plt.figure(figsize=(14, 6))

# Plot Galat RMS
plt.subplot(1, 2, 1)
plt.plot(N_values, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('Galat RMS (log scale)')
plt.title('Galat RMS vs N')

# Plot Waktu Eksekusi
plt.subplot(1, 2, 2)
plt.plot(N_values, times, marker='o')
plt.xscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('Waktu Eksekusi (s)')
plt.title('Waktu Eksekusi vs N')

plt.tight_layout()
plt.show()
