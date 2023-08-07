from PyPDF2 import PdfReader
import pdfplumber
import pyttsx3 as tts
from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()
root.geometry("400x200")
root.title("Convert pdf to mp3")

def pdf_to_mp3():
    pdf_file = askopenfilename(filetypes=[('PDF files', '*.pdf')])
    filename_full = os.path.basename(pdf_file)
    filename = os.path.splitext(filename_full)[0] # gets the file name without the extension
    filename_mp3 = filename + ".mp3"

    pdf_reader = PdfReader(pdf_file) # creating a pdf reader object

    text_to_mp3 = ""
    for page in pdf_reader.pages:
        text_to_mp3 += page.extract_text()

    file_mp3 = asksaveasfilename(initialfile=filename_mp3)
    if file_mp3:
        print(f"file_mp3: {file_mp3}")
        engine = tts.init()
        engine.save_to_file(text_to_mp3, f'{file_mp3}.mp3')
        engine.runAndWait()

    info_label = Label(text="File converted", font=("Calibri", 15))
    info_label.pack(pady=20)

title_label = Label(text="Select a pdf file to convert", font=("Calibri", 15))
title_label.pack(pady=10)

select_file_button = Button(text="Select File", command=pdf_to_mp3)
select_file_button.pack()

root.mainloop()
