# A

usia = 50
usia_setengah = usia / 2
sapaan = 'Halo '
nama = 'Paul'
menyapa = sapaan + nama
print(menyapa + ", umur saya " + str(usia_setengah) + " tahun.")

list_belanja = ['telur', 'mentega', 'susu', 'apel', 'jus', 'sereal']
elemen_akhir=list_belanja[-1]
print(elemen_akhir)


nilai = 90
ipk = 2.7

if not nilai >= 90:
    print("Anda tidak memiliki cukup kredit untuk lulus")
if not ipk >= 3.0:
    print("IPK Anda tidak cukup tinggi untuk lulus.")
if not (nilai >= 90) and not (ipk >=3.0):
    print("Anda tidak memenuhi salah satu persyaratan untuk lulus!")