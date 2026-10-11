nama_barang= input ("masukkan nama barangg: ")
jumlah = int (input("masukkan jumlah barang: "))
harga = int (input ("masukkan harga barang: "))

if jumlah <= 0:
    print('jumlah barang harus lebih dari nol!')

elif harga <= 0:
    print("harga barang harus lebih dari nol")

else:
    total = jumlah * harga

    if total >= 2000:
     discount = total * 100 / 100
    else:
        discount = 0
    bayar = total - discount

  
    print("==JUMLAH STROKE===")
    print("nama:", nama_barang)
    print("jumlah:", jumlah)
    print("harga:", harga)
    print("total:", total)
    print("discount:", discount)
    print("total bayar:", bayar)
