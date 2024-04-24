import random

daftar_teater = ["Teater A", "Teater B", "Teater C", "Teater D", "Teater E"]

genre_film = ["Action", "Drama", "Komedi", "Horor", "Petualangan", "Dokumenter"]

while True:
    print("Daftar Genre Film:")
    for i, genre in enumerate(genre_film):
        print(f"{i+1}. {genre}")
    genre_pilihan = int(input("Pilih jenis genre film (nomor): "))
    if 1 <= genre_pilihan <= len(genre_film):
        break
    print("Pilihan genre tidak valid!")

film_genre = []
if genre_film[genre_pilihan-1] == "Action":
    film_genre = ["Lift", "John Wick", "The Matrix", "Mission: Impossible", "Fast & Furious"]
elif genre_film[genre_pilihan-1] == "Drama":
    film_genre = ["Laskar pelangi", "filosofi kopi", "dua garis biru", "keluarga cemara"]
elif genre_film[genre_pilihan-1] == "Komedi":
    film_genre = ["Warkop DKI", "susah sinyal", "my stupid boss", "terlalu tampan", "agak lain"]
elif genre_film[genre_pilihan-1] == "Horor":
    film_genre = ["Pengabdi setan", "KKN desa penari", "jelangkung", "rumah dara", "keramat"]
elif genre_film[genre_pilihan-1] == "Petualangan":
    film_genre = ["Hangout", "Ben dan jody", "petualangan sherina", "salawaku", "lost in papua"]
elif genre_film[genre_pilihan-1] == "Dokumenter":
    film_genre = ["pulau plastik", "ice cold", "senyap", "negeri dogeng", "dibalik kilang"]
else:
    print("Genre film tidak tersedia")

while True:
    print(f"List Film {genre_film[genre_pilihan-1]}:")
    for i, film in enumerate(film_genre):
        print(f"{i+1}. {film}")
    film_pilihan = int(input("Pilih jenis film (nomor): "))
    if 1 <= film_pilihan <= len(film_genre):
        break
    print("Pilihan film tidak valid!")

film_detail = {
    "nama": film_genre[film_pilihan-1],
    "waktu": "15:00 - 17:00 WIT",
    "harga": {
        "hari_biasa": 35000,
        "sabtu": 45000,
        "minggu": 50000
    }
}

print("\nDetail Film:")
print(f"Nama Film: {film_detail['nama']}")
print(f"Waktu: {film_detail['waktu']}")
hari = input("Masukkan hari pembelian (hari biasa/sabtu/minggu): ").lower()
if hari not in film_detail["harga"]:
    print("Hari tidak valid!")
    exit()

harga_tiket = film_detail["harga"][hari]
print(f"Harga Tiket: Rp {harga_tiket}")

teater_terpilih = random.choice(daftar_teater)
print(f"Teater: {teater_terpilih}")

konfirmasi = input("Apakah Anda ingin membeli tiket? [Y/T]: ").upper()
if konfirmasi != "Y":
    print("Pembelian tiket dibatalkan!")
    exit()

while True:
    try:
        quantity = int(input("Quantity Jumlah Tiket: "))
        if quantity <= 0:
            raise ValueError
        break
    except ValueError:
        print("Quantity harus berupa bilangan bulat positif!")

pembeli = []
for i in range(quantity):
    nama = input(f"Masukkan Nama ({i+1}/{quantity}): ")
    usia = int(input(f"Masukkan Usia ({i+1}/{quantity}): "))
    pembeli.append({"nama": nama, "usia": usia})

for pelanggan in pembeli:
    if pelanggan["usia"] <= 17:
        print(f"{pelanggan['nama']} tidak diperbolehkan menonton karena usia di bawah 17 tahun.")
        exit()

print("\nInvoice Tiket")
for i, pelanggan in enumerate(pembeli):
    print(f"{i+1} Nama: {pelanggan['nama']}")
    print(f"   Usia: {pelanggan['usia']}")
print(f"Film: {film_detail['nama']}")
print(f"Waktu: {film_detail['waktu']}")
print(f"Teater: {teater_terpilih}")
print(f"Quantity: {quantity}")
print(f"Total Harga: Rp {harga_tiket * quantity}")

print("\nTerima kasih atas pembelian Anda!")