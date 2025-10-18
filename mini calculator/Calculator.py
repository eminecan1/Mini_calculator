import tkinter as tk
from tkinter import font

# Global değişken: Ekranda gösterilen ifadeyi tutar
ifade = ""

def tus_bas(deger):
    """
    Tıklanan düğmelerin değerlerini ifadeye ekler ve ekranı günceller.
    """
    global ifade
    ifade += str(deger)
    ekran_degeri.set(ifade)

def hesapla():
    """
    İfadeyi değerlendirir ve sonucu ekranda gösterir.
    Hata oluşursa 'Hata' gösterir.
    """
    global ifade
    try:
        sonuc = str(eval(ifade))
        ekran_degeri.set(sonuc)
        ifade = sonuc
    except Exception:
        ekran_degeri.set("Hata")
        ifade = ""

def temizle():
    """
    Ekranı ve ifadeyi temizler.
    """
    global ifade
    ifade = ""
    ekran_degeri.set("")

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Calculator")
pencere.geometry("320x450")
pencere.resizable(0, 0)
pencere.configure(bg="#2C003E") # Koyu mor arkaplan

# Özel fontları tanımla
font_ekran = font.Font(family='Helvetica', size=28, weight='bold')
font_dugme = font.Font(family='Helvetica', size=18)
font_islem = font.Font(family='Helvetica', size=18, weight='bold')

# Ekranda gösterilecek değeri tutan değişken
ekran_degeri = tk.StringVar()
ekran_degeri.set("") # Başlangıçta boş ekran

# Giriş alanı (Ekran)
ekran = tk.Entry(pencere, textvariable=ekran_degeri, font=font_ekran, bd=0, 
                 insertwidth=0, width=15, justify='right', bg="#4A0072", 
                 fg="white", cursor="arrow", relief='flat', highlightthickness=2, 
                 highlightbackground="#8A2BE2") # Daha belirgin mor çerçeve
ekran.grid(row=0, column=0, columnspan=4, padx=15, pady=20, sticky="nsew")

# Renk paleti (Pembe tonları ile güncellendi)
MOR_KOYU = "#4A0072"
MOR_ORTA = "#8A2BE2"
MOR_ACIK = "#B388FF"
MOR_BUTTON = "#6A1B9A"
PEMBE_VURGU = "#FF69B4" # Canlı pembe vurgu rengi
PEMBE_ACIK = "#FFB6C1" # Basıldığında daha açık pembe

# Düğme oluşturma fonksiyonu
def dugme_olustur(metin, satir, sutun, genislik=1, yukseklik=1, bg_renk=MOR_BUTTON, fg_renk="white", font_tipi=font_dugme):
    if metin == '=':
        komut = hesapla
        bg_renk = PEMBE_VURGU # Eşittir düğmesi için pembe
        fg_renk = "#2C003E" # Eşittir düğmesi yazısı için koyu renk
        font_tipi = font_islem
    elif metin == 'C':
        komut = temizle
        bg_renk = MOR_ORTA # Temizle düğmesi için orta mor
        font_tipi = font_islem
    elif metin in ['/', '*', '-', '+']:
        komut = lambda t=metin: tus_bas(t)
        bg_renk = PEMBE_VURGU # Operatörler için pembe vurgu
        fg_renk = "#2C003E" # Operatör yazısı için koyu renk
        font_tipi = font_islem
    else:
        komut = lambda t=metin: tus_bas(t)

    btn = tk.Button(pencere, text=metin, padx=10, pady=10, font=font_tipi,
                    command=komut, bg=bg_renk, fg=fg_renk,
                    activebackground=MOR_ACIK if metin not in ['=', '/', '*', '-', '+'] else PEMBE_ACIK, 
                    activeforeground="#2C003E", # Düğmeye basıldığında yazı rengi
                    relief=tk.FLAT, bd=0, highlightthickness=0,
                    cursor="hand2") # Mouse imleci el şekline dönüşür
    
    btn.grid(row=satir, column=sutun, columnspan=genislik, rowspan=yukseklik, 
             padx=7, pady=7, sticky="nsew")
    return btn

# Düğme düzeni (Metin, Satır, Sütun, Genişlik)
dugme_duzeni = [
    ('C', 1, 0, 2), ('/', 1, 3, 1),
    ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('*', 2, 3, 1),
    ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('-', 3, 3, 1),
    ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('+', 4, 3, 1),
    ('0', 5, 0, 2), ('.', 5, 2, 1), ('=', 5, 3, 1)
]

# Düğmeleri oluştur ve yerleştir
for (metin, satir, sutun, genislik) in dugme_duzeni:
    dugme_olustur(metin, satir, sutun, genislik)

# Sütunları ve satırları eşit genişlik/yüksekliğe yap
for i in range(4): # 4 sütun (0'dan 3'e)
    pencere.grid_columnconfigure(i, weight=1)
for i in range(1, 6): # 5 satır (1'den 5'e, 0. satır ekran için)
    pencere.grid_rowconfigure(i, weight=1)

# Ana döngüyü başlat
pencere.mainloop()