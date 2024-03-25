from tkinter import Tk, Label, Button, messagebox, Toplevel, Canvas, PhotoImage

from PIL import ImageTk, Image


def anderesite():
    windows2 = Toplevel()
    windows2.title("Personal Daten")
    windows2.geometry("500x500")

def demoColorChange(): 
    button01.configure(bg="red", fg="yellow")

windows = Tk()
windows.title("Dein Grüne Apfel")
windows.geometry("500x500")

image = Image.open("Apfel.png")

resize_image = image.resize((400, 500))
# Add image file 
img = ImageTk.PhotoImage(resize_image)

#icon
#img = PhotoImage("Apfel.png")
# windows.iconphoto(False, img)

# Create Canvas 
canvas1 = Canvas( windows, width = 500, 
				height = 500) 

canvas1.pack(fill = "both", expand = True) 

# Display image 
canvas1.create_image( 160, 150, image = img, anchor = "nw") 

# Add Text 
canvas1.create_text( 250, 50, text = "Dein Grüne Apfel", font=("Helvetica", 20)) 
canvas1.create_text( 250, 120, text = "Mit Unserer Anwendung können Sie Kalorien berechnen ", font=("Helvetica", 14)) 

# add Button
button01 = Button(windows, text="Personal Daten", command=anderesite, font=("Helvetica", 12), fg='#eae0d5', bg='#007f5f')
button1_canvas = canvas1.create_window( 200, 200, 
									anchor = "nw", 
									window = button01)


windows.mainloop()

