daftar_buku = ["Pulang", "Pergi", "Lumpu", "Nebula", "Hujan"]
pinjaman = []

print("DAFTAR BUKU =")
for buku in daftar_buku:
    print("-", buku)

while True:
    print("1. Pinjam")
    print("2. Ubah")
    print("3. Hapus")
    print("4. Selesai")

    pilih = input("Pilih: ")

    if pilih == "1":
        buku = input("Buku yang ingin dipinjam: ")

        if buku in daftar_buku:
            pinjaman.append(buku)
            print("Buku berhasil dipinjam.")
        else:
            print("Buku tidak tersedia.")

    elif pilih == "2":
        print("Pinjaman:", pinjaman)

        if pinjaman:
            nomor = int(input("Nomor buku yang ingin diubah: ")) - 1
            baru = input("Masukkan buku baru: ")

            if nomor >= 0 and nomor < len(pinjaman):
                pinjaman[nomor] = baru
                print("Buku berhasil diubah.")
            else:
                print("Nomor tidak valid.")
        else:
            print("Belum ada buku yang dipinjam.")
    elif pilih == "3":
        print("Pinjaman:", pinjaman)

        if pinjaman:
            nomor = int(input("Nomor buku yang ingin dihapus: ")) - 1

            if nomor >= 0 and nomor < len(pinjaman):
                pinjaman.pop(nomor)
                print("Buku berhasil dihapus.")
            else:
                print("Nomor bukunya tidak valid.")
        else:
            print("Belum ada buku yang dipinjam.")

    elif pilih == "4":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")

print("BUKU YANG DIPINJAM ADALAH :")
for buku in pinjaman:
    print("-", buku)