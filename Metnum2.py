import numpy as np
import matplotlib.pyplot as plt

# Fungsi my_bisection digunakan untuk mencari akar fungsi f(x) dalam interval [a, b]
# dengan toleransi galat e dan maksimal n iterasi.
def my_bisection(f, a, b, e, n):
    if np.sign(f(a)) == np.sign(f(b)):                                       # periksa apakah tanda fungsi di a dan b sama. Jika ya, tidak mungkin ada akar dalam interval tersebut.
        raise Exception('Tidak ada akar pada interval a dan b')

    for i in range(n):                                                       # Menghitung titik tengah interval.
        m = (a + b) / 2
        if np.abs(f(m)) < e:                                                 # Jika nilai absolut f(m) < e, maka akar sudah cukup mendekati, maka m adalah akar yang diinginkan.
            return m
        if np.sign(f(a)) == np.sign(f(m)):                                   # Jika tanda fungsi di a dan m sama, maka kita mencari akar dalam interval [m, b].
            a = m
        else:
            b = m                                                            # Nilai terakhir yang ditemukan adalah perkiraan akar.
    last_value = (a + b) / 2
    return last_value

# Meminta pengguna untuk memasukkan fungsi, interval, toleransi galat, dan jumlah iterasi.
input_f = input("Masukkan fungsi f(x): ")
input_a = float(input("Masukkan interval bawah (a): "))
input_b = float(input("Masukkan interval atas (b): "))
input_e = float(input("Masukkan toleransi galat (e): "))
input_n = int(input("Masukkan jumlah iterasi (n): "))

def user_function(x):                                                        # Membuat fungsi user_function dari input pengguna.
    try:
        return eval(input_f)
    except:
        raise Exception('Fungsi tidak valid')

c = my_bisection(user_function, input_a, input_b, input_e, input_n)          # Menggunakan metode biseksi untuk mencari akar fungsi.

x = np.linspace(input_a, input_b, 400)                                       # Membuat array x dan y untuk grafik fungsi.
y = [user_function(xi) for xi in x]

akar_x = [c]                                                                 # Mencari titik akar pada grafik.
akar_y = [user_function(c)]

plt.plot(x, y, label='f(x)')                                                 # Membuat grafik fungsi dan menandai akar dengan marker.
plt.scatter(akar_x, akar_y, color='red', marker='o', label=f'Akar (x={c:.4f})')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title('Grafik Fungsi dan Akar')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()

print("   /|")                                                               # Menampilkan tanda akar dalam bentuk teks.
print("  / |")
print(" /  |")
print(f"\\_| Akar (x={c:.4f})")  # Menggunakan \\ untuk menampilkan karakter '\'
