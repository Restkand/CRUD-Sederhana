Mahasiswa = ["Dodi", "Joko"]

def show_data():
    if len(Mahasiswa) <= 0:
        print ("Data belum ada")
    else:
        for Indeks in range(len(Mahasiswa)):
            print("[%d] %s" %(Indeks, Mahasiswa[Indeks]))

def insert_data():
    mahasiswaBaru = input ("Masukan nama mahasiswa baru : ")
    Mahasiswa.append(mahasiswaBaru)

def edit_data():
    show_data()
    Indeks = int(input ("Masukan nomor ID : "))
    if (Indeks > len(Mahasiswa)):
        print ("ID yang anda masukan salah")
    else :
        namaBaru = input("Masukan nama baru : ")
        Mahasiswa[Indeks] = namaBaru

def delete_data():
    show_data()
    Indeks = int(input ("Masukan nomor ID : "))
    if (Indeks > len(Mahasiswa)):
        print ("ID yang anda masukan salah")
    else :
        Mahasiswa.remove(Mahasiswa[Indeks])

