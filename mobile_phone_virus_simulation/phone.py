import pygame
import random
import threading
import sys 
import time
import math 
from collections import deque 


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
repair_lock = threading.Lock()


class Phone(threading.Thread):
    """
    Class to represent a phone in the simulation.
    """

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color = WHITE
        self.infected = False
        self.lifespan = 500
        self.repairing = False

    def isinfected(self,other):
        # print(pow(self.x-other.x,2)+pow(self.y-other.y,2))
        if pow(self.x-other.x,2)+pow(self.y-other.y,2) <= 10000 : return True 
        return False 


    # def infect(self):
    #     """
    #     Method to infect the phone.
    #     """
    #     self.infected = True
    #     self.color = RED

    def repair(self):
        """
        Method to repair the phone.
        """
        # Acquire the lock to ensure only one phone is in the repair shop
        with repair_lock:
            
            if self.repairing:
                return
            self.repairing = True
            
            self.color = GREEN
            self.repairing = False
            self.infected = False

# repair function should be synchronus because we want to repair one phone at a time 