import tkinter as tk
from tkinter import messagebox, filedialog
from gtts import gTTS
import os
from playsound import playsound

root = tk.Tk()
root.title("Text to Speech ")
root.geometry("500x300")

def play_text():
    text = text_entry.get()  
    if text: 
        tts = gTTS(text=text, lang='ar')  
        tts.save("output.mp3") 
        playsound("output.mp3")
    else:
        messagebox.showwarning("تحذير", "الرجاء إدخال النص!") 

def set_text():
    text_entry.delete(0, tk.END)  

def save_text():
    text = text_entry.get() 
    if text: 
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path: 
            with open(file_path, "w", encoding="utf-8") as file: 
                file.write(text)
            messagebox.showinfo("نجاح", "تم حفظ النص بنجاح!") 
    else:
        messagebox.showwarning("تحذير", "لا يوجد نص لحفظه!") 

def exit_app():
    root.destroy()  

tk.Label(root, text="أدخل النص:", font=("Arial", 14)).pack(pady=10)

text_entry = tk.Entry(root, font=("Arial", 14), width=30)
text_entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

play_btn = tk.Button(btn_frame, text="تشغيل", bg="green", fg="white", font=("Arial", 12), command=play_text)
play_btn.grid(row=0, column=0, padx=10)

set_btn = tk.Button(btn_frame, text="مسح", bg="blue", fg="white", font=("Arial", 12), command=set_text)
set_btn.grid(row=0, column=1, padx=10)

exit_btn = tk.Button(btn_frame, text="خروج", bg="red", fg="white", font=("Arial", 12), command=exit_app)
exit_btn.grid(row=0, column=3, padx=10)

root.mainloop()