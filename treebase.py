from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Cipher - TreeBase")
root.geometry("1000x500")

#Add some style
style = ttk.Style()

#Pick a theme
style.theme_use('default')

#Configure the treeview colors
style.configure("Treeview", 
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground= "#D3D3D3",
                )

#Change selected color
style.map("Treeview", 
          background= [('selected', '#347083')]
          )

#Create a treeview frame
#Scroll bar works well when you stick them in a frame rather than the treeview itself

tree_frame = Frame(root)
tree_frame.pack(pady=10)

#Create a treeview Scrollbar

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

#Create the treeview

#Configure the scrollbar

#define our columns

#Format our columns

#Create Headings

#Add Fake data

#Create stripped row tags

#Add Record entry boxes


# Add Buttons

root.mainloop()