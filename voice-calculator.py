import tkinter as tk
import winsound

# Ses dosyasını çalmak için winsound modülünü kullanıyoruz
def play_sound(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_FILENAME)

# Sayı tuşlarına tıklandığında, girilen sayıyı ekler
def button_click(number):
    current_expression = entry.get()
    new_expression = current_expression + str(number)
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_expression)
    play_sound("ses.wav") 

# İşlem yap tuşuna tıklandığında, girilen ifadeyi hesaplar ve sonucu gösterir
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        play_sound("ses_2.wav")  
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Hata!")
        play_sound("ses_4.wav")  

# Temizleme tuşuna tıklandığında, girilen ifadeyi temizler
def clear():
    entry.delete(0, tk.END)
    play_sound("ses_3.wav")  

# Pencere oluşturuluyor
window = tk.Tk()
window.title("Hesap Makinesi")

# Simgeyi ekliyoruz
window.iconbitmap("calculator.ico") 

# Giriş alanını oluşturuyoruz
entry = tk.Entry(window, width=25, font=("Arial", 14))  
entry.grid(row=0, column=0, columnspan=4, pady=10)  

# Tuşları oluşturuyoruz
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
row = 1
column = 0
for button_text in buttons:
    if button_text == "=":
        button = tk.Button(window, text=button_text, width=5, font=("Arial", 12), command=calculate)
        # Eşittir tuşunun fontunu ve boyutunu ayarlayın
    else:
        button = tk.Button(window, text=button_text, width=5, font=("Arial", 12), command=lambda text=button_text: button_click(text))
        # Diğer tuşların fontunu ve boyutunu ayarlayın
    button.grid(row=row, column=column, padx=5, pady=5)
    # İçerideki boşluğu ayarlayın
    column += 1
    if column > 3:
        column = 0
        row += 1

clear_button = tk.Button(window, text="C", width=5, font=("Arial", 12), command=clear)
# Temizleme tuşunun fontunu ve boyutunu ayarlayın
clear_button.grid(row=row, column=column, padx=5, pady=5)
# İçerideki boşluğu ayarlayın

# Ses dosyasını çal
play_sound("ses_5.wav")  

window.mainloop()
