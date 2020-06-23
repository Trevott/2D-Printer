from tkinter import *
import RPi.GPIO as GPIO
from time import sleep

def rácsoz():
    for i in range (felbontásX):
        for j in range (felbontásY):
            x = i * rácsméret
            y = j * rácsméret
            can.create_rectangle(x, y, x+rácsméret, y+rácsméret, outline = 'lightgrey')

def click(event):
    for i in range (felbontásX - 1):
        if event.x >= i * rácsméret and event.x < (i + 1) * rácsméret:
            x = i * rácsméret
            break
    for j in range (felbontásY - 1):
        if event.y >= j * rácsméret and event.y < (j + 1) * rácsméret:
            y = j * rácsméret
            break

    if [x, y] in list:
        can.create_rectangle(x, y, x + rácsméret, y + rácsméret, outline = 'lightgrey', fill = 'white')
        list.remove([x, y])
    else:
        can.create_rectangle(x, y, x + rácsméret, y + rácsméret, outline = 'lightgrey', fill = 'lightgrey')
        list.append([x, y])
        
def clickRight(event):
    for i in range (felbontásX - 1):
        if event.x >= i * rácsméret and event.x < (i + 1) * rácsméret:
            x = i * rácsméret
            break
    for j in range (felbontásY - 1):
        if event.y >= j * rácsméret and event.y < (j + 1) * rácsméret:
            y = j * rácsméret
            break
    
    #előző kattintás x és y koordinátájának előhívása (utolsó elem kell, ezért végigjáratjuk)
    for step in list:
        lastX = step[0]
        lastY = step[1]
        
    #listához kell adni az összes két pont közötti pont koordinátáját
    if x == lastX:
        if y > lastY:
            i = lastY
            while i < y:
                can.create_rectangle(x, i, x + rácsméret, i + rácsméret, outline = 'lightgrey', fill = 'lightgrey')
                list.append([x, i])
                i = i + rácsméret
        else:
            i = lastY
            while i > y:
                can.create_rectangle(x, i, x + rácsméret, i + rácsméret, outline = 'lightgrey', fill = 'lightgrey')
                list.append([x, i])
                i = i -rácsméret
    elif y == lastY:
        if x > lastX:
            i = lastX
            while i < x:
                can.create_rectangle(i, y, i + rácsméret, y + rácsméret, outline = 'lightgrey', fill = 'lightgrey')
                list.append([i, y])
                i = i + rácsméret
        else:
            i = lastX
            while i > x:
                can.create_rectangle(i, y, i + rácsméret, y + rácsméret, outline = 'lightgrey', fill = 'lightgrey')
                list.append([i, y])
                i = i - rácsméret
        
        
def goToNextPoint(actXPos, targetXPos, actYPos, targetYPos):
    #irány a következő pont
    if (actXPos < targetXPos):
        i = actXPos / 15
        while i < targetXPos / 15:
            GPIO.output(a1, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a1, GPIO.LOW)
    
            GPIO.output(a2, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a2, GPIO.LOW)
    
            GPIO.output(a3, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a3, GPIO.LOW)
        
            GPIO.output(a4, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a4, GPIO.LOW)
            
            i = i + 1
    elif (actXPos > targetXPos):
        i = actXPos / 15
        while i > targetXPos / 15:   
            GPIO.output(a2, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a2, GPIO.LOW)
        
            GPIO.output(a1, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a1, GPIO.LOW)
        
            GPIO.output(a4, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a4, GPIO.LOW)
        
            GPIO.output(a3, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a3, GPIO.LOW)
                
            i = i - 1
            
    if (actYPos < targetYPos):
        i = actYPos / 15
        while i < targetYPos / 15:
            GPIO.output(b1, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b1, GPIO.LOW)
    
            GPIO.output(b2, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b2, GPIO.LOW)
    
            GPIO.output(b3, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b3, GPIO.LOW)
        
            GPIO.output(b4, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b4, GPIO.LOW)
            
            i = i + 1
    elif (actYPos > targetYPos):
        i = actYPos / 15
        while i > targetYPos / 15:   
            GPIO.output(b2, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b2, GPIO.LOW)
        
            GPIO.output(b1, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b1, GPIO.LOW)
        
            GPIO.output(b4, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b4, GPIO.LOW)
        
            GPIO.output(b3, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b3, GPIO.LOW)
                
            i = i - 1

