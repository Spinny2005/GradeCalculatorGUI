import tkinter as tk

import customtkinter as Ctk

Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("blue")

title_font = ("Arial", 30, "bold")
text_font = ("Arial", 18)
button_font = ("Arial", 18, "bold")

heading_text = "Grade Calculator"
subheading_text = "Made by Spencer Boggs"

root = Ctk.CTk()
root.geometry("500x500")
root.title("Grade Calculator")


def start():
    current = entry1.get()
    final = entry2.get()
    gradeOnFinal = entry3.get()
    desired = entry4.get()
    if (gradeOnFinal == "" and desired == ""):
        return "Please fill in all fields"
    else:
        if (current != "" and final != ""):
            try: 
                if (current.endswith('%')):
                    current = current.rstrip(current[-1])
                current = float(current)
            except ValueError: current = None

            try: 
                if (final.endswith('%')):
                    final = final.rstrip(final[-1])
                final = float(final)
            except ValueError: final = None
    
            if (final != None) and (current != None):
                if (str(final) != "0"):
                    final = float(final)
                    if (desired != ""):
                        try: 
                            if (desired.endswith('%')):
                                desired = desired.rstrip(desired[-1])
                            desired = float(desired)
                        except ValueError: desired = None
                        if (desired != None):
                            desired = float(desired)

                            currentWithFinal = current * ((100 - final) / 100)
                            needed = (desired - currentWithFinal) / (final / 100)
                            resultsLabel.configure(text="You need a " + str(needed) + "% on the final exam")
                    else:
                        try: 
                            if (gradeOnFinal.endswith('%')):
                                gradeOnFinal = gradeOnFinal.rstrip(gradeOnFinal[-1])
                            gradeOnFinal = float(gradeOnFinal)
                        except ValueError: gradeOnFinal = None
                        if (gradeOnFinal != None):
                            gradeOnFinal = str(gradeOnFinal)
                            if (gradeOnFinal.endswith('%')):
                                gradeOnFinal = gradeOnFinal.rstrip(gradeOnFinal[-1])
                                gradeOnFinal = float(gradeOnFinal)
                            elif ("/" in gradeOnFinal):
                                gradeOnFinal = eval(gradeOnFinal)
                                gradeOnFinal = float(gradeOnFinal) * 100
                            else:
                                gradeOnFinal = float(gradeOnFinal)

                            currentWithFinal = current * ((100 - final) / 100)
                            finalGrade = currentWithFinal + (gradeOnFinal * (final / 100))
                            
                            resultsLabel.configure(text="Your final grade will be " + str(finalGrade) + "%")



frame = Ctk.CTkFrame(master=root)
frame.pack(pady=40, padx=40, fill="both", expand=True)

label = Ctk.CTkLabel(master=frame, text=heading_text, font=title_font)
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
label.pack(pady=10, padx=30)

label = Ctk.CTkLabel(master=frame, text=subheading_text, font=text_font)
label.pack(pady=0, padx=30)

label = Ctk.CTkLabel(master=frame, text="Current Grade:", font=text_font)
label.pack(pady=0, padx=30)
entry1 = Ctk.CTkEntry(
    master=frame, font=text_font)
entry1.pack(pady=10, padx=30)

label = Ctk.CTkLabel(master=frame, text="Final Exam %", font=text_font)
label.pack(pady=0, padx=30)

entry2 = Ctk.CTkEntry(
    master=frame, font=text_font)
entry2.pack(pady=10, padx=30)

label = Ctk.CTkLabel(master=frame, text="Grade On Final:", font=text_font)
label.pack(pady=0, padx=30)

entry3 = Ctk.CTkEntry(
    master=frame, font=text_font)
entry3.pack(pady=10, padx=30)

label = Ctk.CTkLabel(master=frame, text="or", font=text_font)
label.pack(pady=2, padx=30)

label = Ctk.CTkLabel(master=frame, text="Desired Grade:", font=text_font)
label.pack(pady=0, padx=30)

entry4 = Ctk.CTkEntry(
    master=frame, font=text_font)
entry4.pack(pady=10, padx=30)

button = Ctk.CTkButton(master=frame, text="Start",
                       font=button_font, command=start)
button.pack(pady=10, padx=30)

resultsLabel = Ctk.CTkLabel(master=frame , text="", font=text_font)
resultsLabel.pack(pady=10, padx=30)

root.mainloop()
