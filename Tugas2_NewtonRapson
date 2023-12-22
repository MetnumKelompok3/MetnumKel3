import matplotlib.pyplot as plt
import numpy as np

# Membaca fungsi f(x) dari pengguna
user_input_f = input("Masukkan fungsi f(x) dalam bentuk Python: ")
def f(x):
    return eval(user_input_f)

# Membaca fungsi g(x) dari pengguna
user_input_g = input("Masukkan fungsi g(x) dalam bentuk Python: ")
def g(x):
    return eval(user_input_g)

# Mendefinisikan fungsi metode newtonRaphson
def newtonRaphson(x0, e, N):
    step = 1
    flag = 1
    condition = True

    # List untuk menyimpan nilai iterasi
    x_values = [x0]
    f_values = [f(x0)]

    while condition:
        if g(x0) == 0.0:
            print('Dibagi 0 error')
            break

        # Loop iterasi
        x1 = x0 - f(x0)/g(x0)
        x_values.append(x1)
        f_values.append(f(x1))

        print('Iterasi-%d, x1 = %0.6f dan f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nakar yang dibutuhkan : %0.8f' % x1)
    else:
        print('\ntidak konvergen')

    # Plot grafik fungsi
    x = np.linspace(min(x_values) - 1, max(x_values) + 1, 400)
    y = f(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)')
    plt.scatter(x_values, f_values, color='red', marker='o', label='Iterasi Newton-Raphson')
    plt.title('Grafik Fungsi dan Iterasi Newton-Raphson')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Convert inputan ke tipe data float
x0 = input('Perkiraan: ')
x0 = float(x0)
e = input('Perkiraan Error: ')
e = float(e)

# Convert inputan ke tipe data int
N = input('Jumlah Step: ')
N = int(N)

newtonRaphson(x0, e, N)
