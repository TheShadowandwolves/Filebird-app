import tkinter as tk
from tkinter import filedialog
from tkinter import ttk as ttk
import mov as mov
from tkinter.ttk import Treeview as tv
import database as db
####################################################################################################
#           window
####################################################################################################

# Create the main window
root = tk.Tk()
root.resizable(width=False, height=False)  # make the window unresizeable

####################################################################################################
#          set up window
####################################################################################################

# Set the title of the window
root.title("File Bird v0.0.1")
root.iconbitmap("img/FileBird-logo.ico")
# Set the size of the window
root.geometry("800x600")

####################################################################################################
#           menu
####################################################################################################

# Create a menu with some items
menu = tk.Menu(root)

# Create a menu bar

# Create a File menu and add it to the menu bar
file_menu = tk.Menu(menu, tearoff=0)
setting_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Open")
setting_menu.add_command(label="Save")
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Settings", menu=setting_menu)


# menu.add_command(label="Open")
# menu.add_command(label="Save")

menu.add_command(label="Quit", command=root.quit)

# Add the menu to the window
root.config(menu=menu)

####################################################################################################
#           variables
####################################################################################################

checkbox_all = []
checkbox_vars = []
for i in range(10):
    var = tk.StringVar(value=0)
    checkbox_vars.append(var)

var_file = []
check_file = []

####################################################################################################
#       side menu frame
####################################################################################################

# create a frame for the side menu
menu_frame = tk.Frame(root, width=200, height=600, bg="#FA8E36")
menu_frame.pack(side="left", fill="y")

####################################################################################################
#       all frames
####################################################################################################

# create a frame for the content
frame0 = tk.Frame(root, width=600, height=600, bg="#E6F7F8")
frame0.pack(side="right", fill="y")
frame1 = tk.Frame(root, width=600, height=600, bg="#343434")
frame1.pack(side="right", fill="y")
frame2 = tk.Frame(root, width=600, height=600, bg="#E5F2F3")
frame2.pack(side="right", fill="y")
frame3 = tk.Frame(root, width=600, height=600, bg="#FFFFF4")
frame3.pack(side="right", fill="y")

about_frame = tk.Frame(frame0, width=600, height=600, bg="#E6F7F8")
about_frame.pack(side="right", fill="y")

donate_frame = tk.Frame(frame0, width=600, height=600, bg="#E6F7F8")
donate_frame.pack(side="right", fill="y")

social_media_frame = tk.Frame(frame0, width=600, height=600, bg="#E6F7F8")
social_media_frame.pack(side="right", fill="y")


####################################################################################################
#       logo
####################################################################################################


# create a frame for the logo at the top of the side menu
logo_frame = tk.Frame(menu_frame, width=200, height=50, bg="#E6F7F8")
logo_frame.pack(side="top")

####################################################################################################
#       logo
####################################################################################################

