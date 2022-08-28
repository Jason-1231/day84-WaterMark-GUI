from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.ttk import *
from PIL import Image, ImageTk

logo_img = Image.open('Kobe_logo.png').convert("RGBA")


def open_image():
    global base_img
    global img
    global file_path
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*.jpeg'), ('All Files', '*.*')])
    # print(file_path.name)
    img = Image.open(file_path.name)
    base_img = ImageTk.PhotoImage(img)
    img_label.config(image=base_img)


def add_watermark():
    global logo_img
    global base_img
    global new_base_img
    global transparent
    # Adjust dimensions according to base image
    width, height = img.size
    l_height = int(round(height / 3, 0))
    l_width = int(round(width / 3, 0))
    l_pos_x = width - l_width
    l_pos_y = height - l_height

    # Resize logo image
    logo_img = logo_img.resize((l_width, l_height))

    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(img, (0, 0))
    transparent.paste(logo_img, (l_pos_x, l_pos_y), mask=logo_img)
    # transparent.show()
    new_base_img = ImageTk.PhotoImage(transparent)
    img_label.config(image=new_base_img)


def save():
    file_name = file_path.name.split('/')[-1].replace('.jpeg', '')
    # print(file_name)
    to_save = transparent.convert("RGB")
    to_save.save(file_name + '_watermarked.jpeg', format='jpeg')
    to_save.show()


# Create GUI interface
root = Tk()
root.title("Watermark GUI application")
# root.geometry("700x500")

# Open Image open_btn on GUI
open_btn = Button(root, text="Open Image", command=open_image)
open_btn.pack()

base_img_frame = LabelFrame(root)
base_img_frame.pack()

img_label = Label(base_img_frame)
img_label.pack()

watermark_btn = Button(root, text="Add logo watermark", command=add_watermark)
watermark_btn.pack()

save_btn = Button(root, text="Save", command=save)
save_btn.pack()

root.mainloop()
