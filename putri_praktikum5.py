motor=["vario","motor matic","150","hitam","dua"]
motor.append("24000000")
motor.append("matic")
motor.insert(2,"honda")
print(motor)

ket= """selamat datang di aplikasi menghitung luas bangun datar masukan pilihan :
    1. untuk menghitung luas persegi 
    2. untuk menghitung luas lingkaran
    3. untuk menghitung segitiga
    pilihan :"""

pilihan = input(ket)
match pilihan:
    case "1":
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi =int (input("masukan sisi ?"))
        luas  = sisi*sisi
        print("luas persegi yang sisinya",sisi,"adalah", luas)
    case "2":
        print("kamu memilih 2 untuk menghitung luas lingkaran")  
        r = float(input("masukan jari2 ?"))
        luas = 3.14*r*r
        print("luas lingkaran yang jari2nya",r,"adalah", luas)
    case "3":
        print("kamu memilih 3 untuk menghitung luas segitiga")
        alas =int (input("masukan alas ?"))
        tinggi = int (input("masukan tinggi ?"))
        luas = 0.5*alas*tinggi
        print("luas segitiga yang alasnya",alas,"tingginya",tinggi,"adalah" ,luas)
    case _:
        print("salah memilih pilihan")