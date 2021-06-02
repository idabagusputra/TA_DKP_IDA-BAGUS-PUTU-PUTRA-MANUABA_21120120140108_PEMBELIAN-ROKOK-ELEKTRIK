from tkinter import *
import os
from tkinter import messagebox 
import count_down

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x210")
    main_screen.title("MENU UTAMA PEMBELIAN VAPOR")
    main_screen.iconbitmap("C:/GUI/vape1.ico")
    Label(text="SILAHKAN MASUK", bg="gray", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    main_screen.mainloop()

def register():
    del_main_screen()
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("REGISTER")
    register_screen.geometry("300x250")
    register_screen.iconbitmap("C:/GUI/vape1.ico")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="DAFTARKAN USERNAME DAN PASSWORD ANDA", bg="gray", width="300", height="2", font=("Calibri", 10)).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="USERNAME * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="PASSWORD * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command = register_user).pack()
 
def login():
    del_main_screen()
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("LOGIN")
    login_screen.geometry("300x300")
    login_screen.iconbitmap("C:/GUI/vape1.ico")
    Label(login_screen, text="MASUKAN USERNAME DAN PASSWORD ANDA", bg="gray", width="300", height="2", font=("Calibri", 10)).pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="USERNAME").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="PASSWORD").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="LOGIN", width=10, height=1, command = login_verify).place(x=170,y=179)
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="KEMBALI", width=10, height=1, command = shw_main_screen).place(x=50,y=179)

def login_dari_register():
    del_register_screen()
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("LOGIN")
    login_screen.geometry("300x270")
    login_screen.iconbitmap("C:/GUI/vape1.ico")
    Label(login_screen, text="MASUKAN USERNAME DAN PASSWORD ANDA", bg="gray", width="300", height="2", font=("Calibri", 10)).pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="USERNAME").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="PASSWORD").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="LOGIN", width=10, height=1, command = login_verify).pack()
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    Button(register_screen, text="LOGIN", width=10, height=1, command = login_dari_register).pack()
 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            Label(login_screen, text="LOGIN SUKSES", fg="green", font=("calibri", 11)).pack()
            Button(login_screen, text="LANJUTKAN", width=10, height=1, command = lanjutkan).pack()

        else:
            messagebox.showerror("Error","PASSWORD SALAH")
            return
 
    else:
        messagebox.showerror("Error","PENGGUNA TIDAK DITEMUKAN")
        return
 

def lanjutkan():
    del_login_screen()
    global pendataan_pembeli
    global stringnama
    global stringnohp
    global radio
    global stringalamat
    pendataan_pembeli = Toplevel(login_screen)
    pendataan_pembeli.title("PEDATAAN PEMBELI")
    pendataan_pembeli.geometry("300x260")
    pendataan_pembeli.iconbitmap("C:/GUI/vape1.ico")
    Label(pendataan_pembeli, text="SILAHKAN MASUKAN DATA DIRI ANDA", bg="gray", width="300", height="2", font=("Calibri", 10)).pack()
    lbnama = Label(pendataan_pembeli, text = "Nama\t:").place(x = 30,y = 50)    
    lbjk = Label(pendataan_pembeli, text = "Gender\t:").place(x = 30, y=80)
    lbHP = Label(pendataan_pembeli, text = "No. HP\t:").place(x=30, y=150)
    lbalamat = Label(pendataan_pembeli, text = "Alamat\t:").place(x=30, y=180)
    stringnama = StringVar()
    stringnohp = StringVar()
    stringalamat = StringVar()
    inama = Entry(pendataan_pembeli, width = 20, textvariable=stringnama).place(x = 110, y = 50) 
    iHP = Entry(pendataan_pembeli, width = 20, textvariable=stringnohp).place(x = 110, y = 150) 
    ialamat = Entry(pendataan_pembeli, width = 20, textvariable=stringalamat).place(x = 110, y = 180) 
    radio = IntVar()
    R1 = Radiobutton(pendataan_pembeli, text="Pria", variable=radio, value=1).place(x=105, y=80)  
    R2 = Radiobutton(pendataan_pembeli, text="Wanita", variable=radio, value=2).place(x=105, y=100)
    R3 = Radiobutton(pendataan_pembeli, text="Anak-Anak", variable=radio, value=3).place(x=105, y=120)
    btn1 = Button(pendataan_pembeli, command = cek_datadiri, text="LANJUTKAN").place(x=120,y=210)

