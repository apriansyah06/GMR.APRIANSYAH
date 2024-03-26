data_mahasiswa = {
    "user1": "password1",
}

data_mata_kuliah = {
    "1": "Pak Syarif",
    "2": "Pak Amal",
    "3": "Pak Yasir",
}

data_dosen_detail = {
    "Pak Syarif": {
        "Mata Kuliah": "Matematika Diskrit",
        "Jam Perkuliahan": "Senin, 08.00 - 10.00",
        "Ruangan": "JT01",
    },
    "Pak Amal": {
        "Mata Kuliah": "Logika Matematika",
        "Jam Perkuliahan": "Selasa, 10.00 - 12.00",
        "Ruangan": "JT02",
    },
    "Pak Yasir": {
        "Mata Kuliah": "Dasar Pemrograman",
        "Jam Perkuliahan": "Rabu, 13.00 - 15.00",
        "Ruangan": "JT03",
    },
}

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username in data_mahasiswa and data_mahasiswa[username] == password:
    print("Login berhasil!")

    print("Daftar Dosen Pengampuh:")
    for mata_kuliah, dosen in data_mata_kuliah.items():
        print(f"{mata_kuliah}: {dosen}")

    pilihan_mata_kuliah = input("Pilih mata kuliah untuk melihat detail dosen pengampuh: ")
    if pilihan_mata_kuliah in data_mata_kuliah:
        dosen_pengampuh = data_mata_kuliah[pilihan_mata_kuliah]
        detail_dosen = data_dosen_detail[dosen_pengampuh]
        print(f"Detail Dosen Pengampuh untuk Mata Kuliah '{pilihan_mata_kuliah}':")
        print(f"Nama Dosen: {dosen_pengampuh}")
        print(f"Mata Kuliah: {detail_dosen['Mata Kuliah']}")
        print(f"Jam Perkuliahan: {detail_dosen['Jam Perkuliahan']}")
        print(f"Ruangan: {detail_dosen['Ruangan']}")
    else:
        print("Mata kuliah tidak ditemukan!")
else:
    print("Username atau password salah. Login gagal!")
