import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
from PIL import Image, ImageTk

selected_file = None

def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        global selected_file
        selected_file = file_path
        display_selected_image(file_path)
        messagebox.showinfo("Image Selection", f"Selected image: {file_path}")

def display_selected_image(image_path):
    image = Image.open(image_path)
    image = image.resize((256, 256))
    image_tk = ImageTk.PhotoImage(image)
    selected_image_label.config(image=image_tk)
    selected_image_label.image = image_tk


def run_model1():
    if selected_file:
        subprocess.run(["env_model1/Scripts/python", "D:/учебные/python_projects/данные для диплома/веса для моделей/model1.py", selected_file])
        display_result("result.png")
    else:
        messagebox.showerror("Error", "Please select an image first")

def run_model2():
    if selected_file:
        subprocess.run(["env_model2/Scripts/python", "D:/учебные/python_projects/данные для диплома/веса для моделей/model2.py", selected_file])
        display_result("result_styled.png")
    else:
        messagebox.showerror("Error", "Please select an image first")

def run_model3():
    if selected_file:
        subprocess.run(["env_model3/Scripts/python", "D:/учебные/python_projects/данные для диплома/веса для моделей/model3.py", selected_file])
        display_result("result.png")
    else:
        messagebox.showerror("Error", "Please select an image first")

def display_result(result_path):
    if os.path.exists(result_path):
        result_image = Image.open(result_path)
        result_image = result_image.resize((256, 256))
        result_image_tk = ImageTk.PhotoImage(result_image)
        result_label.config(image=result_image_tk)
        result_label.image = result_image_tk
    else:
        messagebox.showerror("Error", "Unable to find the result.")

root = tk.Tk()
root.title("Model Interface")
root.geometry("400x600")

# Button to select image
btn_open = tk.Button(root, text="Завантажити зображення", command=load_image)
btn_open.pack(pady=10)

# Label to display the selected image
selected_image_label = tk.Label(root)
selected_image_label.pack(pady=10)

# Buttons to run models
btn_run1 = tk.Button(root, text="Колоризація зображення", command=run_model1)
btn_run1.pack(pady=10)

btn_run2 = tk.Button(root, text="Перетворення зображення в художній стиль Клода Моне", command=run_model2)
btn_run2.pack(pady=10)

btn_run3 = tk.Button(root, text="Покращення якості зображення", command=run_model3)
btn_run3.pack(pady=10)

# Label to display result
result_label = tk.Label(root)
result_label.pack(pady=10)

# Start the main application loop
root.mainloop()
