import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os

class MyButton(tk.Button):
    def __init__(self, master=None, image_path=None, bac="#0D1117", **kwargs):
        super().__init__(master, **kwargs)
        image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(image)
        self.configure(
            font=("Times New Roman", 45),
            bg=bac,
            fg='#0D1117',
            border=0,
            highlightthickness=0,
            image=self.photo,
            activebackground=bac
        )
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
        self.bind("<ButtonRelease-1>", self.on_release)

    def on_hover(self, event):
        self.configure(cursor="hand2")

    def on_leave(self, event):
        self.configure(cursor="")
        
    def on_click(self, event):
        self.configure(bg='#0D1117', fg='#0D1117')
        
    def on_release(self, event):
        self.configure(bg='#0D1117', fg='#0D1117')

def display(A):
    output_text = ""
    for B in range(30):
        for C in range(30):
            D = B * 30 + C
            output_text += chr(A[D]) + " "
        output_text += "\n"
    output_text += "\n"
    return output_text

def shape(A, B, C):
    B = B - 93
    if (A[2] == "0"):
        J = 78
    else:
        J = 86
    for D in range(7):
        for E in range(7):
            F = D * 30 + E
            G = D * 7 + E
            H = F + B
            if (A[G] == "0"):
                C[H] = 126
            else:
                C[H] = J
    return C

def navigate(A, inp):
    B = False
    while not B:
        B = False
        D = A
        C = inp
        if (C == "N" and A >= 30):
            A = A - 30
        elif (C == "S" and A <= 870):
            A = A + 30
        elif (C == "E" and A % 30 != 29):
            A = A + 1
        elif (C == "W" and A % 30 != 0):
            A = A - 1
        else:
            tk.messagebox.showerror("Error","Cannot go there")
            break
        B = border(A)
    return A

def border(A):
    B = False
    for C in range(24):
        for D in range(24):
            E = C * 30 + D + 93
            if (A == E):
                B = True
    return B

def metric(A, B):
    for C in range(24):
        for D in range(24):
            E = C * 30 + D + 93
            if (E == A):
                F = D
                G = C
            if (E == B):
                H = D
                J = C
    K = ((F - H) ** 2 + (G - J) ** 2)
    return K

def clear(A):
    for B in range(900):
        A[B] = 126
    return A

def display_output(output):
    start_button.place_forget()
    exit_button.place_forget()
    
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)
    output_text.config(state=tk.DISABLED)

def up_clicked():
    global LOCATION
    LOCATION = navigate(LOCATION, "N")
    update_ship_location(LOCATION)
    if LOCATION == 405:
        tk.messagebox.showinfo("Congratulations","Welcome Home Captain Nemo")

def down_clicked():
    global LOCATION
    LOCATION = navigate(LOCATION, "S")
    update_ship_location(LOCATION)
    if LOCATION == 405:
        tk.messagebox.showinfo("Congratulations","Welcome Home Captain Nemo")

def right_clicked():
    global LOCATION
    LOCATION = navigate(LOCATION, "E")
    update_ship_location(LOCATION)
    if LOCATION == 405:
        tk.messagebox.showinfo("Congratulations","Welcome Home Captain Nemo")

def left_clicked():
    global LOCATION
    LOCATION = navigate(LOCATION, "W")
    update_ship_location(LOCATION)
    if LOCATION == 405:
        tk.messagebox.showinfo("Congratulations","Welcome Home Captain Nemo")

def update_ship_location(location):
    OCEAN = clear([126] * 900)
    OCEAN = shape(NAUT, location, OCEAN)
    OCEAN = shape(VULC, 405, OCEAN)
    output = display(OCEAN)
    display_output(output)

def main():
    global LOCATION,VULC,NAUT
    LOCATION = 248
    
    OCEAN = [126] * 900
    NAUT = "00000000000000"
    NAUT = NAUT + "00010000111110"
    NAUT = NAUT + "11111110111110"
    NAUT = NAUT + "0000000"
    VULC = "00101000010100"
    VULC = VULC + "01111101111111"
    VULC = VULC + "11111111111111"
    VULC = VULC + "0000000"

    OCEAN = shape(NAUT, 248, OCEAN)
    OCEAN = shape(VULC, 405, OCEAN)
    display(OCEAN)
    output = display(OCEAN)
    display_output(output)
         
def start_game():
    start_button.place_forget()
    exit_button.place_forget()
    output_frame.place(x=600, y=100, width=700, height=600)
    output_text.pack(fill=tk.BOTH, expand=True)
    output_text.config(state=tk.DISABLED)
    label.place(x=520, y=515)
    up.place(x=750, y=515)
    down.place(x=750, y=540)
    left.place(x=710, y=528)
    right.place(x=790, y=528)
    main()

data_dir = os.getcwd()

app = ctk.CTk()
app.title("Captain Nemo")
app.iconbitmap(os.path.join(data_dir, 'nemo.ico'))
app.geometry("1000x570")
app.resizable(0, 0)
app.pack_propagate(False)

background_image = tk.PhotoImage(file=os.path.join(data_dir, 'template.png'))
background_label = tk.Label(app, image=background_image)
background_label.pack()

output_frame = tk.Frame(app, bg="#000000")  # Set background color to black

output_text = tk.Text(output_frame, wrap=tk.WORD, bg="#000000", fg="white", font=("Courier", 12))  # Set text color to white

start_button = MyButton(app, image_path=os.path.join(data_dir, 'start.png'), bac='#000000', fg='white', command=start_game)  # Set text color to white
start_button.place(x=840, y=300)

exit_button = MyButton(app, image_path=os.path.join(data_dir, 'exit.png'), bac='#000000', fg='white', command=app.destroy)  # Set text color to white
exit_button.place(x=850, y=500)

up = ctk.CTkButton(app,  text="N", fg_color='#FFFFFF', text_color='black', height=10, width=30, command=up_clicked)


down = ctk.CTkButton(app, text="S", fg_color='#FFFFFF', text_color='black', height=10, width=30, command=down_clicked)


left = ctk.CTkButton(app, text="W", fg_color='#FFFFFF', text_color='black', height=10, width=30, command=left_clicked)


right = ctk.CTkButton(app, text="E", fg_color='#FFFFFF', text_color='black', height=10, width=30, command=right_clicked)


label = ctk.CTkLabel(app, text="Hi there, Captain Nemo.\nDo you want to navigate\nNorth, South, East or West?", bg_color='#FFFFFF', text_color="black")

app.mainloop()
