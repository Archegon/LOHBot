import time
from modules import Module, ModuleManager
from position import Region, Point
from game import game_control


main_page_check = Region(1503, 845, 1345, 798, 1431, 825)
game_control.add_page('Main', 'world', main_page_check)
main_home_check = Region(1503, 845, 1022, 139, 1123, 170)
game_control.add_page('Main_Home', 'feats', main_home_check)
main_mystic_check = Region(1503, 845, 664, 239, 762, 278)
game_control.add_page('Main_Mystic', 'mystic', main_mystic_check)

# Drag to Main_mystic
# Set up drag start and end point
# Drag to mystic.
mystic_drag_start = Point(1503, 845, 1446, 334)
mystic_drag_end = Point(1503, 845, 67, 348)
game_control.add_drag('HomeToMystic', mystic_drag_start, mystic_drag_end)

# Drag to home.
home_drag_start = Point(1503, 845, 27, 81)
home_drag_end = Point(1503, 845, 1470, 90)
game_control.add_drag('MysticToHome', home_drag_start, home_drag_end)

# Set MAIN PAGE
quit_confirm_check = Region(1681, 945, 620, 421, 738, 466)
game_control.set_quit_confirmation('are you', quit_confirm_check)

# Login Module
login = Module('Login', start_only=True)


def login_routine():
    touch_to_start = Region(1637, 920, 582, 720, 1057, 820)
    touch_b = Point(1637, 920, 616, 517)

    while not game_control.at_page('Main'):
        if touch_to_start.check_for('touch to start'):
            touch_b.click()


login.set_routine(login_routine)


# Fairy Collector
fairy = Module('Fairy Collector', 1800)


def fairy_routine():
    # Set up button and region.
    fairy_status = Region(1514, 852, 721, 413, 816, 467)
    fairy_b = Point(1646, 926, 811, 524)  # Collect fairy gift button

    # Check if on home page.
    if game_control.at_page('Main_Home'):
        # Check if collectable.
        # If empty means collectable.
        if fairy_status.check_empty():
            fairy_b.click()
            fairy.print("Fairy gift collected")
            fairy.set_cooldown_time()
            time.sleep(1)
            game_control.back()
        else:
            fairy.print("No gift found.")


fairy.set_routine(fairy_routine)

module_manager = ModuleManager()
