import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def yeni_dosya():
    text.delete(1.0, tk.END)
    root.title("Yeni Dosya - Not Defteri")

def dosya_ac():
    dosya = filedialog.askopenfilename(defaultextension=".txt",
                                       filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
    if dosya:
        with open(dosya, "w", encoding="utf-8") as f:
            f.write(text.get(1.0, tk.END))
        root.title(f"{dosya} - Not Defteri")

def dosya_kaydet():
    dosya = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Metin Dosyaları", ".txt"), ("Tüm Dosyalar", "*.*")])
    if dosya:
        with open(dosya, "w", encoding="utf-8") as f:
            f.write(text.get(1.0 , tk.END))
        root.title(f"{dosya} - Not Defteri")

def cikis():
    if messagebox.askokcancel("Çıkış", "Gerçekten çıkmak istiyor musun?"):
        root.destroy()

root = tk.Tk()
root.title("Not Defteri")
root.geometry("600x400")

menu = tk.Menu(root)
root.config(menu=menu)

dosya_menu = tk.Menu(menu,tearoff=0)
menu.add_cascade(label="Dosya", menu=dosya_menu)
dosya_menu.add_command(label="Yeni", command=yeni_dosya)
dosya_menu.add_command(label="Aç", command=dosya_ac)
dosya_menu.add_command(label="Kaydet", command=dosya_kaydet)
dosya_menu.add_separator()
dosya_menu.add_command(label="Çıkış", command=cikis )

text = tk.Text(root, font=("Consolas", 12))
text.pack(fill=tk.BOTH, expand=True)

root.mainloop()