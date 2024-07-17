from tkinter import *
from tkinter import messagebox

# Initialize the main window
root = Tk()
root.geometry('400x400')
root.title("Temperature Converter")
root.configure(bg='#2e3f4f')

# String variables to hold the input and output temperature values
textin1 = StringVar()
textin2 = StringVar()

# Input fields for temperatures
text1 = Entry(root, font=("Helvetica", 18), textvar=textin1, width=10, bd=2, bg='#ffffff', fg='#2e3f4f', relief=GROOVE)
text1.place(x=200, y=100, anchor=CENTER)

text2 = Entry(root, font=("Helvetica", 18), textvar=textin2, width=10, bd=2, bg='#ffffff', fg='#2e3f4f', relief=GROOVE)
text2.place(x=200, y=160, anchor=CENTER)

# Conversion functions
def celsius_to_fahrenheit():
    temp = textin1.get()
    try:
        temp = float(temp)
        result = str((temp * 9/5) + 32)
        textin2.set(result)
    except ValueError:
        messagebox.showerror("ERROR", "Please Enter Temperature In Digits")

def fahrenheit_to_celsius():
    temp = textin1.get()
    try:
        temp = float(temp)
        result = str((temp - 32) * 5/9)
        textin2.set(result)
    except ValueError:
        messagebox.showerror("ERROR", "Please Enter Temperature In Digits")

def clear_fields():
    textin1.set("")
    textin2.set("")

# UI Labels and Buttons
label1 = Label(root, text='Temperature Converter', font=("Helvetica", 22, 'bold'), bg='#2e3f4f', fg='#f0f0f0')
label1.pack(pady=20)

def display_celsius_to_fahrenheit():
    label2 = Label(root, text='Celsius (°C)', font=("Helvetica", 14), bg='#2e3f4f', fg='#f0f0f0')
    label2.place(x=200, y=70, anchor=CENTER)

    label3 = Label(root, text='Fahrenheit (°F)', font=("Helvetica", 14), bg='#2e3f4f', fg='#f0f0f0')
    label3.place(x=200, y=130, anchor=CENTER)

    convert_button = Button(root, text="Convert", padx=20, pady=5, bd=0, command=celsius_to_fahrenheit, font=("Helvetica", 14, 'bold'), bg='#f0a500', fg='#2e3f4f', relief=FLAT)
    convert_button.place(x=200, y=220, anchor=CENTER)

    clear_button = Button(root, text="Clear", padx=20, pady=5, bd=0, command=clear_fields, font=("Helvetica", 14, 'bold'), bg='#f0a500', fg='#2e3f4f', relief=FLAT)
    clear_button.place(x=200, y=270, anchor=CENTER)

    toggle_button = Button(root, text='Switch to °F to °C', font=("Helvetica", 12, 'bold'), command=display_fahrenheit_to_celsius, bg='#f0a500', fg='#2e3f4f', relief=FLAT)
    toggle_button.place(x=200, y=320, anchor=CENTER)

def display_fahrenheit_to_celsius():
    label2 = Label(root, text='Fahrenheit (°F)', font=("Helvetica", 14), bg='#2e3f4f', fg='#f0f0f0')
    label2.place(x=200, y=70, anchor=CENTER)

    label3 = Label(root, text='Celsius (°C)', font=("Helvetica", 14), bg='#2e3f4f', fg='#f0f0f0')
    label3.place(x=200, y=130, anchor=CENTER)

    convert_button = Button(root, text="Convert", padx=20, pady=5, bd=0, command=fahrenheit_to_celsius, font=("Helvetica", 14, 'bold'), bg='#f0a500', fg='#2e3f4f', relief=FLAT)
    convert_button.place(x=200, y=220, anchor=CENTER)

    clear_button = Button(root, text="Clear", padx=20, pady=5, bd=0, command=clear_fields, font=("Helvetica", 14, 'bold'), bg='#f0a500', fg='#2e3f4f', relief=FLAT)
    clear_button.place(x=200, y=270, anchor=CENTER)

    toggle_button = Button(root, text='Switch to °C to °F', font=("Helvetica", 12, 'bold'), command=display_celsius_to_fahrenheit, bg='#f0a500', fg='#2e3f4f', relief=FLAT)
    toggle_button.place(x=200, y=320, anchor=CENTER)

# Display the initial conversion mode
display_celsius_to_fahrenheit()

# Run the main loop
root.mainloop()
