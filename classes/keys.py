import pygame


class Key:
    def __init__(self, keylist):
        if isinstance(keylist, int):
            keylist = [keylist]

        self.keylist = keylist
        self.down = False

    def fetch(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in self.keylist:
                self.down = True
        elif event.type == pygame.KEYUP:
            if event.key in self.keylist:
                self.down = False

    def __bool__(self):
        return self.down

    def __call__(self, event):
        self.fetch(event)
