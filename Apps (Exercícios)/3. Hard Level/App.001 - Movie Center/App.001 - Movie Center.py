import os
import ttkbootstrap as ttkb
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk


# Function to get the movie files from a directory
def get_movie_files(directory):
    movie_files = []
    for file in os.listdir(directory):
        if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mkv'):
            movie_files.append(file)
    return movie_files

# Function to display the movie list in the GUI
def display_movie_list(directory):
    movie_files = get_movie_files(directory)
    for i in range(len(movie_files)):
        # Display the movie poster image
        poster_path = os.path.join(directory, movie_files[i].replace('.mp4', '.jpg'))
        if not os.path.exists(poster_path):
            poster_path = 'no-image.jpg'
        poster_image = Image.open(poster_path)
        poster_image = poster_image.resize((150, 200), Image.ANTIALIAS)
        poster = ImageTk.PhotoImage(poster_image)
        label = ttkb.Label(movie_frame, image=poster)
        label.image = poster
        label.grid(row=0, column=i, padx=10, pady=10)

        # Display the movie title
        title = movie_files[i].replace('.mp4', '').replace('_', ' ')
        title_label = ttkb.Label(movie_frame, text=title, font=('Arial', 8))
        title_label.grid(row=1, column=i, padx=10, pady=10)

        # Display the movie play button
        play_button = ttkb.Button(movie_frame, text='Play', command=lambda movie_file=movie_files[i]: play_movie(movie_file))
        play_button.grid(row=2, column=i, padx=10, pady=10)

    # Create horizontal scrollbar for scrolling through the movies
    #scrollbar = Scrollbar(principal, orient='horizontal', xscrollcommand=scrollbar.set, command=movie_frame.xview)
    #scrollbar.pack(side='bottom', fill='x')
    #movie_frame.config()



# Function to browse for a directory containing movie files
def browse_directory():
    global directory, movie_frame
    directory = filedialog.askdirectory()
    if directory:
        movie_frame.destroy()
        movie_frame = ttkb.Frame(canvas)
        movie_frame.pack(padx=20, pady=20)
        display_movie_list(directory)


# Function to display the selected movie
def play_movie(movie_file):
    try:
        # Use the subprocess module to open the movie file in the default media player
        subprocess.Popen([os.path.join(directory, movie_file)], shell=True)
    except Exception as e:
        messagebox.showerror('Error', str(e))


principal = ttkb.Window(themename="darkly")
principal.title('Movie Center')
principal.iconbitmap('./img/mvredicon.ico')
principal.geometry('700x500')

#Barra de rolagem

canvas = Canvas(principal, width=700, height=500)
canvas.pack(padx=10, pady=10, expand=True, fill='both')
barra = Scrollbar(canvas, orient=HORIZONTAL)
barra.config(command=canvas.xview())
barra.pack(side='bottom', fill=X)


# Button Style
browse_button_style = ttkb.Style()
browse_button_style.configure('danger.Outline.TButton', font=('Helvetica', 18))

# Create the browse button
browse_button = ttkb.Button(canvas, text='Procurar', bootstyle='danger-outline', style='danger.Outline.TButton',
                            command=browse_directory, width=30)
browse_button.pack(pady=20)

# Create the movie frame
movie_frame = ttkb.Frame(principal)
movie_frame.pack(padx=20, pady=20)


principal.mainloop()
