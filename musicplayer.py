from tkinter import *
import tkinter.messagebox as tmsg
from pygame import mixer
from PIL import Image,ImageTk
from tkinter import filedialog
import os
mixer.init()
def play():
    global musicfile
    musicfile=music_playlist.get(ANCHOR)
    if musicfile!="":
      mixer.music.load(musicfile)
    else:
        musicfile=filedialog.askopenfilename()
        dirlen=len(os.path.dirname(musicfile))
        mixer.music.load(musicfile)
        play_music.config(text=f"Currently playing {musicfile[dirlen+1:]}")
    mixer.music.play(-1)
    
def stop():
    mixer.music.stop()
def pause():
    if mixer.music.get_busy():
        mixer.music.pause()
    else:
        mixer.music.unpause()
       
def forward():
    current_pos=mixer.music.get_pos()+10
    print(current_pos)
    mixer.music.set_pos(current_pos)
def addtoplaylist():
    if mixer.music.get_busy():
        dirlen=len(os.path.dirname(musicfile))
        for music in music_playlist.get(0,END):
            if music==musicfile[dirlen+1:]:
                tmsg.showinfo("My Music player","Already added to playlist")
                return
        music_playlist.insert(END,musicfile[dirlen+1:])
        tmsg.showinfo("My Music Player","Music added to your playlist")
def submit():
    rating=my_rating.get()
    print(rating)

def onSelect(evt):
    print("delete me")
    w = evt.widget
    index = int(w.curselection()[0])
    w.delete(index)
window=Tk()
window.geometry("644x434")
window.title("My Music Player")
window.resizable(False,False)
musicbg=Image.open(r"C:\Users\HP\Downloads\pexels-daniel-reche-3721941.jpg").resize((644,434))
f1=Frame()
musicphoto=ImageTk.PhotoImage(musicbg)
music_label=Label(f1,image=musicphoto)
music_label.pack(side=TOP,anchor="nw",fill="both")
play_music=Label(f1,anchor="nw",fg="red",text="Play some music!")
play_music.place(relx=0.1,rely=0.1)
selectmusic=Button(f1,anchor="nw",fg="red",text="Select music to play",command=play) 
selectmusic.place(relx=0.1,rely=0.2)
playmusic=Button(f1,anchor="nw",fg="red",image="",command=play) 
playmusic.place(relx=0.1,rely=0.3)
stopmusic=Button(f1,fg="red",text="Stop",command=stop) 
stopmusic.place(relx=0.1,rely=0.4)
pausemusic=Button(f1,fg="red",text="Pause",command=pause) 
pausemusic.place(relx=0.1,rely=0.5)

forwardmusic=Button(f1,fg="red",text="Forward",command=forward) 
forwardmusic.place(relx=0.1,rely=0.6)
addtofav=Button(f1,fg="red",text="Add to fav",command=addtoplaylist) 
addtofav.place(relx=0.1,rely=0.7)
plylist_text=Label(text="My PlayList",fg="red")
plylist_text.place(relx=0.75,rely=0.23)
music_playlist=Listbox(f1)
music_playlist.bind("<<ListboxSelect>>",onSelect)
music_playlist.place(relx=0.65,rely=0.3,width=150)
gif=PhotoImage(file="5uwq.gif",format="gif -index 2",height="20",width="50")
music_playing=Label(f1,image=gif)
music_playing.pack(side=BOTTOM,anchor="sw")
my_rating=Scale(f1,from_=0,to=5,orient=HORIZONTAL,tickinterval=1)
my_rating.place(relx=0.1,rely=0.7)
submit_rating=Button(window,anchor="nw",text="Submit Feedback",command=submit)
submit_rating.place(relx=0.1,rely=0.85)

f1.pack()

window.mainloop()