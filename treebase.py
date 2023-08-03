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
my_tree = ttk.Treeview(tree_frame, yscrollcommand= tree_scroll.set, selectmode="extended")
my_tree.pack()

#Configure the scrollbar
tree_scroll.config(command= my_tree.yview)

#define our columns
my_tree['columns'] = ("First Name", "Last Name", "ID", "Address", "City", "State", "ZipCode")

#Format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Address", anchor=CENTER, width=140)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("State", anchor=CENTER, width=140)
my_tree.column("ZipCode", anchor=CENTER, width=140)

#Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("ZipCode", text="ZipCode", anchor=CENTER)

#Add Fake data
data = [
    ["Brain", "Cipher", 1, "123 Oklahoma St", "Texas", "Famagusta", 99450],
    ["Logan", "Paul", 2, "123 Vegas St", "Las Vegas", "Vegas", 12389],
    ["Derrick", "Hans", 3, "54 Nevada St", "Nevada", "Texas", 34672],
    ["Curry", "Jones", 4, "123 Texas St", "California", "Famagusta", 52621],
    ["Brain", "Cipher", 5, "123 Oklahoma St", "Texas", "Famagusta", 99450],
    ["Logan", "Paul", 6, "123 Vegas St", "Las Vegas", "Vegas", 12389],
    ["Derrick", "Hans", 7, "54 Nevada St", "Nevada", "Texas", 34672],
    ["Curry", "Jones", 8, "123 Texas St", "California", "Famagusta", 52621],
    ["Brain", "Cipher", 9, "123 Oklahoma St", "Texas", "Famagusta", 99450],
    ["Logan", "Paul", 10, "123 Vegas St", "Las Vegas", "Vegas", 12389],
    ["Derrick", "Hans", 11, "54 Nevada St", "Nevada", "Texas", 34672],
    ["Curry", "Jones", 12, "123 Texas St", "California", "Famagusta", 52621],
    ["Brain", "Cipher", 13, "123 Oklahoma St", "Texas", "Famagusta", 99450],
    ["Logan", "Paul", 14, "123 Vegas St", "Las Vegas", "Vegas", 12389],
    ["Derrick", "Hans", 15, "54 Nevada St", "Nevada", "Texas", 34672],
    ["Curry", "Jones", 16, "123 Texas St", "California", "Famagusta", 52621],
   
]

#Create stripped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")


#Add our data to the screen
global count
count = 0

for record in data: 
    if count % 2 == 0: 
        my_tree.insert(parent='', index='end', iid= count, text='', value=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('evenrow'))
    else:
         my_tree.insert(parent='', index='end', iid= count, text='', value=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('oddrow'))
    #increment the counter
    count += 1


#Add Record entry boxes


# Add Buttons

root.mainloop()