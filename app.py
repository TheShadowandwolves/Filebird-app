import tkinter as tk

####################################################################################################
####################################################################################################

# Create the main window
root = tk.Tk()
root.resizable(width=False, height=False)  # make the window unresizeable

####################################################################################################
####################################################################################################

# Set the title of the window
root.title("File Bird v0.0.1")

# Set the size of the window
root.geometry("800x600")

####################################################################################################
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
####################################################################################################

# create a frame for the side menu
menu_frame = tk.Frame(root, width=200, height=600, bg="#FA8E36")
menu_frame.pack(side="left", fill="y")

####################################################################################################
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
####################################################################################################


# create a frame for the logo at the top of the side menu
logo_frame = tk.Frame(menu_frame, width=200, height=50, bg="#E6F7F8")
logo_frame.pack(side="top")

####################################################################################################
####################################################################################################

# add the logo to the logo frame (replace with your own logo)
logo = tk.PhotoImage(file="img/free Bird side.png")
logo_width = 285  # set the width of the logo to the width of the logo frame
logo_height = int(logo.height() * logo_width / logo.width())  # maintain the aspect ratio of the logo
logo = logo.subsample((logo.width() // logo_width)*2, (logo.height() // logo_height)*2)  # resize the logo
logo_label = tk.Label(logo_frame, image=logo, width=logo_width, height=logo_height)
logo_label.pack()

####################################################################################################
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
####################################################################################################

#raise frame0
change_to_frame0()

####################################################################################################
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
#####################################################################################################

#"Introducing FileBird - the revolutionary file organization tool that makes it easy to sort and manage your files. With FileBird, you can effortlessly organize your files into custom folders based on file type and name, so you can quickly find what you need when you need it. Say goodbye to cluttered and disorganized folders, and say hello to a new level of file organization and productivity with FileBird."
# add the text to the main content frame
main_text = "Introducing FileBird - the revolutionary file organization tool that makes it easy to sort and manage your files. With FileBird, you can effortlessly organize your files into custom folders based on file type and name, so you can quickly find what you need when you need it. Say goodbye to cluttered and disorganized folders, and say hello to a new level of file organization and productivity with FileBird."
main_label = tk.Label(content_frame, text=main_text, font=("Helvetica", 16),  bg="#E6F7F8", justify="left", anchor="nw", wraplength=400)
main_label.pack(padx=20, pady=20)


####################################################################################################
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
####################################################################################################








# Start the event loop
root.mainloop()
