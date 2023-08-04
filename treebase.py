from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Cipher - TreeBase")
root.geometry("1000x500")

# data = [
#     ["Brain", "Cipher", 1, "123 Oklahoma St", "Texas", "Famagusta", 99450],
#     ["Logan", "Paul", 2, "123 Vegas St", "Las Vegas", "Vegas", 12389],
#     ["Derrick", "Hans", 3, "54 Nevada St", "Nevada", "Texas", 34672],
#     ["Curry", "Jones", 4, "123 Texas St", "California", "Famagusta", 52621],
#     ["Brain", "Cipher", 5, "123 Oklahoma St", "Texas", "Famagusta", 99450],
#     ["Logan", "Paul", 6, "123 Vegas St", "Las Vegas", "Vegas", 12389],
#     ["Derrick", "Hans", 7, "54 Nevada St", "Nevada", "Texas", 34672],
#     ["Curry", "Jones", 8, "123 Texas St", "California", "Famagusta", 52621],
#     ["Brain", "Cipher", 9, "123 Oklahoma St", "Texas", "Famagusta", 99450],
#     ["Logan", "Paul", 10, "123 Vegas St", "Las Vegas", "Vegas", 12389],
#     ["Derrick", "Hans", 11, "54 Nevada St", "Nevada", "Texas", 34672],
#     ["Curry", "Jones", 12, "123 Texas St", "California", "Famagusta", 52621],
#     ["Brain", "Cipher", 13, "123 Oklahoma St", "Texas", "Famagusta", 99450],
#     ["Logan", "Paul", 14, "123 Vegas St", "Las Vegas", "Vegas", 12389],
#     ["Derrick", "Hans", 15, "54 Nevada St", "Nevada", "Texas", 34672],
#     ["Curry", "Jones", 16, "123 Texas St", "California", "Famagusta", 52621],
   
# ]
#some database stuffs
#Create a database or connect to one that exists

conn = sqlite3.connect('tree_crm.db')

#create a cursor instance 
#a cursor is like a little robot which you can send to go stuffs for you

c = conn.cursor()

#Create a table
c.execute(""" 
          CREATE TABLE if not exists customers (
              first_name text,
              last_name text,
              id integer,
              address text,
              city text,
              state text,
              zipcode text)
          """)

#Add dummy data to table
# for record in data:
#     c.execute("INSERT INTO  customers VALUES (:first_name, :last_name, :id, :address, :city, :state, :zipcode)", 
              
#               {
#                 'first_name': record[0],
#                 'last_name': record[1],
#                 'id': record[2],
#                 'address': record[3],
#                 'city': record[4],
#                 'state': record[5],
#                 'zipcode': record[6],
                
#               }
              
#               )

#Commit the changes
conn.commit()

#Close our connection
conn.close()


def query_database():
    #Create a database or connect to one that exists

    conn = sqlite3.connect('tree_crm.db')

    #create a cursor instance 
    #a cursor is like a little robot which you can send to go stuffs for you

    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM customers")
    records = c.fetchall()
    
    #Add our data to the screen
    global count
    count = 0

    for record in records: 
        if count % 2 == 0: 
            my_tree.insert(parent='', index='end', iid= count, text='', value=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=('evenrow'))
        else:
            my_tree.insert(parent='', index='end', iid= count, text='', value=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=('oddrow'))
        #increment the counter
        count += 1
    
    #Commit the changes
    conn.commit()

    #Close our connection
    conn.close()

    


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


#Create stripped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")



#Add Record entry boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label = Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name")
ln_label.grid(row=1, column=0, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=1, column=1, padx=10, pady=10)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=2, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=3, padx=10, pady=10)

address_label = Label(data_frame, text="Address")
address_label.grid(row=1, column=2, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=3, padx=10, pady=10)

city_label = Label(data_frame, text="City")
city_label.grid(row=0, column=4, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=0, column=5, padx=10, pady=10)

state_label = Label(data_frame, text="State")
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)

zip_label = Label(data_frame, text="ZipCode")
zip_label.grid(row=1, column=6, padx=10, pady=10)
zip_entry = Entry(data_frame)
zip_entry.grid(row=1, column=7, padx=10, pady=10)


#Move Row up
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)
        
#Move Row down
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

#Remove one record
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)


#Remove many records
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)
        

#Remove All Records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)



#Select Record method
def select_record(e):
    #Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zip_entry.delete(0, END)
    
    #Grab record Number
    selected = my_tree.focus()
    
    #Grab record values
    values = my_tree.item(selected, 'values')
    
    # Outputs to entry boxes
    fn_entry.insert(0, values[0])
    ln_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
    address_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    state_entry.insert(0, values[5])
    zip_entry.insert(0, values[6])
    

# Clear Entry boxes
def clear_entries():
     #Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zip_entry.delete(0, END)
    

#Update record
def update_record():
    #Grab the record number
    selected = my_tree.focus()
    #Update record
    my_tree.item(selected, text='', values=(fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zip_entry.get(),))
    
     #Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zip_entry.delete(0, END)
    


# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entries", command= clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

#Bind Treeview
my_tree.bind("<ButtonRelease-1>", select_record)


#Run to pull data from the database on start
query_database()

root.mainloop()