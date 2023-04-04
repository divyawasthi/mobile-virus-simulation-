import pygame 
import random 
import time 
import sys 
import math 
from phone import Phone 


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


PHONE_WIDTH = 10
PHONE_HEIGHT = 10
pygame.init()
size = width, height = 790, 590
screen = pygame.display.set_mode(size)
flag = True  ; write=False 
coordinates = []
ifx,ify = -1,-1 ; start_infection = False 
infection_started = False 
infected = []
to_be_repaired = set()
temp = None 
while True : 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : sys.exit()
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_v : 
                if not start_infection and len(coordinates): 
                    ind = random.randint(0,len(coordinates)-1)
                    temp = coordinates[ind]
                    coordinates[ind].infected = True 
                    infected_phone = coordinates[random.randint(0,len(coordinates)-1)]
                    ifx,ify = infected_phone.x,infected_phone.y 
                    coordinates[ind].color = RED
                    to_be_repaired.add(temp)
                    infected.append(infected_phone)
                    infection_started = True 
                    start_infection = True 
                    
            if event.key == pygame.K_UP : 
                cflag = False 
                while True : 
                    x,y = random.randint(10,780),random.randint(10,590)

                    if len(coordinates) > 1 : 
                        for obj in coordinates: 
                            if obj.x == x and obj.y == y :cflag=True; break 
                    
                    if len(coordinates) == 0 or not cflag : 
                        phone = Phone(x,y)
                        coordinates.append(phone)
                        break 
            
                                            

    screen.fill(pygame.Color(BLACK))
    if not infection_started : 
        for obj in coordinates : pygame.draw.rect(screen,(pygame.Color(obj.color)),pygame.Rect(obj.x,obj.y,PHONE_HEIGHT,PHONE_WIDTH))
    if infection_started : 
        for obj in coordinates : 
            pygame.draw.rect(screen,pygame.Color(obj.color),pygame.Rect(obj.x,obj.y,10,10))
        for val in coordinates : 
            if not val.infected : continue 
            temp = val 
            for v in coordinates : 
                if v.infected  : continue 
        
                if temp.isinfected(v) : v.infected = True ; v.color = RED 
        
        for coordinate in coordinates : 
            if coordinate.infected : 
                coordinate.repair()
                pygame.time.delay(10)
                break 
        for coordinate in coordinates : 
            if coordinate.infected : 
                coordinate.lifespan -= 1

                if coordinate.lifespan == 0 : 
                    coordinates.remove(coordinate)
                    pygame.time.delay(10)
                    
        

                 
    pygame.display.update()
    
