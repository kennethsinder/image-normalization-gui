#!/usr/bin/python

from tkinter.filedialog import askopenfilename
import tkinter
import os
import cv2
import numpy as np
import os
import os.path

# I got tired of the deprecation warning on my Mac
os.environ['TK_SILENCE_DEPRECATION'] = '1'

window = tkinter.Tk()
window.title('Image Normalization tool')

image_file_path = None


def histogram(file_path):
    img = cv2.imread(file_path, 0)
    equ = cv2.equalizeHist(img)
    print(os.path.basename(os.path.normpath(file_path)))
    cv2.imwrite(os.path.basename(os.path.normpath(file_path)), equ)


def choose_file(event):
    image_file_path = askopenfilename(
        initialdir="/", title="Select file",
        filetypes=(("png files", "*.png"), ("all files", "*.*")))
    print(image_file_path if image_file_path else 'No file chosen')
    if image_file_path:
        histogram(image_file_path)


button_widget = tkinter.Button(
    window, text='Select image to histogram-equalize...')
button_widget.pack()

button_widget.bind('<Button-1>', choose_file)

window.mainloop()
