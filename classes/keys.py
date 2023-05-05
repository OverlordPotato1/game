import pygame


class Key:
    down = False
    tog = False
    prev = False
    turnedOn = False

    def __init__(self, keylist):
        if isinstance(keylist, int):
            keylist = [keylist]

        self.keylist = keylist
        

    def __fetch(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in self.keylist:
                self.down = True
        elif event.type == pygame.KEYUP:
            if event.key in self.keylist:
                self.down = False

    def __bool__(self):
        return self.down

    def __call__(self, event):
        self.__fetch(event)
        # if self.keylist[0] == pygame.K_k:
        #     print(self.down, self.prev)
    
    def x(self):
        self.prev = self.down
        
    def toggle(self):
        if self.down and not self.prev:
            self.tog != self.tog
        return self.tog

    def single(self):
        if self.down == True and self.prev == False:
            return True
        else:
            return False
