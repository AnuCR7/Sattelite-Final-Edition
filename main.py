import pgzrun
from random import randint
from time import time

WIDTH=800
HEIGHT=600

next_satellite=0
Satellitenumber=10
Sats= []
Lines=[]
starttime=0
totaltime=0

def Create_Satellite():
    global starttime,totaltime
    for i in range(Satellitenumber):
        Satellite=Actor('satellite')
        Satellite.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        Sats.append(Satellite)
    starttime=time()
    



def draw():
    global totaltime
    screen.clear()
    screen.blit('background',(0,0))
    Number=1
    for i in Sats:
        screen.draw.text(str(Number),(i.pos[0],i.pos[1]+20))
        i.draw()
        Number=Number+1
    for i in Lines:
        screen.draw.line(i[0],i[1],('white'))
    if next_satellite < Satellitenumber:
        totaltime=time() - starttime
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)



def update():
    pass
def on_mouse_down(pos):
    global next_satellite,Satellitenumber,Lines
    if next_satellite < Satellitenumber:
        if Sats[next_satellite].collidepoint(pos):
            if next_satellite:
                Lines.append((Sats[next_satellite-1].pos,Sats[next_satellite].pos))
            next_satellite=next_satellite+1
        else:
            Lines=[]
            next_satellite=0


                
                


    
Create_Satellite()
pgzrun.go()