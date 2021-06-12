import time
from game import game_control
from modules import Module
from position import Region, Point

raid_auto = Module('Raid Auto', 14400, timeout=1200)


def raid_auto_routine():
    world_b = Point(1651, 928, 1526, 821)
    raid_check = Region(1651, 928, 1367, 511, 1466, 547)
    start_b = Point(1651, 928, 1378, 851)
    ready_b = Point(1651, 928, 727, 848)
    battle_end_check = Region(1651, 928, 1290, 676, 1365, 716)
    after_b = Point(1651, 928, 1523, 814)
    start_check = Region(1651, 928, 1378, 831, 1496, 880)

    world_b.click()
    raid_check.click()
    time.sleep(2)
    start_check.click()

    if not start_check.check_for('start', filter_str=True, inside=True):
        # Raid available
        ready_b.click()
        # Wait for raid to end
        raid_auto.print('Waiting for raid to end')
        time.sleep(300)

        while not battle_end_check.check_for('tap'):
            time.sleep(5)

        battle_end_check.click()
        after_b.click()
        time.sleep(5)

        while not start_check.check_for('start'):
            time.sleep(2)

        start_check.click()
        ready_b.click()

        # Wait for raid to end
        raid_auto.print('Waiting for raid to end')
        time.sleep(180)

        while not battle_end_check.check_for('tap'):
            time.sleep(5)

        battle_end_check.click()
        after_b.click()
        time.sleep(5)
    else:
        raid_auto.print('Raid not available')


raid_auto.set_cooldown_time()
game_control.back_to_main()

raid_auto.set_routine(raid_auto_routine)
