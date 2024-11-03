import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%d %B %Y %H:%M:%S %p")
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("600x100")

# Create the time label
time_label = tk.Label(window, font=("Arial", 24), bg="black", fg="white")
time_label.pack(pady=20)

# Start the clock
update_time()

# Run the main loop
window.mainloop()