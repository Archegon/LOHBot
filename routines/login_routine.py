import time
from modules import Module
from position import Region, Point
from game import game_control
from routines.routines_setup import module_manager

# Login Module
login = Module('Login', start_only=True)


def login_routine():
    touch_to_start = Region(1637, 920, 582, 720, 1057, 820)
    touch_b = Point(1637, 920, 616, 517)

    start_time = time.time()
    time_out = 300
    kill_game = False

    while not game_control.at_page('Main'):
        if touch_to_start.check_for('touch to start'):
            touch_b.click()

        if time.time() - start_time >= time_out:
            kill_game = True
            break

    if not kill_game:
        time.sleep(5)
        game_control.back_to_main()
    else:
        module_manager.stop = True
        game_control.kill_program()


login.set_routine(login_routine)
