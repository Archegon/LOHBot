import time
from game import game_control
from modules import Module
from position import Point

# Alliance Collector
alliance = Module('Alliance Collector', 3600)


def alliance_routine():
    alliance_b = Point(1635, 920, 1307, 840)
    alliance_collect_b = Point(1635, 920, 1354, 817)

    if game_control.at_page('Main'):
        alliance_b.click()
        time.sleep(2)
        alliance_collect_b.click()
        time.sleep(1)
        game_control.back()
        alliance.set_cooldown_time()

    game_control.back_to_main()


alliance.set_routine(alliance_routine)
