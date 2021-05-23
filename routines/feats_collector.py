import time
from game import game_control
from modules import Module
from position import Region, Point

# Feats Collector
feats_collector = Module('Feats Collector', 3600)


def feats_collector_routine():
    feats_b = Point(1496, 841, 1070, 161)
    complete_check = Region(1496, 841, 1237, 237, 1400, 310)

    feats_b.click()

    while complete_check.check_for('complete'):
        complete_check.click()
        time.sleep(1)
        complete_check.click()
        time.sleep(0.5)

    feats_collector.set_cooldown_time()
    game_control.back_to_main()


feats_collector.set_routine(feats_collector_routine)