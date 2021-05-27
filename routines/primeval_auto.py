import time
from modules import Module
from position import Region, Point
from game import game_control

# Auto Primeval Halls
auto_primeval = Module('Auto Primeval', 43200, timeout=1800)


def auto_primeval_routine():
    world_b = Point(1651, 928, 1540, 871)
    p_halls_b = Point(1651, 928, 326, 592)
    hall_t_b = Point(1651, 928, 938, 571)
    hall_e_b = Point(1651, 928, 1324, 487)
    ready_check = Region(1651, 928, 1183, 796, 1308, 839)
    enter_b = Point(1651, 928, 1164, 855)
    battle_outcome_check = Region(1651, 928, 759, 808, 917, 864)
    floor_list = [Point(1651, 928, 1214, 231), Point(1651, 928, 1205, 322), Point(1651, 928, 1207, 421), Point(1651, 928, 1201, 513), Point(1651, 928, 1200, 587)]

    world_b.click()
    time.sleep(3)
    p_halls_b.click()
    hall_t_b.click()

    for floor in floor_list:
        while not ready_check.check_for('ready'):
            pass

        floor.click()
        ready_check.click()
        time.sleep(3)

        if ready_check.check_for('ready'):
            auto_primeval.print('Cannot enter battle.')
            continue

        enter_b.click()
        time.sleep(60)

        while not battle_outcome_check.check_for('leave'):
            time.sleep(10)
            pass

        battle_outcome_check.click()
        time.sleep(3)

    auto_primeval.print('Going to experience hall.')
    game_control.back()
    time.sleep(5)
    hall_e_b.click()

    for floor in floor_list:
        while not ready_check.check_for('ready'):
            pass

        floor.click()
        ready_check.click()
        time.sleep(3)

        if ready_check.check_for('ready'):
            auto_primeval.print('Cannot enter battle.')
            continue

        enter_b.click()
        time.sleep(60)

        while not battle_outcome_check.check_for('leave'):
            time.sleep(10)
            pass

        battle_outcome_check.click()
        time.sleep(3)

    auto_primeval.set_cooldown_time()
    game_control.back_to_main()


auto_primeval.set_routine(auto_primeval_routine)
