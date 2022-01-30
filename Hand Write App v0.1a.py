import pywhatkit
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from locate import this_dir
import pyglet

dir_ = str(this_dir())
pyglet.font.add_file(dir_ + "\\Jenine-Regular.otf")


def save_image():
    #image_name = image_name.get()
    text_ = text.get("1.0","end")
    loc = filedialog.asksaveasfilename(filetypes=(
                    ("Png", "*.png"),
                    ("Jpg", "*.jpg"),
                    ("All files", "*.*"),
                ))
    try:
        pywhatkit.text_to_handwriting(text_,save_to=loc)
        messagebox.showinfo("Done!","تم الحفظ")
    except:
        messagebox.showerror("Error 0", "غير قادر على الاتصال!")

window = Tk()
window.configure(bg="darkgrey")
window.title('Hand Writing App V:0.1a | Sub:(EN) | By "Wesam Almasruri"')
window.geometry("500x400")
window.resizable(False,False)
window.iconbitmap(dir_ + "\\icon.ico")
title = Label(window,text="تطبيق الكتابة اليدوية",font=("Jenine",26),fg="white",bg="darkgrey")
title.pack(pady=10)

text = Text(window,font="arial",height=14)
text.pack(padx=2)

save_button = Button(window,text="حفظ الصورة",width=10,height=2,command=save_image,font=("Jenine",14))
save_button.pack(pady=11)





if __name__ == "__main__":
    window.mainloop()