def print():
    #rajzolás
    tempX = 0
    tempY = 0
    for step in list:
        if (step[0] >= tempX - (rácsméret + 1) and step[0] <= tempX + (rácsméret + 1)) and (step[1] >= tempY - (rácsméret + 1) and step[1] <= tempY + (rácsméret + 1)):
            #fej marad lent
            goToNextPoint(tempX, step[0], tempY, step[1])
        else:
            
            #fej felemelése
            #lift again the pencil
            servo.ChangeDutyCycle(3)
            sleep(0.5)
            servo.ChangeDutyCycle(0)
            
            goToNextPoint(tempX, step[0], tempY, step[1])
            
            #a fej leengedése...
            #let down the pencil
            servo.ChangeDutyCycle(5)
            sleep(0.5)
            servo.ChangeDutyCycle(0)
        
        tempX = step[0]
        tempY = step[1]
            
    #lift again the pencil
    servo.ChangeDutyCycle(3)
    sleep(0.5)
    servo.ChangeDutyCycle(0)
        
    #goin back to the nullpoint
    if (tempX > 0):
        i = tempX / 10#itt az osztó kisebb, hogy biztosan elérjük az alaphelyzetet
        while i > 0:   
            GPIO.output(a2, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a2, GPIO.LOW)
        
            GPIO.output(a1, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a1, GPIO.LOW)
        
            GPIO.output(a4, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a4, GPIO.LOW)
        
            GPIO.output(a3, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(a3, GPIO.LOW)
                
            i = i - 1
            
    if (tempY > 0):
        i = tempY / 10#itt az osztó kisebb, hogy biztosan elérjük az alaphelyzetet
        while i > 0:   
            GPIO.output(b2, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b2, GPIO.LOW)
        
            GPIO.output(b1, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b1, GPIO.LOW)
        
            GPIO.output(b4, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b4, GPIO.LOW)
        
            GPIO.output(b3, GPIO.HIGH)
            sleep(0.015)
            GPIO.output(b3, GPIO.LOW)
                
            i = i - 1

def delete():
    for i in range (felbontásX):
        for j in range (felbontásY):
            x = i * rácsméret
            y = j * rácsméret
            can.create_rectangle(x, y, x+10, y+10, outline = 'lightgrey', fill = 'white')

    list.clear()
    

if __name__ == '__main__': #program starts from here
    
    GPIO.setmode(GPIO.BCM)
    
    #Pins for motor driver inputs
    a1 = 27
    a2 = 5
    a3 = 17
    a4 = 22
    
    b1 = 6
    b2 = 26
    b3 = 13
    b4 = 19
    
    GPIO.setup(a3, GPIO.OUT) #All pins as output
    GPIO.setup(a4, GPIO.OUT)
    
    GPIO.setup(a1, GPIO.OUT) #All pins as output
    GPIO.setup(a2, GPIO.OUT)
    
    GPIO.setup(b3, GPIO.OUT) #All pins as output
    GPIO.setup(b4, GPIO.OUT)
    
    GPIO.setup(b1, GPIO.OUT) #All pins as output
    GPIO.setup(b2, GPIO.OUT)
    
    GPIO.setup(14, GPIO.OUT)
    servo = GPIO.PWM(14,50)
    
    #starting position
    servo.start(3)
    sleep(0.5)
    
    list = []
    rácsméret = 12
    felbontásX = 65
    felbontásY = 65
    
    ablak=Tk()
    can=Canvas(ablak,width=800,height=800,bg='white')
    can.bind("<Button-1>", click)
    can.bind("<Button-3>", clickRight)
    rácsoz()
    can.pack(side=LEFT)
    Button(ablak,text='Kilép',command=ablak.quit).pack(side=BOTTOM)
    Button(ablak,text='Nyomtatás',command=print).pack()
    Button(ablak,text='Töröl',command=delete).pack()
    ablak.mainloop()
