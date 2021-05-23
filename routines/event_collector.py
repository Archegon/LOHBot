import time
from game import game_control
from modules import Module
from position import Region, Point

# Event Collector NEEDS UPDATE
event_collector = Module('Event Collector', 7200)


def event_collector_routine():
    event_b = Point(1496, 841, 99, 242)
    random_b = Point(1496, 841, 1389, 786)
    event_b_list = [Point(1496, 841, 125, 101), Point(1496, 841, 147, 219), Point(1496, 841, 145, 327)]
    event_txt_check = Region(1496, 841, 419, 93, 1134, 198)
    login_b_list = [Point(1496, 841, 1348, 573), Point(1496, 841, 1144, 561), Point(1496, 841, 967, 574),
                    Point(1496, 841, 765, 596), Point(1496, 841, 587, 556), Point(1496, 841, 389, 551)]
    ptu_b_list = [Point(1496, 841, 1017, 500), Point(1496, 841, 870, 649), Point(1496, 841, 732, 504),
                  Point(1496, 841, 581, 655), Point(1496, 841, 444, 494)]
    energetic_b_list = [Point(1496, 841, 1039, 511), Point(1496, 841, 843, 645), Point(1496, 841, 699, 484),
                        Point(1496, 841, 566, 632), Point(1496, 841, 428, 471)]

    check_string = ['login event', 'paid to upgrade_', 'energetic efforts']

    event_b.click()
    time.sleep(5)

    for event_1_b in event_b_list:
        event_1_b.click()
        time.sleep(1)

        for check in check_string:
            if event_txt_check.check_for(check):
                if check == 'login event':
                    for login_b in login_b_list:
                        login_b.click()
                        time.sleep(1)

                    random_b.click()
                    time.sleep(2)
                elif check == 'paid to upgrade_':
                    for ptu_b in ptu_b_list:
                        ptu_b.click()
                        time.sleep(1)

                    random_b.click()
                    time.sleep(2)
                elif check == 'energetic efforts':
                    for energetic_b in energetic_b_list:
                        energetic_b.click()
                        time.sleep(1)

                    random_b.click()
                    time.sleep(2)

    event_collector.set_cooldown_time()
    game_control.back_to_main()


event_collector.set_routine(event_collector_routine)