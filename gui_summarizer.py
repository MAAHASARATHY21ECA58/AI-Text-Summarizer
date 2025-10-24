import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

# Load the summarizer model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=-1)  # CPU

# Function to summarize text
def summarize_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter some text to summarize.")
        return
    
    # Automatically adjust max_length based on input length
    word_count = len(text.split())
    max_len = min(60, word_count // 2 + 5)
    
    try:
        summary = summarizer(text, max_length=max_len, min_length=5, do_sample=False)[0]['summary_text']
    except Exception as e:
        summary = f"Error during summarization: {e}"
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)

# Function to clear text boxes
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Create main window
root = tk.Tk()
root.title("AI Text Summarizer")
root.geometry("700x500")
root.resizable(False, False)

# Input text box with scroll
tk.Label(root, text="Enter text to summarize:", font=("Helvetica", 12)).pack(pady=5)
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, font=("Helvetica", 11))
input_text.pack(pady=5)

# Summarize button
summarize_btn = tk.Button(root, text="Summarize", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=summarize_text)
summarize_btn.pack(pady=10)

# Clear button
clear_btn = tk.Button(root, text="Clear", font=("Helvetica", 12), bg="#f44336", fg="white", command=clear_text)
clear_btn.pack(pady=5)

# Output text box with scroll
tk.Label(root, text="Summary:", font=("Helvetica", 12)).pack(pady=5)
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, font=("Helvetica", 11))
output_text.pack(pady=5)

# Run the GUI
root.mainloop()
