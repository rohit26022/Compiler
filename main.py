import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import os
from datetime import datetime

from ai_client import AIClient
from config import API_KEY

ai = AIClient(API_KEY)

def run_code():
    code = code_editor.get("1.0", tk.END)
    with open("temp_exec.py", "w") as temp_file:
        temp_file.write(code)
    try:
        output = subprocess.check_output(["python", "temp_exec.py"], stderr=subprocess.STDOUT, text=True)
        output_console.config(state='normal')
        output_console.delete("1.0", tk.END)
        output_console.insert(tk.END, output)
        output_console.config(state='disabled')
    except subprocess.CalledProcessError as e:
        output_console.config(state='normal')
        output_console.delete("1.0", tk.END)
        output_console.insert(tk.END, e.output)
        output_console.config(state='disabled')

def save_code():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    filename = f"generated_code_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    filepath = filedialog.asksaveasfilename(defaultextension=".py", initialdir=desktop, initialfile=filename)
    if filepath:
        with open(filepath, "w") as f:
            f.write(code_editor.get("1.0", tk.END))
        messagebox.showinfo("Saved", f"File saved to {filepath}")

def ai_generate_code():
    prompt = prompt_entry.get("1.0", tk.END).strip()
    if not prompt:
        messagebox.showwarning("Warning", "Enter a prompt to generate code.")
        return
    generated = ai.generate_code(prompt)
    code_editor.insert(tk.END, f"\n# AI GENERATED CODE\n{generated}\n")


root = tk.Tk()
root.title("Gemini Code Editor - Mini IDE")
root.geometry("1000x700")

prompt_label = tk.Label(root, text="Prompt for AI Code Generation:")
prompt_label.pack()
prompt_entry = scrolledtext.ScrolledText(root, height=4)
prompt_entry.pack(fill="x", padx=10)

generate_btn = tk.Button(root, text="Generate Code", command=ai_generate_code)
generate_btn.pack(pady=5)

code_editor = scrolledtext.ScrolledText(root, font=("Courier", 12))
code_editor.pack(expand=True, fill="both", padx=10, pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)
run_btn = tk.Button(button_frame, text="Run Code", command=run_code)
run_btn.pack(side="left", padx=5)
save_btn = tk.Button(button_frame, text="Save to Desktop", command=save_code)
save_btn.pack(side="left", padx=5)

output_label = tk.Label(root, text="Output Console:")
output_label.pack()
output_console = scrolledtext.ScrolledText(root, height=10, state='disabled', bg="#111", fg="#0f0")
output_console.pack(fill="x", padx=10, pady=5)

root.mainloop()