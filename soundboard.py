import tkinter as tk
import playsound as p


def playsound(event):
    print(event)
    p.playsound("zapsplat_explosion_with_shockwave_designed_002_93119.mp3", False)

def playsounds(events):
    print(events)
    p.playsound('animals_dogs_x2_barking_small_001.mp3',False)

def playsounds1(events1):
    print(events1)
    p.playsound('zapsplat_impacts_metal_and_glass_box_drop_smash_break_010_108044.mp3',False)

def playsounds2(events2):
    print(events2)
    p.playsound('zapsplat_emergency_siren_personal_alarm_high_pitched_92571.mp3',False)

def playsounds3(events3):
    print(events3)
    p.playsound("zapsplat_bells_small_church_bell_chime_ring_12_92161.mp3",False)

win = tk.Tk()
win.attributes('-topmost',True)
win.geometry("400x150")


b = []
b.append(tk.Button(win,text="This button makes an explosion sound"))
b[0].bind("<Button>",playsound)

bb = []
bb.append(tk.Button(win,text= 'This is the sound a dog makes'))
bb[0].bind('<Button>',playsounds)

bbb = []
bbb.append(tk.Button(win,text='This is the sound of glass breaking'))
bbb[0].bind('<Button>',playsounds1)

bbbb = []
bbbb.append(tk.Button(win,text='This is the sound of an emergency siren/alarm'))
bbbb[0].bind('<Button>',playsounds2)

bbbbb = []
bbbbb.append(tk.Button(win,text='This is the sound of a church bell ringing'))
bbbbb[0].bind('<Button>', playsounds3)

for i in range(0,1):
    b[i].pack()
    bb[i].pack()
    bbb[i].pack()
    bbbb[i].pack()
    bbbbb[i].pack()

win.mainloop()