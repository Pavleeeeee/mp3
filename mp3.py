from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os
import random

mixer.init()

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))
    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()
    status.set(f"Playing: {songs_list.get(ACTIVE)}")
def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")
def load(listbox):
    directory = filedialog.askdirectory(title='Open a songs directory')
    if directory:
        os.chdir(directory)
        tracks = [track for track in os.listdir() if track.endswith('.mp3')]
        for track in tracks:
            listbox.insert(END, track)
def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")
def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")
def skip_song(status: StringVar, songs_list: Listbox):
    current_index = songs_list.curselection()
    if current_index:
        next_index = (current_index[0] + 1) % songs_list.size()
        song_name.set(songs_list.get(next_index))
        mixer.music.load(songs_list.get(next_index))
        mixer.music.play()
        status.set(f"Playing: {songs_list.get(next_index)}")
def previous_song(status: StringVar, songs_list: Listbox):
    current_index = songs_list.curselection()
    if current_index:
        prev_index = (current_index[0] - 1) % songs_list.size()
        song_name.set(songs_list.get(prev_index))
        mixer.music.load(songs_list.get(prev_index))
        mixer.music.play()
        status.set(f"Playing: {songs_list.get(prev_index)}")
def shuffle_and_play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    songs = list(songs_list.get(0, END))
    if songs:
        random_song = random.choice(songs)
        song_name.set(random_song)
        mixer.music.load(random_song)
        mixer.music.play()
        status.set(f"Playing random song: {random_song}")
    else:
        status.set("Playlist is empty")

root = Tk()
root.geometry('1000x220') 
root.title('MP3 PLAYER')
root.resizable(0, 0)

song_frame = LabelFrame(root, text='Current Song', bg='RoyalBlue', width=700, height=80) 
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', bg='RoyalBlue', width=1000, height=120)  
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue')
listbox_frame.place(x=700, y=0, height=200, width=300)

song_name = StringVar(root, value='<Not selected>')
song_status = StringVar(root, value='<Not Available>')

playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold', bg='#3A3A3A', fg='white', selectmode=SINGLE)
playlist.pack(fill=BOTH, padx=5, pady=5, expand=True)

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL, bg='#3A3A3A')
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)

Label(song_frame, text='CURRENTLY PLAYING:', bg='RoyalBlue', font=('Times', 10, 'bold')).place(x=5, y=20)
song_lbl = Label(song_frame, textvariable=song_name, bg='Goldenrod', font=("Times", 12), width=40)
song_lbl.place(x=150, y=20)

pause_btn = Button(button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=7, command=lambda: pause_song(song_status))
pause_btn.place(x=15, y=10)

stop_btn = Button(button_frame, text='Stop', bg='Aqua', font=("Georgia", 13), width=7, command=lambda: stop_song(song_status))
stop_btn.place(x=100, y=10)

play_btn = Button(button_frame, text='Play', bg='Aqua', font=("Georgia", 13), width=7, command=lambda: play_song(song_name, playlist, song_status))
play_btn.place(x=185, y=10)

resume_btn = Button(button_frame, text='Resume', bg='Aqua', font=("Georgia", 13), width=7, command=lambda: resume_song(song_status))
resume_btn.place(x=270, y=10)

skip_btn = Button(button_frame, text='Skip Song', bg='Aqua', font=("Georgia", 13), width=10, command=lambda: skip_song(song_status, playlist))
skip_btn.place(x=355, y=10)

previous_btn = Button(button_frame, text='Previous', bg='Aqua', font=("Georgia", 13), width=10, command=lambda: previous_song(song_status, playlist))
previous_btn.place(x=470, y=10)

shuffle_btn = Button(button_frame, text='Shuffle', bg='Aqua', font=("Georgia", 13), width=10, command=lambda: shuffle_and_play_song(song_name, playlist, song_status))
shuffle_btn.place(x=585, y=10)

load_btn = Button(button_frame, text='Load Directory', bg='Aqua', font=("Georgia", 13), width=68, command=lambda: load(playlist))
load_btn.place(x=10, y=55)

Label(root, textvariable=song_status, bg='SteelBlue', font=('Times', 9), justify=LEFT).pack(side=BOTTOM, fill=X)

root.update()
root.mainloop()

