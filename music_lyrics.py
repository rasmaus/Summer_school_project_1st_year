
import tkinter as tk
from tkinter import *
from lyrics_extractor import SongLyrics

window = Tk()  
window.geometry('600x600')  
window.title('music_lyrics')  

head = Label(window, text="Enter the song you want Lyrics for", font=('Calibri 15'))  
head.pack(pady=20)

song = tk.StringVar()  
result = tk.StringVar()

def get_lyrics():
    song_name = song.get()  
    api_key = "AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg"
    engine_id = "aa2313d6c88d1bf22"
    extract_lyrics = SongLyrics(api_key, engine_id)  
    song_lyrics = extract_lyrics.get_lyrics(song_name)  
    
    
    with open("vivek.txt", "w", encoding="utf-8") as file:
        file.write(song_lyrics['lyrics'])
    
    
    with open("vivek.txt", "r", encoding="utf-8") as file:
        k = file.readlines()
        content = ''.join(k)
        
   
    text_widget.config(state=NORMAL) 
    text_widget.delete(1.0, END)  
    text_widget.insert(END, content)  
    text_widget.tag_add('center', 1.0, 'end')  
    text_widget.config(state=DISABLED)  

Entry(window, textvariable=song).pack()  
Button(window, text="GO", command=get_lyrics).pack()

frame = Frame(window)
frame.pack(fill=BOTH, expand=1)


text_widget = Text(frame, wrap='word', bg="light grey", font=20)
scrollbar = Scrollbar(frame, command=text_widget.yview)
text_widget.configure(yscrollcommand=scrollbar.set)


scrollbar.pack(side=RIGHT, fill=Y)
text_widget.pack(side=LEFT, fill=BOTH, expand=1)


text_widget.tag_configure('center', justify='center')


text_widget.config(state=DISABLED)

window.mainloop()

