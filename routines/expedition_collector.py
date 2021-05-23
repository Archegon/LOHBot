import time
from game import game_control
from modules import Module
from position import Region, Point

# Expedition Collector
expedition_collector = Module('Expedition Collector', 10800)


def expedition_collector_routine():
    world_b = Point(1496, 841, 1384, 766)
    option_1_b = Point(1496, 841, 1237, 748)
    complete_check = Region(1496, 841, 1329, 596, 1446, 621)
    yes_check = Region(1496, 841, 845, 554, 928, 605)
    exped_b = Point(1496, 841, 1411, 767)
    hard_b = Point(1496, 841, 783, 179)
    auto_select_b = Point(1496, 841, 946, 772)
    dispatch_b = Point(1496, 841, 1270, 766)
    dispatch_confirm_b = Point(1496, 841, 907, 593)

    world_b.click()

    if complete_check.check_for('completel'):
        while complete_check.check_for('completel'):
            complete_check.click()
            time.sleep(3)

            if yes_check.check_for('yes'):
                yes_check.click()
                time.sleep(5)
                game_control.back()
                time.sleep(1)
                break

            option_1_b.click()
            time.sleep(3)
            game_control.back()
            time.sleep(1)

        exped_b.click()
        hard_b.click()
        auto_select_b.click()
        dispatch_b.click()
        dispatch_confirm_b.click()
        expedition_collector.set_cooldown_time()
        time.sleep(10)
    else:
        expedition_collector.set_cooldown_time(3600)

    game_control.back_to_main()


expedition_collector.set_routine(expedition_collector_routine)