import tkinter as tk
from tkinter import ttk,PhotoImage,filedialog,Menu
import os
import pygame
import time



window=tk.Tk()
menubar=Menu(window)
window.config(menu=menubar)
submenu=Menu(menubar)

paused=False



current_positon=0

current_song=None
 
def choose_song():
    global current_song
    song_path=filedialog.askopenfilename(initialdir='.',title='Bir şarkı seçini',filetypes=(('MP3 Files','.mp3'),))
    
    çal_müzik(song_path)
    
    

window.title('PLAYASH')
window.geometry('700x846')
window.iconbitmap('C:/Users/Nuray/Downloads/rapper_AWB_icon.ico')
window.config(bg='black')

pygame.mixer.init()


def çal_müzik(song_path):
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused=False
    
    else:
        song_path=filedialog.askopenfilename()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    
    
    
    
        
def pause_müzik():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused=True
        


def stop_müzik():
    pygame.mixer.music.stop()
    

    
   
    
    
    


def set_vol(val):
    volume=int(val)/100
    pygame.mixer.music.set_volume(volume)
    
    
    
    muted=False

    
    
def mute_müzik():
    global muted
    if muted:
        pygame.mixer.music.set_volume(0.7)
        volume_buton.configure(image=volume_icon)
        scale.set(50)
        muted=False
    else:
        pygame.mixer.music.set_volume(0)
        volume_buton.configure(image=mute_icon)
        scale.set(0)
        muted=True
    



    

label=tk.Label(window,text='PLAYASH',font=('Verdana',20),bg='grey')
label.pack()

image=tk.PhotoImage(file='C:/Users/Nuray/Desktop/image/albüm.png')
label=tk.Label(window,image=image,bg='black')
label.pack(side=tk.LEFT)
middleframe=tk.Frame(window)
middleframe.pack(padx=10,pady=10)

seç_buton=tk.Button(window,text='Şarkı Seç',font=('Verdana',16),command=choose_song)
seç_buton.pack(side=tk.LEFT,padx=10)


play_icon=tk.PhotoImage(file='C:/Users/Nuray/Desktop/başlat2.png')
çal_buton=tk.Button(window,image=play_icon,command=lambda:çal_müzik(current_song))
    
çal_buton.pack(side=tk.LEFT,padx=10)


durdur_icon=tk.PhotoImage(file='C:/Users/Nuray/Desktop/durdur2.png')
durdur_buton=tk.Button(window,image=durdur_icon,command=pause_müzik)
durdur_buton.pack(side=tk.LEFT,padx=10)

stop_icon=tk.PhotoImage(file='C:/Users/Nuray/Desktop/stop1.png')
stop_buton=tk.Button(window,image=stop_icon,command=stop_müzik)
stop_buton.pack(side=tk.LEFT,padx=10)

mute_icon=tk.PhotoImage(file='C:/Users/Nuray/Desktop/mute1.png')

volume_icon=tk.PhotoImage(file='C:/Users/Nuray/Desktop/volume.png')
volume_buton=tk.Button(window,image=volume_icon,command=mute_müzik)
volume_buton.pack(side=tk.LEFT)



scale=tk.Scale(window,from_=0,to=100,orient='horizontal',length=200,command=set_vol)
scale.set(50)
pygame.mixer.music.set_volume(0.7)
scale.pack(pady=15,side=tk.LEFT)






window.mainloop()