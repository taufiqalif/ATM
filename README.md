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

for disini untuk melakukan perulangan dan mengecek apakah parameter p(pin)
yang kita masukan saat pertama kali menggunakan ATM sama/ada di dalam variable user(array)
