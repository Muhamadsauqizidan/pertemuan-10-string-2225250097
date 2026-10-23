
# Tugas: Normalisasi Data Mahasiswa
# Nama: Muhamad Sauqi Zidan

def normalisasi_nama(nama):
    return " ".join(nama.strip().split()).title()


def buat_inisial(nama):
    kata = normalisasi_nama(nama).split()
    return "".join(item[0] for item in kata)


def normalisasi_kode(kode):
    kata = kode.strip().upper().split()
    return "-".join(kata)


nama = input("Nama: ")
kode = input("Kode kelas: ")

nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)

print("\nHasil Normalisasi")
print(f"Nama bersih : {nama_bersih}")
print(f"Kode kelas  : {kode_bersih}")
print(f"Jumlah kata : {len(nama_bersih.split())}")
print(f"Inisial     : {buat_inisial(nama)}")
