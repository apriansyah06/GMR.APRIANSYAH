def hitung_nilai_akhir(kehadiran, nilai_tugas, nilai_uts, nilai_uas):
    total_kehadiran = kehadiran * 16
    total_nilai_tugas = sum(nilai_tugas) / len(nilai_tugas)
    nilai_akhir = total_kehadiran + total_nilai_tugas + nilai_uts + nilai_uas
    return nilai_akhir

def tentukan_hasil_nilai(nilai_akhir):
    if nilai_akhir >= 90:
        return "A"
    elif nilai_akhir >= 80:
        return "B"
    elif nilai_akhir >= 70:
        return "C"
    elif nilai_akhir >= 60:
        return "D"
    else:
        return "E"

kehadiran = int(input("Masukkan jumlah kehadiran: "))
nilai_tugas = [float(input(f"Masukkan nilai tugas ke-{i+1}: ")) for i in range(8)]
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = hitung_nilai_akhir(kehadiran, nilai_tugas, nilai_uts, nilai_uas)
hasil_nilai = tentukan_hasil_nilai(nilai_akhir)

print(f"Nilai akhir: {nilai_akhir}")
print(f"Hasil nilai kelulusan: {hasil_nilai}")