def cek_datadiri():
    del_pendataan_pembeli()
    struk_stringnama = stringnama.get()
    struk_stringnohp = stringnohp.get()
    radio_radio      = radio.get()
    struk_stringalamat = stringalamat.get()

    if len(struk_stringnama) == 0:
        messagebox.showerror("Error","MOHON LENGKAAPI SEMUA DATA")
        shw_pendataan_pembeli()
        return
    if len(struk_stringnohp) == 0:
        messagebox.showerror("Error","MOHON LENGKAAPI SEMUA DATA")
        shw_pendataan_pembeli()
        return
    if len(struk_stringalamat) == 0:
        messagebox.showerror("Error","MOHON LENGKAAPI SEMUA DATA")
        shw_pendataan_pembeli()
        return
    if radio_radio == 0:
        messagebox.showerror("Error","MOHON LENGKAAPI SEMUA DATA")
        shw_pendataan_pembeli()
        return
    if radio_radio == 3:
        messagebox.showerror("Error","MOHON MAAF ANDA BELUM CUKUP UMUR")
        shw_pendataan_pembeli()
        return
    else : 
        pilihpaket()
        del_pilih_paket
        
def pilihpaket():
        global pilih_paket
        pilih_paket = Toplevel(pendataan_pembeli)
        pilih_paket.geometry("480x540")
        pilih_paket.title("PAKET VAPOR")
        pilih_paket.iconbitmap("C:/GUI/vape1.ico")
        Label(pilih_paket, text="SILAHKAN PILIH PAKET VAPOR YANG ANDA INGINKAN", bg="gray", width="300", height="2", font=("Calibri", 11)).pack()
        global radio_paket
        radio_paket = IntVar()

        R1 = Radiobutton(pilih_paket, text="PAKET [1]", variable=radio_paket, value=1).place(x=50, y=50) 
        lb1 = Label(pilih_paket, text = "MOD HexOhm 3.0 Anodized").place(x = 50,y = 80)  
        hr1 = Label(pilih_paket, text = "Rp.2.700.000,00").place(x = 350,y = 80)
        lb2 = Label(pilih_paket, text = "2 X AWT IMR 18650 3000mAh 40A").place(x = 50,y = 100)
        hr1 = Label(pilih_paket, text = "Rp.160.000,00").place(x = 350,y = 100)
        lb3 = Label(pilih_paket, text = "RDA Reload S Authentic").place(x = 50,y = 120)
        hr3 = lb3 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 120)
        lb4 = Label(pilih_paket, text = "Coil inhale Alien V1 0,16 Ohm").place(x = 50,y = 140)
        lb4 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 140)

        R2 = Radiobutton(pilih_paket, text="PAKET [2]", variable=radio_paket, value=2).place(x=50, y=190) 
        lb1 = Label(pilih_paket, text = "MOD Lost Vape Centaurus DNA250C").place(x = 50,y = 220)  
        hr1 = Label(pilih_paket, text = "Rp.1.800.000,00").place(x = 350,y = 220)
        lb2 = Label(pilih_paket, text = "2 X AWT IMR 18650 3000mAh 40A").place(x = 50,y = 240)
        hr1 = Label(pilih_paket, text = "Rp.160.000,00").place(x = 350,y = 240)
        lb3 = Label(pilih_paket, text = "RDA Reload S Authentic").place(x = 50,y = 260)
        hr3 = lb3 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 260)
        lb4 = Label(pilih_paket, text = "Coil inhale Alien V1 0,16 Ohm").place(x = 50,y = 280)
        lb4 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 280)

        R2 = Radiobutton(pilih_paket, text="PAKET [3]", variable=radio_paket, value=3).place(x=50, y=330) 
        lb1 = Label(pilih_paket, text = "MOD Think Vape AUXO DNA250C").place(x = 50,y = 360)  
        hr1 = Label(pilih_paket, text = "Rp.1.500.000,00").place(x = 350,y = 360)
        lb2 = Label(pilih_paket, text = "2 X AWT IMR 18650 3000mAh 40A").place(x = 50,y = 380)
        hr1 = Label(pilih_paket, text = "Rp.160.000,00").place(x = 350,y = 380)
        lb3 = Label(pilih_paket, text = "RDA Reload S Authentic").place(x = 50,y = 400)
        hr3 = lb3 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 400)
        lb4 = Label(pilih_paket, text = "Coil inhale Alien V1 0,16 Ohm").place(x = 50,y = 420)
        lb4 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 420)

        btn2 = Button(pilih_paket, command = struk, text="LANJUTKAN").place(x=350,y=480)

