import tkinter as tk
from datetime import datetime, timedelta
import time

# Date
target_year = 2024
target_month = 3
target_day = 4
target_hour = 0
target_minutes = 0

def calculate_time_until_date():
    target_date = datetime(target_year, target_month, target_day, target_hour, target_minutes)
    current_time = datetime.now()

    time_difference = target_date - current_time

    months, days = divmod(time_difference.days, 30)
    hours, seconds = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    milliseconds = time_difference.microseconds // 1000

    return months, days, hours, minutes, seconds, milliseconds

def update_time_label():
    months, days, hours, minutes, seconds, milliseconds = calculate_time_until_date()
    time_str = f"{months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds, {milliseconds} milliseconds"
    time_label.config(text=time_str)
    total_days = days + months * 30 
    total_seconds = total_days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
    seconds_label.config(text=f"Seconds: {total_seconds}")
    minutes_label.config(text=f"Minutes: {total_seconds // 60}")
    hours_label.config(text=f"Hours: {total_seconds // 3600}")
    milliseconds_label.config(text=f"Milliseconds: {total_seconds * 1000 + milliseconds}")
    days_label.config(text=f"Days: {total_days}")

    root.after(1, update_time_label) 

root = tk.Tk()
root.title("Time Until Date App")


time_label = tk.Label(root, text="", font=("Helvetica", 16))
time_label.pack(pady=10)


days_label = tk.Label(root, text="Days: 0", font=("Helvetica", 12))
days_label.pack()

hours_label = tk.Label(root, text="Hours: 0", font=("Helvetica", 12))
hours_label.pack()

minutes_label = tk.Label(root, text="Minutes: 0", font=("Helvetica", 12))
minutes_label.pack()

seconds_label = tk.Label(root, text="Seconds: 0", font=("Helvetica", 12))
seconds_label.pack()

milliseconds_label = tk.Label(root, text="Milliseconds: 0", font=("Helvetica", 12))
milliseconds_label.pack()


update_time_label()


root.mainloop()
