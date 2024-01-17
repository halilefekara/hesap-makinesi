import tkinter as tk
import math

def button_click(num):
    label["text"]="{}{}".format( label["text"] , num)
def button_clear_click():
    label["text"]=""
def button_equal_click():
    sonuc = eval(label["text"])
    label["text"]=sonuc
def button_delete_click():
    label["text"] = str(label["text"])[:-1]
def button_square_root_click():
    sayi = math.sqrt(int(label["text"]))
    label["text"]=sayi
def button_absolute_value_click():
    if label["text"][0] == ("-"):
        label["text"] = (label["text"])[1:]
    else:
        pass



    



root = tk.Tk()
root.title("B.Bilsem")
root.configure(bg="#a2a2a2")

# pencere genişliği ve yüksekliği
ekran_genislik = root.winfo_screenwidth()
ekran_yukseklik = root.winfo_screenheight()
pencere_genislik = 275
pencere_yukseklik = 325

# pencereyi ekranın ortasına yerleştir
x = (ekran_genislik - pencere_genislik) // 2
y = (ekran_yukseklik - pencere_yukseklik) // 2


root.geometry("{}x{}+{}+{}".format(pencere_genislik, pencere_yukseklik, x, y))


label = tk.Label(root, text="",bg="white", height=2,width=33)
label.place(x=20,y=20)

one = tk.Button(root, text="1", command=lambda: button_click(1), width=4, height=2,bg="gray")
one.place(x=20, y=70)

two = tk.Button(root,text="2",command=lambda: button_click(2),width=4, height=2,bg="gray")
two.place(x=70,y=70)

three = tk.Button(root,text="3",command=lambda: button_click(3),width=4,height=2,bg="gray")
three.place(x=120,y=70)

zero = tk.Button(root,text="0",command=lambda: button_click(0),width=4,height=2,bg="gray")
zero.place(x=170,y=70)

delete = tk.Button(root,text="sil",command=lambda: button_delete_click(),width=4,height=2,bg="gray")
delete.place(x=220,y=70)

four = tk.Button(root,text="4",command=lambda: button_click(4),width=4,height=2,bg="gray")
four.place(x=20,y=120)

five = tk.Button(root,text="5",command=lambda: button_click(5),width=4,height=2,bg="gray")
five.place(x=70,y=120)


six = tk.Button(root,text="6",command=lambda: button_click(6),width=4,height=2,bg="gray")
six.place(x=120,y=120)

plus = tk.Button(root,text="+",command=lambda: button_click("+"),width=4,height=2,bg="gray")
plus.place(x=170,y=120)

impact = tk.Button(root,text="*",command=lambda: button_click("*"),width=4,height=2,bg="gray")
impact.place(x=220,y=120)

seven = tk.Button(root,text="7",command=lambda: button_click(7),width=4,height=2,bg="gray")
seven.place(x=20,y=170)

eight = tk.Button(root,text="8",command=lambda: button_click(8),width=4,height=2,bg="gray")
eight.place(x=70,y=170)


nine = tk.Button(root,text="9",command=lambda: button_click(9),width=4,height=2,bg="gray")
nine.place(x=120,y=170)


extraction = tk.Button(root,text="-",command=lambda: button_click("-"),width=4,height=2,bg="gray")
extraction.place(x=170,y=170)


divide = tk.Button(root,text="/",command=lambda: button_click("/"),width=4,height=2,bg="gray")
divide.place(x=220,y=170)

brackets1 = tk.Button(root,text="(",command=lambda: button_click("("),width=4,height=2,bg="gray")
brackets1.place(x=20,y=220)

brackets2 = tk.Button(root,text=")",command=lambda: button_click(")"),width=4,height=2,bg="gray")
brackets2.place(x=70,y=220)

square_root = tk.Button(root,text="karekök",command=lambda: button_square_root_click(),width=11,height=2,bg="gray")
square_root.place(x=120,y=220)

absolute_value = tk.Button(root,text="|",command=lambda: button_absolute_value_click(),width=4,height=2,bg="gray")
absolute_value.place(x=220,y=220)

coefficient = tk.Button(root,text="katsayı",command=lambda:button_click("**"),width=11,height=2,bg="gray")
coefficient.place(x=120,y=270)

clear = tk.Button(root,text="tamamen sil",command=lambda: button_clear_click(),width=11,height=2,bg="gray")
clear.place(x=20,y=270)

equal = tk.Button(root,text="=",command=lambda: button_equal_click(),width=4,height=2,bg="gray")
equal.place(x=220,y=270)



# Butonu 2. satır, 3. sütuna konumlandır



root.mainloop()