def pilihpaket_darikembali():
        del_strukanda()
        global pilih_paket
        pilih_paket = Toplevel(pendataan_pembeli)
        pilih_paket.geometry("480x540")
        pilih_paket.title("PAKET VAPOR")
        pilih_paket.iconbitmap("C:/GUI/vape1.ico")
        Label(pilih_paket, text="SILAHKAN PILIH PAKET VAPOR YANG ANDA INGINKAN", bg="gray", width="300", height="2", font=("Calibri", 11)).pack()
        global radio_paket
        radio_paket = IntVar()

        R1 = Radiobutton(pilih_paket, text="PAKET [1]", variable=radio_paket, value=1).place(x=50, y=50) 
        lb1 = Label(pilih_paket, text = "MOD HexOhm 3.0 Anodized").place(x = 50,y = 80)  
        hr1 = Label(pilih_paket, text = "Rp.2.700.000,00").place(x = 350,y = 80)
        lb2 = Label(pilih_paket, text = "2 X AWT IMR 18650 3000mAh 40A").place(x = 50,y = 100)
        hr1 = Label(pilih_paket, text = "Rp.160.000,00").place(x = 350,y = 100)
        lb3 = Label(pilih_paket, text = "RDA Reload S Authentic").place(x = 50,y = 120)
        hr3 = lb3 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 120)
        lb4 = Label(pilih_paket, text = "Coil inhale Alien V1 0,16 Ohm").place(x = 50,y = 140)
        lb4 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 140)

        R2 = Radiobutton(pilih_paket, text="PAKET [2]", variable=radio_paket, value=2).place(x=50, y=190) 
        lb1 = Label(pilih_paket, text = "MOD Lost Vape Centaurus DNA250C").place(x = 50,y = 220)  
        hr1 = Label(pilih_paket, text = "Rp.1.800.000,00").place(x = 350,y = 220)
        lb2 = Label(pilih_paket, text = "2 X AWT IMR 18650 3000mAh 40A").place(x = 50,y = 240)
        hr1 = Label(pilih_paket, text = "Rp.160.000,00").place(x = 350,y = 240)
        lb3 = Label(pilih_paket, text = "RDA Reload S Authentic").place(x = 50,y = 260)
        hr3 = lb3 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 260)
        lb4 = Label(pilih_paket, text = "Coil inhale Alien V1 0,16 Ohm").place(x = 50,y = 280)
        lb4 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 280)

        R2 = Radiobutton(pilih_paket, text="PAKET [3]", variable=radio_paket, value=3).place(x=50, y=330) 
        lb1 = Label(pilih_paket, text = "MOD Think Vape AUXO DNA250C").place(x = 50,y = 360)  
        hr1 = Label(pilih_paket, text = "Rp.1.500.000,00").place(x = 350,y = 360)
        lb2 = Label(pilih_paket, text = "2 X AWT IMR 18650 3000mAh 40A").place(x = 50,y = 380)
        hr1 = Label(pilih_paket, text = "Rp.160.000,00").place(x = 350,y = 380)
        lb3 = Label(pilih_paket, text = "RDA Reload S Authentic").place(x = 50,y = 400)
        hr3 = lb3 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 400)
        lb4 = Label(pilih_paket, text = "Coil inhale Alien V1 0,16 Ohm").place(x = 50,y = 420)
        lb4 = Label(pilih_paket, text = "Rp.900.000,00").place(x = 350,y = 420)

        btn2 = Button(pilih_paket, command = struk, text="LANJUTKAN").place(x=350,y=480)


