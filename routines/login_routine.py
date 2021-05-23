import time
from modules import Module
from position import Region, Point
from game import game_control

# Login Module
login = Module('Login', start_only=True)


def login_routine():
    touch_to_start = Region(1637, 920, 582, 720, 1057, 820)
    touch_b = Point(1637, 920, 616, 517)

    while not game_control.at_page('Main'):
        if touch_to_start.check_for('touch to start'):
            touch_b.click()

    time.sleep(5)
    game_control.back_to_main()


login.set_routine(login_routine)
