from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import simpledialog

root=Tk()
root.title("Notepad")
#root.iconbitmap("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_M6SzMy82SMHPAcWvpDIZoTiPKYXvhxnswA&usqp=CAU")
root.geometry("1200x660")

cu_file_path=""
global selected
selected=False


#File Menu

#New menu
def new_file():
    text_b.delete("1.0",END)
    root.title("New")

#New window
# def new_win():
#     root.title("New Window")
    

#Open
def open_file():
    # save_file()
    text_b.delete("1.0",END) #clear text box
    #open dialog box
    text_file = filedialog.askopenfilename(initialdir="C:/Users/91956/", title="Open File", filetype=(("Text File","*.txt"),("All Files","*.*")))
    name=text_file
    #rename file address
    name=name.replace("C:/Users/91956/","")
    root.title(f'{name}')
    #open file 
    with open(text_file, "r") as file:
        stuff = file.read()
        # add file to text box
        text_b.insert('end', stuff)


            
#save the updates
def save_file():
    global cu_file_path
    if cu_file_path:
        # Open file for writing
        with open(cu_file_path, "w") as file:
            file.write(text_b.get("1.0", "end"))
    

#save as
def save_as():
    global cu_file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialdir="C:/Users/91956/", title="Save As",filetype=(("Text File", "*.txt"), ("All Files", "*.*")))
    if file_path:
        cu_file_path= file_path
        name = file_path.replace("C:/Users/91956/", "")
        root.title(f'{name}')
        # open file for writing
        with open(file_path, "w") as file:
            file.write(text_b.get("1.0", "end"))
    



#edit menu

#cut    
def cut_text():
    global selected
    if text_b.selection_get():
        selected = text_b.selection_get() 
        text_b.delete("sel.first", "sel.last")

#copy
def copy_text():
    global selected
    if text_b.selection_get():
        selected = text_b.selection_get()

#paste
def paste_text():
    if selected:
        position = text_b.index(INSERT)
        text_b.insert(position, selected)


#select all
def select_All():
    text_b.tag_add("sel","1.0", "end")

#find
def find_text():
    search_text = simpledialog.askstring("Find", "Enter text to find:")
    if search_text:
        start_pos = text_b.search(search_text, "1.0", stopindex="end", nocase=True)
        if start_pos:
            end_pos = f"{start_pos}+{len(search_text)}c"
            text_b.tag_remove("sel", "1.0", "end")
            text_b.tag_add("sel", start_pos, end_pos)
            text_b.mark_set("insert", start_pos)
            text_b.see("insert")


#delete
def delete_text():
    global selected
    if text_b.selection_get():
        text_b.delete("sel.first", "sel.last")
            


# def i_word():
#     italics_f= font.Font(text_b, text_b.)
    

#main frame
m_frame = Frame(root)
m_frame.pack(pady=5)

#scroll bar
scroll = Scrollbar(m_frame)
scroll.pack(side=RIGHT,fill=Y)

#menu bar
menu_bar = Menu(root)   
root.config(menu=menu_bar)

#file menu
file_menu = Menu(menu_bar, tearoff=False) #tearoff is to seperate buttons from menu bar  
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)
# file_menu.add_command(label="New Window", command= new_win)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)





#status bar
#status_bar = Label(root, text="")
#status.pack(fill=X, side=BOTTOM, ipady=5)

#text box
text_b= Text(m_frame, width=140, height=37, font=("Ariel", 11 ), selectbackground="navy blue", selectforeground="white", undo = True , yscrollcommand=scroll.set)
text_b.pack()


#edit menu
edit_menu = Menu(menu_bar, tearoff=False)  
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text_b.edit_undo)
edit_menu.add_command(label="Redo", command=text_b.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut",command=lambda:cut_text())
edit_menu.add_command(label="Copy",command=lambda:copy_text())
edit_menu.add_command(label="Paste",command=lambda:paste_text())
edit_menu.add_command(label="Delete",command=lambda:delete_text())
edit_menu.add_separator()
edit_menu.add_command(label="Find",command=lambda:find_text())
edit_menu.add_command(label="Select All", command=select_All)

#adding scroll bar
scroll.config(command=text_b.yview)

root.mainloop()
