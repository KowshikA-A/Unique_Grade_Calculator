import tkinter as tk
from tkinter import ttk

# Define a custom grading scale with unique color shades
custom_grading_scale = {
    'A+': ('#9C27B0', 95),  # Purple
    'A': ('#03A9F4', 90),   # Light Blue
    'A-': ('#00BCD4', 85),  # Cyan
    'B+': ('#4CAF50', 80),  # Green
    'B': ('#FFC107', 75),   # Yellow
    'B-': ('#FF5722', 70),  # Deep Orange
    'C+': ('#FF9800', 65),  # Orange
    'C': ('#795548', 60),   # Brown
    'C-': ('#607D8B', 55),  # Blue Grey
    'D': ('#616161', 50),   # Grey
    'F': ('#000000', 0)     # Black
}

# Function to calculate the relative grade and set the label text and color
def calculate_relative_grade():
    actual_score_text = actual_score_entry.get()
    max_score_text = max_score_entry.get()
    total_strength_text = total_strength_entry.get()

    try:
        actual_score = float(actual_score_text)
        max_score = float(max_score_text)
        total_strength = int(total_strength_text)
    except ValueError:
        # Handle the case where input is not a valid number
        relative_grade_label.config(text="Please enter valid numbers for actual score, maximum score, and total strength.", fg='#FF5722')  # Set text color to Deep Orange
        return

    if max_score <= 0:
        relative_grade_label.config(text="Maximum Score must be greater than 0.", fg='#FFC107')  # Set text color to Yellow
    elif total_strength <= 0:
        relative_grade_label.config(text="Total Strength must be greater than 0.", fg='#FFC107')  # Set text color to Yellow
    elif actual_score < 0:
        relative_grade_label.config(text="Actual Score cannot be negative.", fg='#FFC107')  # Set text color to Yellow
    else:
        relative_grade = calculate_relative_grade_score(actual_score, max_score, total_strength)
        relative_grade_label.config(text=f"Relative Grade: {relative_grade[0]}", fg=relative_grade[1])  # Set text and color

# Function to calculate the relative grade based on actual score, maximum score, and total strength
def calculate_relative_grade_score(actual_score, max_score, total_strength):
    percentile = (actual_score / max_score) * 100

    for grade, (color, lower_bound) in custom_grading_scale.items():
        if percentile >= lower_bound:
            return (grade, color)
    
    return ('F', '#000000')  # Set to 'F' if no other grade matches

# Create the main application window
app = tk.Tk()
app.title("Unique Grading Calculator")
app.configure(bg='#B3E0E6')  # Light Blue background

# Create a frame with a colorful border and padding
outer_frame = tk.Frame(app, bd=2, relief="solid", bg='#4CAF50')  # Green border
outer_frame.pack(padx=15, pady=15)

frame = tk.Frame(outer_frame, bd=0, relief="solid")  # Set borderwidth to 0 to remove the border
frame.configure(bg='#E1F5FE', padx=10, pady=10)  # Light Blue background and padding
frame.pack()

# Create input fields and labels within the frame with padding
actual_score_label = tk.Label(frame, text="Actual Score:")
actual_score_label.configure(bg='#E1F5FE')  # Light Blue background
actual_score_label.pack(pady=5)  # Add vertical space

actual_score_entry = tk.Entry(frame)
actual_score_entry.configure( insertbackground='#9C27B0', highlightthickness=0, bg='#E0E0E0')  # Unique Purple insert background and Grey background color
actual_score_entry.pack(pady=5)  # Add vertical space

max_score_label = tk.Label(frame, text="Maximum Score (Class's Highest Score):")
max_score_label.configure(bg='#E1F5FE')  # Light Blue background
max_score_label.pack(pady=5)  # Add vertical space

max_score_entry = tk.Entry(frame)
max_score_entry.configure( insertbackground='#9C27B0', highlightthickness=0, bg='#E0E0E0')  # Unique Purple insert background and Grey background color
max_score_entry.pack(pady=5)  # Add vertical space

total_strength_label = tk.Label(frame, text="Total Strength (Class Size):")
total_strength_label.configure(bg='#E1F5FE')  # Light Blue background
total_strength_label.pack(pady=5)  # Add vertical space

total_strength_entry = tk.Entry(frame)
total_strength_entry.configure( insertbackground='#9C27B0', highlightthickness=0, bg='#E0E0E0')  # Unique Purple insert background and Grey background color
total_strength_entry.pack(pady=5)  # Add vertical space

# Create a custom style for the button with a unique look
style = ttk.Style()
style.configure('TButtonUnique.TButton', padding=0, borderwidth=0, focuscolor=0, background='#FF5722', relief='flat')  # Deep Orange button with no border
calculate_button = ttk.Button(frame, text="Calculate Relative Grade", command=calculate_relative_grade, style='TButtonUnique.TButton')
calculate_button.pack(pady=8)  # Add vertical space

relative_grade_label = tk.Label(frame, text="Relative Grade:", fg='#795548', bg='#E1F5FE')  # Set text color to Brown and Light Blue background
relative_grade_label.pack()

# Start the main event loop
app.mainloop()






















