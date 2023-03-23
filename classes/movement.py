

class Movement:
    def __init__(self, animation_class, left_walk, right_walk, move_speed):
        self.animation_class = animation_class
        self.leftWalk = left_walk
        self.rightWalk = right_walk
        self.last_direction = 0
        self.move_speed = move_speed

    def __call__(self, up, down, left, right, scroll_x, scroll_y):
        succeed = 0
        ms = self.move_speed
        if up and not down:
            scroll_y += ms
            succeed += 1
        if down and not up:
            scroll_y -= ms
            succeed += 1
        if left and not right:
            scroll_x += ms
            if self.last_direction == 0:
                self.animation_class.switch_sheet(self.leftWalk)
                self.last_direction = 1
            succeed += 1
        if right and not left:
            scroll_x -= ms
            if self.last_direction == 1:
                self.animation_class.switch_sheet(self.rightWalk)
                self.last_direction = 0
            succeed += 1
        if succeed == 0:
            self.animation_class.ticks_since = 18

        return scroll_x, scroll_y
