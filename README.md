# Sistem ATM

![system_ATM_0.png](/gambar/system_ATM_0.png)


### Membuat Variable Utama

    user_id = 0
    loop = "n"
    user = [
        {
            "id": "1234",
            "no_rekening": "312010289",
            "username": "Taufiq",
            "pin": "1497",
            "saldo": 1000000000
        },
        {
            "id": "4321",
            "no_rekening": "0987654321",
            "username": "Wegi",
            "pin": "1234",
            "saldo": 50000000
        },
        {
            "id": "1497",
            "no_rekening": "312010309",
            "username": "Fajar",
            "pin": "2000",
            "saldo": 100000000
        }
    ]
    status_login = False
    pakai_atm = "y"

**user_id** untuk menyimpan id dari user yang login

**loop** untuk menyimpan kondisi while saat memilih menu ATM ( dimana kita tahu untuk memakai program berulang-ulang di python kita menggunakan while untuk perulangannya )

**user** karena ini program sederhana kita hanya akan menggunakan array statis untuk menyimpan data usernya,untuk lebih lanjut kalian bisa menggunakan database

**status_login** menyimpan status apakah user berhasil login atau tidak

**pakai_atm** menyimpan kondisi apakah kita masih menggunakan ATM atau tidak


### Cek Login

    def cek_login(p):
        for us in user:
            if us['pin'] == p:
                return us
        return False

**for** disini untuk melakukan perulangan dan mengecek apakah parameter p(pin)
yang kita masukan saat pertama kali menggunakan ATM sama/ada di dalam variable user(array)

### Cek User

    def cek_user(id):
        for i in range(len(user)):
            if user[i]['id'] == str(id):
                return int(i)
        return -1

**return -1** karena setalah mengcek user kita akan me-return/mengembalikan nilai dari index variable user karena tipenya array kita perlu index untuk mengaksesnya


### Perulangan While

    while pakai_atm == "y":
        while status_login == False:
            print("=====================================")
            print(">>>>SELAMAT DATANG DI ATM BERSAMA<<<<")
            print("=====================================")
            print(">>>>>>Silahkan masukan pin anda<<<<<<")
            print("=====================================")
            pin = input("Masukan PIN : ")

            cl = cek_login(pin)
            if cl != False:
                print("selamat data "+cl['username'])
                user_id = cl['id']
                status_login = True
                loop = "y"
            else:
                print("Ops PIN anda salah")

        while loop == "y" and status_login == True:
            u = user[cek_user(user_id)]
            print("=====================================")
            print(">>>>SELAMAT DATANG DI ATM BERSAMA<<<<")
            print("=====================================")
            print("1.Cek Saldo")
            print("2.Transfer Uang")
            print("3.Ambil Uang")
            print("4.Logout")
            print("5.Keluar ATM")
            a = int(input("Silahkan pilih menu : "))
            if a == 1:
                print("--------------------------------------")
                print("Sisa Saldo anda adalah Rp.", u['saldo'])
                print("--------------------------------------")
                loop = "n"
            elif a == 2:
                print("----------------------------------------------------------")
                print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
                print("----------------------------------------------------------")
                no_rek = input("Masukan No Rekening Tujuan : ")
                cnk = cek_rekening(no_rek)

                if cnk >= 0:
                    print(
                        "----------------------------------------------------------------------------")
                    print(
                        "Nomor rekening ditemukan,silahkan masukan nominal yang yang akan di transfer")
                    print(
                        "----------------------------------------------------------------------------")
                    nominal = input("Nominal Yang Akan Di Transfer : ")
                    tranfer_uang(nominal, no_rek)
                    print(
                        "--------------------------------------------------------------------------")
                    loop = "n"
                else:
                    print("----------------------------------------------------------")
                    print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                    print("----------------------------------------------------------")
                    loop = "n"

            elif a == 3:
                print("---------------------------------------")
                nominal = input("Nominal Yang Akan Di Tarik : ")
                print("---------------------------------------")
                ambil_uang(nominal)
                print("---------------------------------------")
                loop = "n"
            elif a == 4:
                status_login = False

            elif a == 5:
                status_login = False
                loop = "n"
                pakai_atm = "n"
            else:
                print("pilihan tidak tersedia")
            if status_login == True:

                input("kembali Ke menu (Enter) ")
                print("")
                loop = "y"