# add the logo to the logo frame (replace with your own logo)
logo = tk.PhotoImage(file="img/free Bird side.png")
logo_width = 285  # set the width of the logo to the width of the logo frame
logo_height = int(logo.height() * logo_width / logo.width())  # maintain the aspect ratio of the logo
logo = logo.subsample((logo.width() // logo_width)*2, (logo.height() // logo_height)*2)  # resize the logo
logo_label = tk.Label(logo_frame, image=logo, width=logo_width, height=logo_height)
logo_label.pack()

####################################################################################################
#       functions
####################################################################################################

def change_to_frame0(event=None):
    frame0.pack(fill="both", expand=True)
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    about_frame.pack_forget()
    donate_frame.pack_forget()
    social_media_frame.pack_forget()

def change_to_frame1(event=None):
    frame1.pack(fill="both", expand=True)
    frame0.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    about_frame.pack_forget()
    donate_frame.pack_forget()
    social_media_frame.pack_forget()

def change_to_frame2(event=None):
    frame2.pack(fill="both", expand=True)
    frame0.pack_forget()
    frame1.pack_forget()
    frame3.pack_forget()
    about_frame.pack_forget()
    donate_frame.pack_forget()
    social_media_frame.pack_forget()

def change_to_frame3(event=None):
    frame3.pack(fill="both", expand=True)
    frame0.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()
    about_frame.pack_forget()
    donate_frame.pack_forget()
    social_media_frame.pack_forget()

def change_to_about(event=None):
    about_frame.pack(fill="both", expand=True)
    donate_frame.pack_forget()
    social_media_frame.pack_forget()
    frame0.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()

def change_to_donate(event=None):
    donate_frame.pack(fill="both", expand=True)
    about_frame.pack_forget()
    social_media_frame.pack_forget()
    frame0.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()

def change_to_social_media(event=None):
    social_media_frame.pack(fill="both", expand=True)
    about_frame.pack_forget()
    donate_frame.pack_forget()
    frame0.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()


####################################################################################################
#       main frame
####################################################################################################

#raise frame0
change_to_frame0()

####################################################################################################
#       buttons side menu
####################################################################################################

# create the buttons for the side menu
start_button = tk.Button(menu_frame, text="Start", width=40, height=5, bg="#FA8E18", command=lambda: change_to_frame1())
start_button.pack(pady=10, padx=0)

edit_button = tk.Button(menu_frame, text="Folder Settings", width=40, height=5, bg="#FA8E18", command=lambda: change_to_frame2())
edit_button.pack(pady=10)

keywords_button = tk.Button(menu_frame, text="Keywords Edit", width=40, height=5, bg="#FA8E18", command=lambda: change_to_frame3())
keywords_button.pack(pady=10,padx=0)

about_button = tk.Button(menu_frame, text="About", width=40, height=2, bg="#FA8E18", command=lambda: change_to_about())
about_button.pack(pady=2.5,padx=0)

donate_button = tk.Button(menu_frame, text="Donate", width=40, height=2, bg="#FA8E18", command=lambda: change_to_donate())
donate_button.pack(pady=2.5,padx=0)

social_media_button = tk.Button(menu_frame, text="Social Media", width=40, height=2, bg="#FA8E18", command=lambda: change_to_social_media())
social_media_button.pack(pady=2.5,padx=0)

####################################################################################################
#       content frames
####################################################################################################

# create a frame for the main content
content_frame = tk.Frame(frame0, width=800, height=500, bg="#E6F7F8")
content_frame.pack(side="right", fill="both", expand=True)

#create fram for main content for frame 1
content_frame1 = tk.Frame(frame1, width=800, height=500, bg="#B0C4DE")
content_frame1.pack(side="right", fill="both", expand=True)

#create fram for main content for frame 2
content_frame2 = tk.Frame(frame2, width=800, height=500, bg="#B0C4DE")
content_frame2.pack(side="right", fill="both", expand=True)

#create fram for main content for frame 3
content_frame3 = tk.Frame(frame3, width=800, height=500, bg="#B0C4DE")
content_frame3.pack(side="right", fill="both", expand=True)

content_frame_about = tk.Frame(about_frame, width=800, height=500, bg="#B0C4DE")
content_frame_about.pack(side="right", fill="both", expand=True)

content_frame_donate = tk.Frame(donate_frame, width=800, height=500, bg="#B0C4DE")
content_frame_donate.pack(side="right", fill="both", expand=True)

content_frame_social_media = tk.Frame(social_media_frame, width=800, height=500, bg="#B0C4DE")
content_frame_social_media.pack(side="right", fill="both", expand=True)



#####################################################################################################
#       title frame
#####################################################################################################
#create a frame for the title of the main content
title_frame = tk.Frame(content_frame, width=800, height=50,  bg="#E6F7F8")
title_frame.pack(side="top", fill="x")

#create a frame for the start button
start_frame = tk.Frame(content_frame1, width=800, height=50,  bg="#E6F7F8")
start_frame.pack(side="top", fill="x")

#create a frame for the edit button
folder_settings_frame = tk.Frame(content_frame2, width=800, height=50,  bg="#E6F7F8")
folder_settings_frame.pack(side="top", fill="x")

# create frame for the settings button
settings_frame = tk.Frame(content_frame3, width=800, height=50,  bg="#E6F7F8")
settings_frame.pack(side="top", fill="x")

# create frame for the about button
about_frame = tk.Frame(content_frame_about, width=800, height=50,  bg="#E6F7F8")
about_frame.pack(side="top", fill="x")

# create frame for the donate button
donate_frame = tk.Frame(content_frame_donate, width=800, height=50,  bg="#E6F7F8")
donate_frame.pack(side="top", fill="x")

# create frame for the social media button
social_media_frame = tk.Frame(content_frame_social_media, width=800, height=50,  bg="#E6F7F8")
social_media_frame.pack(side="top", fill="x")


#####################################################################################################
#       title
#####################################################################################################

# add the title to the title frame
title = tk.Label(title_frame, text="File Bird", font=("Helvetica", 24),  bg="#E6F7F8")
title.pack(padx=20, pady=20)

# add the title to the start frame
start_title = tk.Label(start_frame, text="Start", font=("Helvetica", 24),  bg="#E6F7F8")
start_title.pack(padx=20, pady=20)

# add the title to the edit frame
edit_title = tk.Label(folder_settings_frame, text="Folder Settings", font=("Helvetica", 24),  bg="#E6F7F8")
edit_title.pack(padx=20, pady=20)

# add the title to the settings frame
settings_title = tk.Label(settings_frame, text="Keyword Settings", font=("Helvetica", 24),  bg="#E6F7F8")
settings_title.pack(padx=20, pady=20)

# add the title to the about frame
about_title = tk.Label(about_frame, text="About", font=("Helvetica", 24),  bg="#E6F7F8")
about_title.pack(padx=20, pady=20)

# add the title to the donate frame
donate_title = tk.Label(donate_frame, text="Donate", font=("Helvetica", 24),  bg="#E6F7F8")
donate_title.pack(padx=20, pady=20)

# add the title to the social media frame
social_media_title = tk.Label(social_media_frame, text="Social Media", font=("Helvetica", 24),  bg="#E6F7F8")
social_media_title.pack(padx=20, pady=20)


#####################################################################################################
#       button frame
#####################################################################################################

# # label for the start button
# start_button_label = tk.Label(start_frame, text="Start", font=("Helvetica", 16),  bg="#E6F7F8")
# start_button_label.pack(side="left", padx=20, pady=20)

# # label for the edit button
# edit_button_label = tk.Label(folder_settings_frame, text="Folder settings", font=("Helvetica", 16),  bg="#E6F7F8")
# edit_button_label.pack(side="left", padx=20, pady=20)

# # label for the settings button
# settings_button_label = tk.Label(settings_frame, text="Keyword Settings", font=("Helvetica", 16),  bg="#E6F7F8")
# settings_button_label.pack(side="left", padx=20, pady=20)

#####################################################################################################
#       intro text
#####################################################################################################

#"Introducing FileBird - the revolutionary file organization tool that makes it easy to sort and manage your files. With FileBird, you can effortlessly organize your files into custom folders based on file type and name, so you can quickly find what you need when you need it. Say goodbye to cluttered and disorganized folders, and say hello to a new level of file organization and productivity with FileBird."
# add the text to the main content frame
main_text = "Introducing FileBird - the revolutionary file organization tool that makes it easy to sort and manage your files. With FileBird, you can effortlessly organize your files into custom folders based on file type and name, so you can quickly find what you need when you need it. Say goodbye to cluttered and disorganized folders, and say hello to a new level of file organization and productivity with FileBird."
main_label = tk.Label(content_frame, text=main_text, font=("Helvetica", 16),  bg="#E6F7F8", justify="left", anchor="nw", wraplength=400)
main_label.pack(padx=20, pady=20)


####################################################################################################
#       return to main
####################################################################################################
def return_to_main():
    change_to_frame0()



#back button for each frame
back_button = tk.Button(content_frame1, text="Back", width=10, height=2, bg="#E6F7F8", command=return_to_main)
back_button.place(x=0, y=0)

back_button2 = tk.Button(content_frame2, text="Back", width=10, height=2, bg="#E6F7F8", command=return_to_main)
back_button2.place(x=0, y=0)

back_button3 = tk.Button(content_frame3, text="Back", width=10, height=2, bg="#E6F7F8", command=return_to_main)
back_button3.place(x=0, y=0)


####################################################################################################
#       functions
####################################################################################################
# def process_text(event):
#     # Get the text that the user entered
#     text = entry.get()

#     # Create a Label widget
#     label = tk.Label(frame1, text=text)
#     label.place(x= 1, y = 300)
#     # Do something with the text
#     print(text)
#     return text

def dir_label(text, n):
    # Create a Label widget
    if n== 1:
       dir_label_.config(text=text)
    elif n==2:
        dir_label_2.config(text=text)
        
def select_folder2():
    # Select the folder
    folder_selected = filedialog.askdirectory()
    entry_dir2.delete(0, tk.END)
    entry_dir2.insert(0, folder_selected)
    dir_label(folder_selected, 2)
    

def select_folder():
    # Open a directory selector
    folder_path = filedialog.askdirectory()

    # Set the text of the Entry widget to the selected folder path
    entry_dir.delete(0, tk.END)
    entry_dir.insert(0, folder_path)

    # Call the dir_label function, passing the folder_path as an argument
    dir_label(folder_path, 1)

def submit():
    # Get the text that the user entered
    origin = entry_dir.get()
    print(origin)
    destination = entry_dir2.get()
    chose = get_clicked_checkboxes()
    suc = mov.run(origin, destination, chose)
    if suc == "success":
        success_label.config(text="", bg="#E6F7F8", fg="black")
        success_label.config(text="Success!", bg="green", fg="white")
    elif suc == "Error: NO CHOICE WAS MADE":
        #"Error: NO CHOICE WAS MADE"
        success_label.config(text="", bg="#E6F7F8", fg="black")
        success_label.config(text="Error: NO CHOICE WAS MADE", bg="red", fg="white")
    elif suc == "Error: Path does not exist":
        #"Error: Path does not exist"
        success_label.config(text="", bg="#E6F7F8", fg="black")
        success_label.config(text="Error: Path does not exist", bg="red", fg="white")
        
        

def get_clicked_checkboxes():
    clicked_checkboxes = []
    for i in range(len(checkbox_vars)):
        ck = checkbox_vars[i].get()
        if ck != "0":
            clicked_checkboxes.append(ck)
            # print("Checkbox " + str(i) + " is checked")
    return clicked_checkboxes

# def get_clicked_output():
#     text = "these were clicked: "
#     gc = get_clicked_checkboxes()
#     for cb in gc:
#         text += str(cb) + " "
#     clicked_checkboxes_label.config(text=text)



####################################################################################################
#       content frame 1
####################################################################################################
start_label_insert = tk.Label(content_frame1, text="Choose directory from where the files should be cleaned: ", font=("Helvetica", 8),height=1,  bg="#E6F7F8")
start_label_insert.place(x= 2, y = 100)

dir_label_ = tk.Label(content_frame1, text="No directory choosen", font=("Helvetica", 8),  bg="#E6F7F8", wraplength= 500)
dir_label_.place(x= 120, y = 130)

file_type_chose_label =  tk.Label(content_frame1, text="Choose file type you want to sort for: ", font=("Helvetica", 8),  bg="#E6F7F8")
file_type_chose_label.place(x= 2, y = 160)

location_label = tk.Label(content_frame1, text="Choose directory where the files should be sorted: ", font=("Helvetica", 8),  bg="#E6F7F8")
location_label.place(x= 2, y = 290)

dir_label_2 = tk.Label(content_frame1, text="No directory choosen", font=("Helvetica", 8),  bg="#E6F7F8", wraplength= 500)
dir_label_2.place(x= 120, y = 320)

imp_mess_label = tk.Label(content_frame1, text="Important: The files will be moved to the choosen directory, not copied", font=("Helvetica", 8),  bg="#E6F7F8")
imp_mess_label.place(x= 2, y = 350)
imp2_mess_label = tk.Label(content_frame1, text="Changing folder names, need to be done in the folder settings", font=("Helvetica", 8),  bg="#E6F7F8")
imp2_mess_label.place(x= 2, y = 370)
imp3_mess_label = tk.Label(content_frame1, text="Changing file types, need to be done in the keyword settings, that does also contain \nthe custom Checkbox, other Checkboxes cannot be changed and preset", font=("Helvetica", 8), justify="left", bg="#E6F7F8")
imp3_mess_label.place(x= 2, y = 390)

success_label = tk.Label(content_frame1, text="", font=("Helvetica", 8),  bg="#E6F7F8")
success_label.place(x= 2, y = 500)

####################################################################################################
#       input dir  
####################################################################################################

# Create an Entry widget
#entry = tk.Entry(frame1)
entry_dir = tk.Entry(frame1, width=30)
entry_dir2 = tk.Entry(frame1, width=30)

# Add the Entry widget to the root window
#entry.place(x= 1, y = 600)

#entry.bind("<Return>", process_text)

####################################################################################################
#       output dir
####################################################################################################

# Create a Button widget
button = tk.Button(frame1, text="Select Folder", command=select_folder)

# Add the Entry and Button widgets to the root window
button.place(x= 10, y = 130, width=100, height=20)

button2 = tk.Button(frame1, text="Select Folder", command=select_folder2)

button2.place(x= 10, y = 320, width=100, height=20)

submits = tk.Button(frame1, text="Submit",  bg="green", fg="white", command=submit)

submits.place(x= 120, y = 450, width=200, height=50)
#####################################################################################################
#       checkbox
#####################################################################################################



# Create the radio buttons
check_button1 = tk.Checkbutton(frame1, text="All", variable = checkbox_vars[0], onvalue="All", offvalue="0")
check_button2 = tk.Checkbutton(frame1, text="Documents", variable = checkbox_vars[1], onvalue="Doc", offvalue="0")
check_button3 = tk.Checkbutton(frame1, text="Pictures", variable = checkbox_vars[2], onvalue="Pic", offvalue="0")
check_button4 = tk.Checkbutton(frame1, text="Code", variable = checkbox_vars[3], onvalue="Cod", offvalue="0")
check_button5 = tk.Checkbutton(frame1, text="Application", variable = checkbox_vars[4], onvalue="App", offvalue="0")
check_button6 = tk.Checkbutton(frame1, text="Audio", variable = checkbox_vars[5], onvalue="Aud", offvalue="0")
check_button7 = tk.Checkbutton(frame1, text="web", variable = checkbox_vars[6], onvalue="web", offvalue="0")
check_button8 = tk.Checkbutton(frame1, text="zip", variable = checkbox_vars[7], onvalue="zip", offvalue="0")
check_button9 = tk.Checkbutton(frame1, text="Video", variable = checkbox_vars[8], onvalue="vid", offvalue="0")
check_button10 = tk.Checkbutton(frame1, text="Custom", variable = checkbox_vars[9], onvalue="cus", offvalue="0")


check_button1.deselect()
check_button2.deselect()
check_button3.deselect()
check_button4.deselect()
check_button5.deselect()
check_button6.deselect()
check_button7.deselect()
check_button8.deselect()
check_button9.deselect()
check_button10.deselect()


# Place the radio buttons and labels on the screen
check_button1.place(x=10, y=200)
#label1.place(x=140, y=200)
check_button2.place(x=60, y=200)
#label2.place(x=140, y=230)
check_button3.place(x=160, y=200)
check_button4.place(x=240, y=200)
check_button5.place(x=10, y=250)
check_button6.place(x=310, y=200)
check_button7.place(x=110, y=250)
check_button8.place(x=170, y=250)
check_button9.place(x=225, y=250)
check_button10.place(x=300, y=250)



checkbox_all.append(check_button1)
checkbox_all.append(check_button2)
checkbox_all.append(check_button3)
checkbox_all.append(check_button4)
checkbox_all.append(check_button5)
checkbox_all.append(check_button6)
checkbox_all.append(check_button7)
checkbox_all.append(check_button8)
checkbox_all.append(check_button9)
checkbox_all.append(check_button10)


####################################################################################################
#       checkbox checkup
####################################################################################################

def show():
    #myLabel = tk.Label(frame1, text = checkbox_vars[0].get()).pack()
    txt = ""
    for i in range(len(checkbox_vars)):
        if checkbox_vars[i].get() != "0":
            txt += checkbox_vars[i].get() + " "
            # print("Checkbox " + str(i) + " is checked")
    clicked_checkboxes_label.config(text = txt)
#label for checking which checkboxes where clicked
clicked_checkboxes_label = tk.Label(content_frame1, text="No checkboxes clicked", font=("Helvetica", 8),  bg="#E6F7F8")
clicked_checkboxes_label.place(x= 2, y = 450)


myButton = tk.Button(frame1, text = "Click Me!", command = show).place(x=10, y=470)

####################################################################################################
#      treeview functions
####################################################################################################
def delete_item(event):
    for selected_item in tree.selection():
        values = tree.item(selected_item)['values']
        type = values[0]
        print(type)
        folder = values[1]
        print(folder)
        tree.delete(selected_item)
        delt = db.delete_from_file(type, folder)
        print(delt)
        if delt == "Error: File type does not exist":
            pass
        else:
            pass




def insert_item(event):
    sel = []
    def klick_top(self):
        for j,i in enumerate(trie.selection()):
            sel.append(trie.item(i)['values'])
            db.add_to_file(sel[j][0], sel[j][1])
            print(f'sel {sel}')
        #close window
        #window.destroy()
        #enable main window
        #frame2.grab_release()
    
    window = tk.Toplevel(frame2, width=300, height=400)
    window.resizable(False, False)

    window.title("Insert")
    window.configure(bg="#E6F7F8")
    #disable minimize and maximize button
    window.attributes("-toolwindow", 1)
    #if window is open disable main window
    window.grab_set()
    window.focus_set()
    window.transient(frame2)
    trie = ttk.Treeview(window, columns=('file_type', 'folder_name'), show='headings')
    trie.heading('file_type', text='File Type')
    trie.heading('folder_name', text='Folder Name')
    trie.column('file_type', width=100)
    trie.column('folder_name', width=100)
    trie.place(x=10, y=10)
    
   
    #insert data into treeview
    with open(f"file_types/types_All.txt", "r") as file:     
        for line in file:
            (key, val) = line.split()
            trie.insert('', 'end', values=(key, val))
        
        
        
        frame2.grab_release()
        print(sel)
def activate_item(event):
    pass


def klick(event):
    selected_item = tree.selection()
    values = tree.item(selected_item)['values']
    #print(values)


    

####################################################################################################
#       treeview
####################################################################################################

tree = ttk.Treeview(frame2, columns=('file_type', 'folder_name', 'activation'), show='headings')

# Set the column headers
tree.heading('file_type', text='File Type')
tree.heading('folder_name', text='Folder Name')
tree.heading('activation', text='Activation')

# Set the column widths
tree.column('file_type', width=50)
tree.column('folder_name', width=50)
tree.column('activation', width=50)

# Hide the column with row numbers
#tree.column('#0', width=0, stretch='no')


with open(f"file_types/types_Cus.txt", "r") as file:     
    for i,line in enumerate(file):
        (key, val) = line.split()
        vals = tk.StringVar(value=0)
        check_file.append(vals.get())
        ch = tk.Checkbutton(tree, text="h", onvalue="1", offvalue="0")
        ch.deselect()
        check_file.append(ch)
        tree.insert('', 'end', values=(key, val, vals.get()))
        
        
        

tree.bind('<<TreeviewSelect>>', klick)

selected_item = tree.selection()
values = tree.item(selected_item)['values']
remove_button = tk.Button(frame2, text="Remove", command= lambda: delete_item(selected_item))
remove_button.place(x=10, y=500)
insert_button = tk.Button(frame2, text="New", command= lambda: insert_item(selected_item))
insert_button.place(x=65, y=500)
activate_button = tk.Button(frame2, text="Activate", command= lambda: activate_item(selected_item))
activate_button.place(x=105, y=500)

# insert_btt = tk.Button(window, text="Insert", command=trie.bind('<<TreeviewSelect>>', klick_top))
# insert_btt.place(x=10, y=350)

# Add multiple rows to the Treeview
# tree.insert('', 'end', values=('image', 'folder1', ''))
# tree.insert('', 'end', values=('video', 'folder2', 'False'))
# tree.insert('', 'end', values=('audio', 'folder3', 'True'))


#tree.add_widget(checkbox, 1, 2)

# Display the Treeview
tree.place(x=10, y=200, width=300, height=300)


# add a scrollbar
scrollbar = ttk.Scrollbar(frame2, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x=310, y=200, width=20, height=300)


####################################################################################################
#       end
####################################################################################################


# Start the event loop
root.mainloop()
