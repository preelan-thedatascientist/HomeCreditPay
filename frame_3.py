from tkinter import *
from helper import *

#-----------------------------------------
def copy_code():
    #Your code that checks the expression
    varContent = text1.get(1.0, END) # get what's written in the inputentry entry widget

    with open('original_code.txt','w+') as f:
        f.write(varContent)
        
    index_values = file_to_code_convertion()
    text2.delete(1.0, END) # clear the outputtext text widget
    text2.insert(END, new_code())

    for index in index_values:
        text2.tag_add("here", index[0], index[1])
        text2.tag_config("here", background = "yellow", foreground = "blue")
#-----------------------------------------
root = Tk()
root.title('Main Frame')
root.geometry('800x600')

# Seems strange to column- and rowconfigure the root but if I don't -
# the text widgets won't resize at all

for i in range(5):
    root.columnconfigure(0, weight=1)
for i in range(1,4):
    root.rowconfigure(1, weight=1)

# make a master PanedWindow
m1 = PanedWindow(root)
m1.grid(column=0, row=0, rowspan=4, columnspan=4, sticky=E+N+W+S)
for i in range(4):
    m1.columnconfigure(i, weight=1) # Enable vertical resizing
for i in range(1,3):
    m1.rowconfigure(i, weight=1) #Enable horizontal resizing

# make a PanedWindow inside m1, positioned to the left
m2=PanedWindow(m1, orient=VERTICAL)
m2.grid(column=0, row=1, columnspan=2, rowspan=2, sticky=E+N+W+S)

for i in range(2):
    m2.columnconfigure(i, weight=1) # Enable vertical resizing
for i in range(1,3):
    m2.rowconfigure(i, weight=1) #Enable horizontal reditmenuizing

# make another PanedWindow inside m1, positioned to the right
m3=PanedWindow(m1,orient=VERTICAL)
m3.grid(column=2, row=1, columnspan=2, rowspan=2, sticky=E+N+W+S)
for i in range(2, 4):
    m3.columnconfigure(i, weight=1) # Enable vertical resizing
for i in range(1,3):
    m3.rowconfigure(i, weight=1) #Enable horizontal resizing

# Add a text widget in m2

text1 = Text(m2, height=29, width =15)
m2.add(text1)

Analysis = Button(m2, text="Analysis", command=copy_code)
m2.add(Analysis)

# Add another textwidget in m3
text2=Text(m3, height=29, width=15)
m3.add(text2)

Button_1=Button(m3, text="Change")
m3.add(Button_1)

Button_2=Button(m3, text="Don't Change")
m3.add(Button_2)

Button_3=Button(m3, text="Manual")
m3.add(Button_3)

root.mainloop()
