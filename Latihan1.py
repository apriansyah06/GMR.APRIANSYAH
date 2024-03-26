def hitung_diskon(total_belanja):
    if total_belanja >= 250.000:
        diskon = total_belanja * 50 / 100
        return diskon
    else:
        return None

total_belanjaan = float(input("Masukkan total belanjaan: Rp. "))
diskon = hitung_diskon(total_belanjaan)

if diskon != None:
    print(f"Diskon yang diterima: Rp {diskon}")
else:
    print(f"Anda tidak mendapatkan diskon karena total belanjaan tidak mencapai Rp 250.000. Total belanjaan Anda: Rp {total_belanjaan}")
