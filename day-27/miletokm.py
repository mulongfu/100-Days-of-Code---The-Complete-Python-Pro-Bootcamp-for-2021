from tkinter import *

def mile_to_km():
    miles = float(mile.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")

# Creating a new window and configurations
window = Tk()
window.title("Mile to km converter")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

mile = Entry(width=7)
mile.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)
calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
