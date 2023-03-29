from classes.keys import Key
import definitions


def create_movement_objects():
    return Key(definitions.UP_KEYS), Key(definitions.DOWN_KEYS), Key(definitions.LEFT_KEYS), Key(definitions.RIGHT_KEYS)


def create_base_window_size():
    return definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT
