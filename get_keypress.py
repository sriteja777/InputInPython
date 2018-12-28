from time import sleep

import keyboard

def getch_unix():
    """
    Get the singe character typed on terminal on Unix-based systems
    :return: Single character typed during game
    """
    import sys
    import tty
    import termios
    file_desc = sys.stdin.fileno()
    old_settings = termios.tcgetattr(file_desc)
    try:
        tty.setraw(sys.stdin.fileno())
        char1 = None
        char2 = None
        print(12)
        # sys.stdin.read(2)
        sleep(0.1)
        if keyboard.is_pressed('a'):
            char1 = 'a'
        if keyboard.is_pressed('s'):
            char2 = 's'
        if keyboard.is_pressed('q'):
            char1 = 'q'
    finally:
        termios.tcsetattr(file_desc, termios.TCSADRAIN, old_settings)
    return char1, char2


def run():
    while True:
        c,d = getch_unix()
        # sleep(0.01)
        if c is not None or d is not None:
            if c == 'q':
                break
            print(c, d)
            # pass

if __name__ == '__main__':
    run()
