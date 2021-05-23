import time
from game import game_control
from modules import Module
from position import Region, Point

# Alchemy Collector
alchemy_collector = Module('Alchemy Collector', 72000)


def alchemy_collector_routine():
    alchemy_b = Point(1496, 841, 1293, 211)
    alchemy_left_b = Point(1496, 841, 629, 477)
    alchemy_free_check = Region(1496, 841, 826, 674, 950, 735)
    alchemy_confirm_b = Point(1496, 841, 749, 576)
    alchemy_drag_start = Point(1496, 841, 773, 579)
    alchemy_drag_end = Point(1496, 841, 228, 477)
    game_control.add_drag('Alchemy', alchemy_drag_start, alchemy_drag_end)
    alchemy_reveal_b = Point(1496, 841, 1427, 785)

    left_click_val = 3

    alchemy_b.click()

    if alchemy_free_check.check_for('free'):
        while left_click_val > 0:
            alchemy_left_b.click()
            time.sleep(1)
            left_click_val -= 1

        alchemy_free_check.click()
        alchemy_confirm_b.click()
        time.sleep(7)
        game_control.drag('Alchemy')
        time.sleep(10)
        alchemy_reveal_b.click()
        alchemy_collector.set_cooldown_time()
    else:
        alchemy_collector.set_cooldown_time(3600)

    game_control.back_to_main()


alchemy_collector.set_routine(alchemy_collector_routine)