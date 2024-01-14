import pytube
# # pytube is installed by this command : pip install pytube
try:
    video_url=input('Enter Url :  ')

    video_instance =pytube.YouTube(video_url)
    stream =video_instance.streams.get_highest_resolution()

# # starting the download
    stream.download()

except Exception as e:
    print(e)

#  ========== GUI VERSION ======================
import tkinter as tk
from tkinter import Entry,Button
from tkinter import messagebox
import pytube

def download():
    try:
        url=entry_url.get()
        video_instance =pytube.YouTube(url)
        stream =video_instance.streams.get_highest_resolution()

        # starting the download
        stream.download()
    except Exception as e:
         messagebox.showerror("Error", f"An error occured: {e}")



# creating the window
window= tk.Tk()
window.title("DownFlex 1.0/2024")
window.geometry("500x500")

# creating the widgets
label_url=tk.Label(window, text="Paste the URL to the video: ")
label_url.pack(pady=10)

entry_url=tk.Entry(window, width=50)
entry_url.pack(pady=10)

download_button= tk.Button(window, text="Download", command="download")
download_button.pack(pady=10)


# footer 
lbl1= tk.Label(window, text="Developed by Chipcode Technologies: ")
    # run the main loop
window.mainloop()