def interpolasi_linier(x_data, y_data, x_interpolasi):
    n = len(x_data)
    
    if len(y_data) != n:
        raise ValueError("Jumlah nilai y harus sama dengan jumlah nilai x")
    
    for i in range(n-1):
        if not (x_data[i] < x_interpolasi <= x_data[i+1]):
            continue
        
        # Metode interpolasi linier
        x0, y0 = x_data[i], y_data[i]
        x1, y1 = x_data[i+1], y_data[i+1]
        
        nilai_interpolasi = y0 + (y1 - y0) * (x_interpolasi - x0) / (x1 - x0)
        return nilai_interpolasi
    
    raise ValueError(f"Tidak dapat melakukan interpolasi untuk nilai x={x_interpolasi}")

# Input data x dan y dari pengguna
x_data = list(map(float, input("Masukkan nilai x (pisahkan dengan spasi): ").split()))
y_data = list(map(float, input("Masukkan nilai y (pisahkan dengan spasi): ").split()))

# Input nilai x yang ingin diinterpolasi
x_interpolasi = float(input("Masukkan nilai x yang ingin diinterpolasi: "))

# Melakukan interpolasi
hasil_interpolasi = interpolasi_linier(x_data, y_data, x_interpolasi)

# Menampilkan hasil interpolasi
print(f"\nHasil interpolasi untuk x = {x_interpolasi}: {hasil_interpolasi}")
