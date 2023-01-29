import tkinter as tk

import customtkinter as Ctk

Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("blue")

title_font = ("Arial", 20, "bold")
text_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

heading_text = "Grade Calculator"
subheading_text = "Made by Spencer Boggs"

root = Ctk.CTk()
root.geometry("500x500")
root.title("Grade Calculator")


def start():
    print("Hello")


frame = Ctk.CTkFrame(master=root)
frame.pack(pady=40, padx=40, fill="both", expand=True)

# Title/Heading
label = Ctk.CTkLabel(master=frame, text=heading_text, font=title_font)
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
label.pack(pady=10, padx=10)

# Subheading
label = Ctk.CTkLabel(master=frame, text=subheading_text, font=text_font)
label.pack(pady=0, padx=10)

entry1 = Ctk.CTkEntry(
    master=frame, placeholder_text="Current grade:", font=text_font)
entry1.pack(pady=20, padx=10)

button = Ctk.CTkButton(master=frame, text="Start",
                       font=button_font, command=start)
button.pack(pady=20, padx=10)

#checkbox = tk.CTkCheckBox(master=frame, text="Check me")
#checkbox.pack(pady=20, padx=10)

root.mainloop()
