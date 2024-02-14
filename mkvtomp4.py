import subprocess  # Provides functions to run and manage external processes
import sys         # Access to system-specific variables and functions
import os          # Offers ways to interact with the operating system
import tkinter as tk  # The GUI toolkit for Python
import shutil      # High-level file operations (like copying)
from tkinter import filedialog  # Dialogs for file selection
import threading   # To enable concurrent operations 


# Initialize global variable for output directory
output_dir = ""

# Function to check dependencies
def check_dependencies():
    if sys.platform.startswith('win'):
        # Check for ffmpeg on Windows
        if not shutil.which('ffmpeg'):
            update_progress_label('ffmpeg not found on Windows. Please install it first.')
            return False
    return True

# Function to convert MKV to MP4
def convert_file(input_file, output_folder):
    global output_dir
    try:
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + '.mp4')
        subprocess.run(['ffmpeg', '-i', input_file, '-codec', 'copy', output_file], check=True)
        update_progress_label("Conversion complete: " + output_file)
        show_open_folder_button()  # Show the open folder button after successful conversion
    except subprocess.CalledProcessError as e:
        update_progress_label("An error occurred: " + str(e))

# Function to open output folder
def open_output_folder():
    global output_dir
    if output_dir:
        if sys.platform.startswith('win'):
            os.startfile(output_dir)
        elif sys.platform.startswith('darwin'):
            subprocess.run(['open', output_dir])
        else:
            subprocess.run(['xdg-open', output_dir])

# Function to handle file selection and conversion
def select_and_convert_file():
    global output_dir
    input_file = filedialog.askopenfilename(
        title="Select MKV file",
        filetypes=(("MKV files", "*.mkv"), ("All files", "*.*"))
    )
    if input_file:
        output_dir = os.path.join(os.getcwd(), 'convert')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        update_progress_label("Converting file...")
        convert_thread = threading.Thread(target=convert_file, args=(input_file, output_dir))
        convert_thread.start()

# Function to show the open folder button
def show_open_folder_button():
    open_button.pack(pady=5)

# Function to update progress label
def update_progress_label(message):
    progress_label.config(text=message)
    root.update_idletasks()

if not check_dependencies():
    sys.exit(1) # End the script if dependencies are missing

# Setting up the application window
root = tk.Tk()
root.title("MKV to MP4 Converter")
root.geometry("400x200")
root.configure(bg='black')

# Convert button
convert_button = tk.Button(root, text="Select MKV and Convert", command=select_and_convert_file, bg="white", fg="black")
convert_button.pack(pady=20)

# Progress label
progress_label = tk.Label(root, text="", bg="black", fg="white")
progress_label.pack(pady=5)

# Open folder button (initially not visible)
open_button = tk.Button(root, text="Open Output Folder", command=open_output_folder, bg="white", fg="black")

# Run the application
root.mainloop()