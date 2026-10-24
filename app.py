def format_rupiah(amount: int) -> str:
    return f"Rp{amount:,}".replace(",", ".")


def input_angka(prompt: str, minimum: int = 1) -> int:
    while True:
        try:
            angka = int(input(prompt))
        except ValueError:
            print("Masukkan angka yang valid.")
            continue

        if angka < minimum:
            print(f"Masukkan angka minimal {minimum}.")
            continue
        return angka


menu = {
    1: {"nama": "Nasi goreng", "harga": 15000, "stok": 10},
    2: {"nama": "Es teh", "harga": 5000, "stok": 20},
    3: {"nama": "Mie ayam", "harga": 8000, "stok": 20},
    4: {"nama": "Bakso", "harga": 12000, "stok": 15},
}

print("=== FOOD ORDERING & KASIR ===")
nama_pelanggan = input("Masukkan nama Anda: ").strip()
if not nama_pelanggan:
    nama_pelanggan = "Pelanggan"

pesanan = []

while True:
    print("\n=== MENU ===")
    for nomor, item in menu.items():
        print(
            f"{nomor}. {item['nama']} - {format_rupiah(item['harga'])} "
            f"(stok: {item['stok']})"
        )
    print("0. Selesai memilih")

    pilihan = input_angka("Pilih nomor menu: ", minimum=0)
    if pilihan == 0:
        break
    if pilihan not in menu:
        print("Nomor menu tidak tersedia.")
        continue

    item = menu[pilihan]
    jumlah = input_angka(f"Jumlah {item['nama']}: ")
    if jumlah > item["stok"]:
        print(f"Stok tidak cukup. Stok tersedia: {item['stok']}.")
        continue

    pesanan.append(
        {
            "nama": item["nama"],
            "harga": item["harga"],
            "jumlah": jumlah,
        }
    )
    item["stok"] -= jumlah
    print(f"{item['nama']} ditambahkan ke pesanan.")

if not pesanan:
    print("Belum ada pesanan. Transaksi dibatalkan.")
else:
    subtotal = sum(item["harga"] * item["jumlah"] for item in pesanan)

    print("\nMasukkan kode redeem untuk mendapatkan diskon spesial.")
    kode_redeem = input("Kode redeem (tekan Enter jika tidak ada): ").strip().upper()
    if kode_redeem == "BULKING10":
        diskon = subtotal * 10 // 100
        print("Kode berhasil! Kamu mendapatkan diskon 10%.")
    else:
        diskon = 0
        if kode_redeem:
            print("Kode tidak valid. Diskon tidak diberikan.")

    total_bayar = subtotal - diskon
    print(f"Total setelah diskon: {format_rupiah(total_bayar)}")

    while True:
        uang_dibayar = input_angka("Uang dibayar: ")
        if uang_dibayar < total_bayar:
            print(f"Uang kurang {format_rupiah(total_bayar - uang_dibayar)}.")
            continue
        break

    kembalian = uang_dibayar - total_bayar

    print("\n========== STRUK BELANJA ==========")
    print(f"Pelanggan: {nama_pelanggan}")
    print("-----------------------------------")
    for item in pesanan:
        jumlah_harga = item["harga"] * item["jumlah"]
        print(f"{item['nama']} x{item['jumlah']}")
        print(
            f"  {format_rupiah(item['harga'])} x {item['jumlah']} "
            f"= {format_rupiah(jumlah_harga)}"
        )
    print("-----------------------------------")
    print(f"Subtotal     : {format_rupiah(subtotal)}")
    print(f"Kode redeem  : {kode_redeem or '-'}")
    print(f"Diskon       : -{format_rupiah(diskon)}")
    print(f"Total bayar  : {format_rupiah(total_bayar)}")
    print(f"Uang dibayar : {format_rupiah(uang_dibayar)}")
    print(f"Kembalian    : {format_rupiah(kembalian)}")
    print("===================================")
    print("Terima kasih sudah memesan!")
