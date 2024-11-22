# List untuk menyimpan data mahasiswa
data_mahasiswa = []

# Perulangan untuk menambah data
while True:
    print("\nMasukkan data mahasiswa:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas (0-100): "))
    uts = float(input("Nilai UTS (0-100): "))
    uas = float(input("Nilai UAS (0-100): "))

    # Hitung nilai akhir
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

    # Simpan data ke dalam list
    data_mahasiswa.append({
        "Nama": nama,
        "NIM" : nim,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": nilai_akhir
    })

    # Tanya apakah ingin menambah data lagi
    tambah_data = input("\nTambah data lagi? (y/t): ").lower()
    if tambah_data == "t":
        break

# Tampilkan data mahasiswa
print("\nDaftar Data Mahasiswa:")
print("No | Nama       | Tugas | UTS   | UAS   | Nilai Akhir")
print("-" * 50)
for i, data in enumerate(data_mahasiswa, start=1):
    print(f"{i:<3} | {data['Nama']:<10} | {data['Tugas']:<5} | {data['UTS']:<5} | {data['UAS']:<5} | {data['Nilai Akhir']:.2f}")
