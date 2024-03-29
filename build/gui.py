from pathlib import Path
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\python project for learning\calculator\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("376x565")

window.configure(bg = "#404040")
window.title("calculator")

window.config(bg="red")

canvas = Canvas(
    window,
    bg = "#404040",
    height = 565,
    width = 376,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    181.5,
    85.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font="tahoma 22  bold "
)
entry_1.place(
    x=42.0,
    y=57.0,
    width=279.0,
    height=55.0
)

canvas.create_text(
    103.0,
    8.0,
    anchor="nw",
    text="technotaz calculator",
    fill="#FFFFFF",
    font=("Koulen Regular", 20 * -1)
)

def adad7():
    entry_1.insert(INSERT, "7")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=adad7,
    relief="flat"
)
button_1.place(
    x=42.0,
    y=165.0,
    width=77.0,
    height=72.0
)
def adad8():
    entry_1.insert(INSERT, "8")


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=adad8,
    relief="flat"
)
button_2.place(
    x=143.0,
    y=162.0,
    width=77.0,
    height=75.0
)
def adad9():
    entry_1.insert(INSERT, "9")

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=adad9,
    relief="flat"
)
button_3.place(
    x=244.0,
    y=167.0,
    width=77.0,
    height=70.0
)
def adad4():
    entry_1.insert(INSERT, "4")


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=adad4,
    relief="flat"
)
button_4.place(
    x=42.0,
    y=265.0,
    width=77.0,
    height=73.0
)
def adad5():
    entry_1.insert(INSERT, "5")



button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=adad5,
    relief="flat"
)
button_5.place(
    x=143.0,
    y=268.0,
    width=77.0,
    height=70.0
)
def adad6():
    entry_1.insert(INSERT, "6")

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=adad6,
    relief="flat"
)
button_6.place(
    x=249.0,
    y=267.0,
    width=77.0,
    height=71.0
)
def adad1():
    entry_1.insert(INSERT, "1")

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=adad1,
    relief="flat"
)
button_7.place(
    x=42.0,
    y=365.0,
    width=77.0,
    height=74.0
)
def adad2():
    entry_1.insert(INSERT, "2")


button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=adad2,
    relief="flat"
)
button_8.place(
    x=143.0,
    y=369.0,
    width=77.0,
    height=70.0
)
def adad3():
    entry_1.insert(INSERT, "3")


button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=adad3,
    relief="flat"
)
button_9.place(
    x=249.0,
    y=369.0,
    width=77.0,
    height=70.0
)
def zarb():
    entry_1.insert(INSERT, "x")

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=zarb,
    relief="flat"
)
button_10.place(
    x=36.0,
    y=479.0,
    width=46.0,
    height=45.0
)
def plus():
    entry_1.insert(INSERT, "+")

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=plus,
    relief="flat"
)
button_11.place(
    x=101.0,
    y=479.0,
    width=42.0,
    height=45.0
)
def menha():
    entry_1.insert(INSERT, "-")

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=menha,
    relief="flat"
)
button_12.place(
    x=162.0,
    y=479.0,
    width=43.0,
    height=45.0
)
def taghsim():
    entry_1.insert(INSERT, "%")

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=taghsim,
    relief="flat"
)
button_13.place(
    x=228.0,
    y=479.0,
    width=42.0,
    height=45.0
)
def mosavi():
    formol = entry_1.get()
    if "+" in formol:
        varlist = formol.split("+")
        befor = varlist[0]
        after = varlist[1]
        result = int(befor) + int(after)
        entry_1.insert(INSERT, f" = {result}")
    elif "x" in formol:
        varlist = formol.split("x")
        befor = varlist[0]
        after = varlist[1]
        result = int(befor) * int(after)
        entry_1.insert(INSERT, f" = {result}")
    elif "%" in formol:
        varlist = formol.split("%")
        befor = varlist[0]
        after = varlist[1]
        result = int(befor) / int(after)
        entry_1.insert(INSERT, f" = {result}")
    elif "-" in formol:
        varlist = formol.split("-")
        befor = varlist[0]
        after = varlist[1]
        result = int(befor) - int(after)
        entry_1.insert(INSERT, f" = {result}")

    else:
        entry_1.insert(INSERT, "nist")


button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=mosavi,
    relief="flat"
)
button_14.place(
    x=282.0,
    y=479.0,
    width=44.0,
    height=45.0
)
window.resizable(False, False)
window.mainloop()
