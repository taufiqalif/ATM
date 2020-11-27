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


def cek_login(p):
    for us in user:
        if us['pin'] == p:
            return us
    return False


def cek_user(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return int(i)
    return -1


def cek_rekening(no):
    for i in range(len(user)):
        if str(user[i]['no_rekening']) == str(no):
            return int(i)
    return -1


def tranfer_uang(uang, no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] = user[index1]['saldo'] - int(uang)
            user[index2]['saldo'] = user[index2]['saldo'] + int(uang)
            print("Anda berhasil mentransfer uang Rp." +
                  str(uang)+" ke Rekening "+no_rekening)
            print("sisa saldo anda adalah Rp.", user[index1]['saldo'])
        else:
            print("Ops saldo anda tidak cukup")


def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] = user[index1]['saldo'] - int(uang)
            print("Anda berhasil menarik uang Rp."+str(uang))
            print("sisa saldo anda adalah Rp.", user[index1]['saldo'])
        else:
            print("Ops saldo anda tidak cukup")


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
