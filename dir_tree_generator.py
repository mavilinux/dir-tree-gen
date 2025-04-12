# ===========================================================
# Author: Muawia Rehman
# GitHub: https://github.com/mavilinux
# Description: Directory Tree Generator - A Python application to
#              generate and save directory structures in Text or PDF format.
# License: MIT License
# Version: 1.0.0
# Date: March 2025
# ===========================================================

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def get_tree_structure(startpath):
    """Recursively get the directory tree structure in the desired format."""
    tree = ''
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level)  # Indentation based on the directory depth
        base_name = os.path.basename(root)
        tree += f"{indent}├── {base_name}/\n" if level != 0 else f"{base_name}/\n"  # Add directory to tree
        subindent = '│   ' * (level + 1)  # Add extra indentation for files
        for i, file in enumerate(files):
            tree += f"{subindent}├── {file}\n" if i < len(files) - 1 else f"{subindent}└── {file}\n"  # Add files with tree formatting
    return tree


def save_as_txt(tree, filepath):
    """Save the tree structure to a text file."""
    with open(filepath, 'w') as f:
        f.write(tree)


def save_as_pdf(tree, filepath):
    """Save the tree structure to a PDF file."""
    c = canvas.Canvas(filepath, pagesize=letter)
    c.setFont("Helvetica", 10)
    width, height = letter
    y_position = height - 40
    for line in tree.splitlines():
        if y_position < 40:  # Start a new page if the current one is full
            c.showPage()
            y_position = height - 40
        c.drawString(40, y_position, line)
        y_position -= 12
    c.save()


def browse_folder():
    """Open file dialog to select a folder."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        tree_structure = get_tree_structure(folder_selected)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, tree_structure)
        folder_path.set(folder_selected)


def save_file():
    """Save the tree structure to a file (TXT or PDF)."""
    tree = output_text.get(1.0, tk.END).strip()
    if not tree:
        messagebox.showwarning("Empty Tree", "There is no tree structure to save.")
        return

    file_type = file_format.get()
    if file_type == 'Text File':
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file:
            save_as_txt(tree, file)
            messagebox.showinfo("Success", "Tree structure saved as a .txt file.")
    elif file_type == 'PDF File':
        file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file:
            save_as_pdf(tree, file)
            messagebox.showinfo("Success", "Tree structure saved as a .pdf file.")


def exit_program():
    """Exit the application."""
    root.quit()


# Create the main window
root = tk.Tk()
root.title("Directory Tree Generator")
root.geometry("600x500")
root.config(bg="#f0f0f0")  # Set background color for the main window

# Folder selection section (Entry for displaying path)
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

# Label for Select Folder, aligned to the start
select_label = tk.Label(frame, text="Select Folder:", bg="#f0f0f0", font=("Arial", 12, "bold"))
select_label.grid(row=0, column=0, padx=10, sticky="w")

# Variable to store the folder path
folder_path = tk.StringVar()

# Entry widget to display the selected folder path (width increased)
folder_entry = tk.Entry(frame, textvariable=folder_path, width=30, font=("Arial", 12))
folder_entry.grid(row=0, column=1, padx=10)

# Button to trigger folder selection
select_button = tk.Button(frame, text="Browse", command=browse_folder, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="solid", bd=2)
select_button.grid(row=0, column=2, padx=10)

# Output tree structure section
output_text = scrolledtext.ScrolledText(root, width=70, height=20, font=("Courier New", 10))
output_text.pack(pady=10)

# Frame for the save and exit buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

# Label for "Choose Format:" aligned to the left
format_label = tk.Label(button_frame, text="Choose Format:", bg="#f0f0f0", font=("Arial", 12, "bold"))
format_label.grid(row=0, column=0, padx=10, sticky="w")

# ComboBox to select file format (Text or PDF) moved to second position
file_format = tk.StringVar(value="Text File")
file_format_menu = Combobox(button_frame, textvariable=file_format, values=["Text File", "PDF File"], state="readonly", font=("Arial", 12))
file_format_menu.grid(row=0, column=1, padx=10)

# Save button for Tree (PDF or Text) moved to third position
save_button = tk.Button(button_frame, text="Save Tree", command=save_file, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="solid", bd=2)
save_button.grid(row=0, column=2, padx=10)

# Exit button
exit_button = tk.Button(button_frame, text="Exit", command=exit_program, font=("Arial", 12, "bold"), bg="#f44336", fg="white", relief="solid", bd=2)
exit_button.grid(row=0, column=3, padx=10)

# Run the Tkinter event loop
root.mainloop()