def struk():
    del_pilih_paket()
    struk_stringnama = stringnama.get()
    struk_stringnohp = stringnohp.get()
    radio_radio      = radio.get()
    r_destinasi      = radio_paket.get()
    struk_stringalamat = stringalamat.get()

    if radio_paket.get() == 0:
         messagebox.showerror("Error","BELUM MEMILIH PAKET VAPE")
         shw_pilih_paket()
         return

    else :

        if radio.get() == 1:
             gender ="Pria"
        if radio.get() == 2:
             gender ="Wanita"
        if radio.get() == 3:
             gender ="Anak-Anak"

        if radio_paket.get() == 1:
             des1 ="MOD HexOhm 3.0 Anodized"
             des2 ="Rp.2.700.000,00"
             des3 ="Rp.3.860.000,00"

        if radio_paket.get() == 2:
             des1 ="MOD Lost Vape Centaurus DNA250C"
             des2 ="Rp.1.800.000,00"
             des3 ="Rp.2.960.000,00"

        if radio_paket.get() == 3:
             des1 ="MOD Think Vape AUXO DNA250C"
             des2 ="Rp.1.500.000,00"
             des3 ="Rp.2.660.000,00"


        global strukanda
        strukanda = Toplevel(pilih_paket)
        strukanda.geometry("475x440")
        strukanda.title("STRUK PEMBAYARAN")
        strukanda.iconbitmap("C:/GUI/vape1.ico")
        Label(strukanda, text="STRUK ANDA", bg="gray", width="300", height="2", font=("Calibri", 13)).pack()

        Label(strukanda, text="DATA DIRI PEMESAN", bg="gray", font=("Calibri", 10)).place(x=30,y=60)
        Label(strukanda, text="Nama      :  " + struk_stringnama).place(x=30,y=90)
        Label(strukanda, text="Gender    :  " + gender).place(x=30,y=110)
        Label(strukanda, text="No.HP     :  " + struk_stringnohp).place(x=30,y=130)
        Label(strukanda, text="Alamat    :  " + struk_stringalamat).place(x=30,y=150)

        Label(strukanda, text="PEMBELIAN VAPE", bg="gray", font=("Calibri", 10)).place(x=30,y=200)
        Label(strukanda, text=des1).place(x=30,y=230)
        Label(strukanda, text=des2).place(x=350,y=230)
        Label(strukanda, text = "2 X AWT IMR 18650 3000mAh 40A").place(x = 30,y = 250)
        Label(strukanda, text = "Rp.160.000,00").place(x = 350,y = 250)
        Label(strukanda, text = "RDA Reload S Authentic").place(x = 30,y = 270)
        Label(strukanda, text = "Rp.900.000,00").place(x = 350,y = 270)
        Label(strukanda, text = "Coil inhale Alien V1 0,16 Ohm").place(x = 30,y = 290)
        Label(strukanda, text = "Rp.900.000,00").place(x = 350,y = 290)

        Label(strukanda, text="                                                                                                              ", bg="gray", font=("Calibri", 10)).place(x=30,y=340)
        Label(strukanda, text="TOTAL BIAYA    ", bg="gray", font=("Calibri", 10)).place(x=30,y=340)
        Label(strukanda, text=des3, bg="gray", font=("Calibri", 10)).place(x=350,y=340)

        btn = Button(strukanda, command = pilihpaket_darikembali, text="KEMBALI").place(x=30,y=390)
        btn = Button(strukanda, command = countdown, text="PESAN").place(x=350,y=390)


def countdown():
       del_strukanda()
       get_class = count_down.HM()


def del_main_screen():
    main_screen.withdraw()

def shw_main_screen():
    main_screen.deiconify()
    login_screen.withdraw()

def del_register_screen():
    register_screen.withdraw()

def del_login_screen():
    login_screen.withdraw()
 
def delete_login_success():
    login_success_screen.destroy()

def del_pendataan_pembeli():
    pendataan_pembeli.withdraw()

def shw_pendataan_pembeli():
    pendataan_pembeli.deiconify()

def del_pilih_paket():
    pilih_paket.withdraw()

def shw_pilih_paket():
    pilih_paket.deiconify()


def del_strukanda():
    strukanda.destroy()

def del_menu_utama():
    menu_utama.destroy()

main_account_screen()