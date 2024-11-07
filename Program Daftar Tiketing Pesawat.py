def menutujuan():
    print("\n===============================")
    print("Program Pemesanan Tiket Pesawat")
    print("===============================")
    print("1. AIR ASIA")
    print("2. BATIK AIR")
    print("3. GARUDA")
    print("4. CITILINK")
    print("5. Exit")
    print("\n===============================")

def pembelian(harga):
    pembeli = input("Nama Pemesan Tiket = ")
    jumlahtiket = int(input("Masukkan Jumlah Tiket Yang Dibeli = "))
    totaltiket = jumlahtiket * harga
    print("Total Pembayaran Anda adalah = Rp" + str(totaltiket))

def main():
    menutujuan()
    tujuan = int(input("Masukkan Pilihan [1-5] = "))

    if tujuan == 1:
        print("\n-------------------------------------------------------")
        print("\nKode  Nama     |   Kota       |   Harga")
        print("\n      Pesawat  |   Tujuan     |   Tiket")
        print("\n-------------------------------------------------------")
        print("\n101.  AIR ASIA |   Bandung    |   Rp.1.500.000")		
        print("\n102.  AIR ASIA |  Surabaya    |   Rp.2.000.000")
        print("\n103.  AIR ASIA |  Jakarta     |   Rp.2.500.000")
        print("\n-------------------------------------------------------")
        nomorpesawat = int(input("Masukan kode penerbangan = "))

        if nomorpesawat == 101:
            harga = 1500000
            pembelian(harga)
        elif nomorpesawat == 102:
            harga = 2000000
            pembelian(harga)
        elif nomorpesawat == 103:
            harga = 2500000
            pembelian(harga)
        else:
            print("Kode Penerbangan Tidak ada di daftar")

    elif tujuan == 2:
        print("\n----------------------------------------------------------")
        print("\nKode  Nama     |        Kota            |  Harga")
        print("\n      Pesawat  |       Tujuan           |  Tiket")
        print("\n----------------------------------------------------------")
        print("\n201. BATIK AIR |       Medan            |  Rp.2.000.000")
        print("\n202. BATIK AIR |     Balikpapan         |  Rp.3.000.000")
        print("\n203. BATIK AIR |       Manado           |  Rp.4.000.000")
        print("\n----------------------------------------------------------")
        nomorpesawat = int(input("Masukan kode penerbangan = "))

        if nomorpesawat == 201:
            harga = 2000000
            pembelian(harga)
        elif nomorpesawat == 202:
            harga = 3000000
            pembelian(harga)
        elif nomorpesawat == 203:
            harga = 4000000
            pembelian(harga)
        else:
            print("Kode Penerbangan Tidak ada di daftar")

    elif tujuan == 3:
        print("\n----------------------------------------------------------")
        print("\nKode  Nama     |        Kota            |  Harga")
        print("\n      Pesawat  |       Tujuan           |  Tiket")
        print("\n----------------------------------------------------------")
        print("\n301. GARUDA    |       Medan            |  Rp.5.000.000")
        print("\n302. GARUDA    |     Balikpapan         |  Rp.6.000.000")
        print("\n303. GARUDA    |       Manado           |  Rp.7.000.000")
        print("\n----------------------------------------------------------")
        nomorpesawat = int(input("Masukan kode penerbangan = "))

        if nomorpesawat == 301:
            harga = 5000000
            pembelian(harga)
        elif nomorpesawat == 302:
            harga = 6000000
            pembelian(harga)
        elif nomorpesawat == 303:
            harga = 7000000
            pembelian(harga)
        else:
            print("Kode Penerbangan Tidak ada di daftar")

    elif tujuan == 4:
        print("\n----------------------------------------------------------")
        print("\nKode  Nama     |        Kota            |  Harga")
        print("\n      Pesawat  |       Tujuan           |  Tiket")
        print("\n----------------------------------------------------------")
        print("\n401. CITILINK  |       Bandung          |  Rp.1.000.000")
        print("\n402. CITILINK  |     Surabaya           |  Rp.1.500.000")
        print("\n403. CITILINK  |       Jakarta          |  Rp.2.000.000")
        print("\n----------------------------------------------------------")
        nomorpesawat = int(input("Masukan kode penerbangan = "))

        if nomorpesawat == 401:
            harga = 1000000
            pembelian(harga)
        elif nomorpesawat == 402:
            harga = 1500000
            pembelian(harga)
        elif nomorpesawat == 403:
            harga = 2000000
            pembelian(harga)
        else:
            print("Kode Penerbangan Tidak ada di daftar")

    elif tujuan == 5:
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")

main()
