'''
Script containing the animation class and functions for scrolling the screen
'''
import pygame
import os
import asyncio
from player import player

class animation:
    def __init__(self, screen, walking, attack, death, idle):
        '''
        Constructor for the animation class
        
        Args:
            screen: the screen to draw the animation on
            walking: a list of sprites for the walking animation
            attack: a list of sprites for the attack animation
            death: a list of sprites for the death animation
            idle: a list of sprites for the idle animation
        
        Returns:
            None
            
        Raises:
            None
            
        Example:
            animation = animation(walking, attack, death, idle)
        '''
        self.walk = walking
        self.attack = attack
        self.death = death
        self.idle = idle
        self.screen = screen
        self.active = None
        self.activeString = None

    def __walk(self):
        '''
        Plays the walking animation
        
        Args:
            None
            
        Returns:
            None
            
        Raises:
            None
            
        Example:
            animation._walk()
        '''
        while True:
            for sprite in self.walk:
                self.screen.blit(sprite, (0, 0))
                pygame.display.flip()
                pygame.time.delay(100)

    def __attack(self):
        '''
        Plays the attack animation
        
        Args:
            None
            
        Returns:
            None
            
        Raises:
            None
            
        Example:
            animation._attack()
        '''
        for sprite in self.attack:
            self.screen.blit(sprite, (0, 0))
            pygame.display.flip()
            pygame.time.delay(100)
        
    def __death(self):
        '''
        Plays the death animation
        
        Args:
            None
            
        Returns:
            None
            
        Raises:
            None
            
        Example:
            animation._death()
        '''
        for sprite in self.death:
            self.screen.blit(sprite, (0, 0))
            pygame.display.flip()
            pygame.time.delay(100)

    def __idle(self):
        '''
        Plays the idle animation
        
        Args:
            None
            
        Returns:
            None
            
        Raises:
            None
            
        Example:
            animation._idle()
        '''
        while True:
            for sprite in self.idle:
                self.screen.blit(sprite, (0, 0))
                pygame.display.flip()
                pygame.time.delay(100)

    def play(self, animation, loop = True):
        '''
        Plays an animation
        
        Args:
            animation: the animation to play
            loop: whether or not to loop the animation
            
        Returns:
            None
            
        Raises:
            None
            
        Example:
            animation._play("walk", True)
        '''
        # if the animation is already playing, don't play it again
        if self.activeString == animation:
            return
        # if there is an animation playing, stop it
        if animation == "walk":
            # start the walk animation in a new thread that can be terminated
            self.activeString = "walk"
            self.active = asyncio.create_task(self.__walk())
        elif animation == "attack":
            # start the attack animation in a new thread that can be terminated
            self.active = asyncio.create_task(self.__attack())
            self.activeString = "attack"
        elif animation == "death":
            # start the death animation in a new thread that can be terminated
            self.active = asyncio.create_task(self.__death())
            self.activeString = "death"
        elif animation == "idle":
            # start the idle animation in a new thread that can be terminated
            self.activeString = "idle"
            self.active = asyncio.create_task(self.__idle())
            
        return

async def __player_move(self, direction):
    '''
    Moves the player in a direction
    
    Args:
        direction: a tuple with the x and y direction to move in
        
    Returns:
        None
        
    Raises:
        None
        
    Example:
        __player_move((0, 1))
    '''

    player.move(direction)

async def __world_move(self, direction):
    '''
    Moves the world in a direction
    
    Args:
        direction: a tuple with the x and y direction to move in
        
    Returns:
        None
        
    Raises:
        None
        
    Example:
        __world_move((0, 1))
    '''

    # delay the world movement so that the player will move away
    await asyncio.sleep(0.5)

    ##################################################################### this will need actual code when the game exists
    

def scrolling(self, direction):
    '''
    Scrolls the screen in a direction
    Delays the camera movement so that the player will move away using asyncio
    
    Args:
        direction: a tuple with the x and y direction to scroll in

    Returns:    
        None

    Raises:
        None

    Example:
        scrolling((0, 1))
    '''

    # call __world_move and __player_move without waiting for them to finish
    asyncio.create_task(self.__world_move(direction))
    asyncio.create_task(self.__player_move(direction))
