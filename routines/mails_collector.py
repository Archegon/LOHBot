import time
from game import game_control
from modules import Module
from position import Region, Point

# Mail Collector
mails_collector = Module('Mails Collector', 1800)


def mails_collector_routine():
    mail_b = Point(1496, 841, 1322, 36)
    collect_check = Region(1496, 841, 1089, 273, 1232, 337)

    mail_b.click()

    while collect_check.check_for('free'):
        collect_check.click()
        time.sleep(35)
        game_control.back()

    while collect_check.check_for('accept'):
        collect_check.click()
        time.sleep(1)

    mails_collector.set_cooldown_time()
    game_control.back_to_main()


mails_collector.set_routine(mails_collector_routine)