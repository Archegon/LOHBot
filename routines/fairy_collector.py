import time
from modules import Module
from position import Region, Point
from game import game_control

# Fairy Collector
fairy = Module('Fairy Collector', 300)


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
            fairy.set_cooldown_time(120)


fairy.set_routine(fairy_routine)
