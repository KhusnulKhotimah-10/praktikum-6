def tambah(data_mahasiswa):
  nama = input("Masukkan nama mahasiswa: ")
  nilai = float(input("Masukkan nilai mahasiswa: "))
  data_mahasiswa.append({"nama": nama, "nilai": nilai})
  print("Data mahasiswa berhasil ditambahkan.")

def tampilkan(data_mahasiswa):
  if not data_mahasiswa:
    print("Data mahasiswa masih kosong.")
  else:
    print("Daftar Nilai Mahasiswa:")
    print("--------------------------")
    for mahasiswa in data_mahasiswa:
      print(f"Nama: {mahasiswa['nama']} , Nilai: {mahasiswa['nilai']}")
      print("--------------------------")

def hapus(data_mahasiswa, nama):
  for i, mahasiswa in enumerate(data_mahasiswa):
    if mahasiswa['nama'] == nama:
      del data_mahasiswa[i]
      print(f"Data mahasiswa dengan nama {nama} berhasil dihapus.")
      return
  print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

def ubah(data_mahasiswa, nama):
  for mahasiswa in data_mahasiswa:
    if mahasiswa['nama'] == nama:
      nilai_baru = float(input("Masukkan nilai baru: "))
      mahasiswa['nilai'] = nilai_baru
      print(f"Data mahasiswa dengan nama {nama} berhasil diubah.")
      return
  print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

# Inisialisasi data mahasiswa
data_mahasiswa = []

# Menu program
while True:
  print("\nMenu:")
  print("1. Tambah data mahasiswa")
  print("2. Tampilkan data mahasiswa")
  print("3. Hapus data mahasiswa")
  print("4. Ubah data mahasiswa")
  print("5. Keluar")
  pilihan = input("Pilih menu (1/2/3/4/5): ")

  if pilihan == '1':
    tambah(data_mahasiswa)
  elif pilihan == '2':
    tampilkan(data_mahasiswa)
  elif pilihan == '3':
    nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
    hapus(data_mahasiswa, nama)
  elif pilihan == '4':
    nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
    ubah(data_mahasiswa, nama)
  elif pilihan == '5':
    break
  else:
    print("Pilihan tidak valid.")