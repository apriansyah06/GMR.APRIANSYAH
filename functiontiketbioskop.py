import random

def pilih_genre():
    while True:
        print("Daftar Genre Film:")
        for i, genre in enumerate(genre_film):
            print(f"{i+1}. {genre}")
        genre_pilihan = int(input("Pilih jenis genre film (nomor): "))
        if 1 <= genre_pilihan <= len(genre_film):
            return genre_pilihan
        print("Pilihan genre tidak valid!")

def pilih_film(genre_pilihan):
    film_genre = []
    if genre_film[genre_pilihan-1] == "Action":
        film_genre = ["Lift", "John Wick", "The Matrix", "Mission: Impossible", "Fast & Furious"]
    elif genre_film[genre_pilihan-1] == "Drama":
        film_genre = ["Laskar Pelangi", "Filosofi Kopi", "Dua Garis Biru", "Keluarga Cemara"]
    elif genre_film[genre_pilihan-1] == "Komedi":
        film_genre = ["Warkop DKI", "Susah Sinyal", "My Stupid Boss", "Terlalu Tampan", "Agak Lain"]
    elif genre_film[genre_pilihan-1] == "Horor":
        film_genre = ["Pengabdi Setan", "KKN Desa Penari", "Jelangkung", "Rumah Dara", "Keramat"]
    elif genre_film[genre_pilihan-1] == "Petualangan":
        film_genre = ["Hangout", "Ben dan Jody", "Petualangan Sherina", "Salawaku", "Lost in Papua"]
    elif genre_film[genre_pilihan-1] == "Dokumenter":
        film_genre = ["Pulau Plastik", "Ice Cold", "Senyap", "Negeri Dongeng", "Dibalik Kilang"]
    else:
        print("Genre film tidak tersedia")
        return []

    while True:
        print(f"List Film {genre_film[genre_pilihan-1]}:")
        for i, film in enumerate(film_genre):
            print(f"{i+1}. {film}")
        film_pilihan = int(input("Pilih jenis film (nomor): "))
        if 1 <= film_pilihan <= len(film_genre):
            return film_genre[film_pilihan-1]
        print("Pilihan film tidak valid!")

def detail_film(film_nama):
    return {
        "nama": film_nama,
        "waktu": "15:00 - 17:00 WIT",
        "harga": {
            "hari_biasa": 35000,
            "sabtu": 45000,
            "minggu": 50000
        }
    }

def pembelian_tiket(film_detail):
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

daftar_teater = ["Teater A", "Teater B", "Teater C", "Teater D", "Teater E"]

genre_film = ["Action", "Drama", "Komedi", "Horor", "Petualangan", "Dokumenter"]

genre_pilihan = pilih_genre()
film_nama = pilih_film(genre_pilihan)
film_detail = detail_film(film_nama)
pembelian_tiket(film_detail)
