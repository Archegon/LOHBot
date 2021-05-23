import time
from game import game_control
from modules import Module
from position import Region, Point

# Coliseum Bot //Make checks for page
coliseum_bot = Module('Coliseum Bot', 14400)


def coliseum_bot_routine():
    world_b = Point(1496, 841, 1382, 763)
    coliseum_drag_start = Point(1496, 841, 1424, 344)
    coliseum_drag_end = Point(1496, 841, 651, 325)
    reward_b = Point(1496, 841, 1365, 700)
    reward_collect_b = Point(1496, 841, 462, 370)
    coliseum_check = Region(1496, 841, 278, 461, 1210, 659)
    enemy_b = Point(1495, 841, 544, 702)
    enemy_enter_b = Point(1495, 841, 671, 735)
    auto_b = Point(1495, 841, 368, 799)
    leave_check = Region(1495, 841, 380, 712, 544, 768)
    entered_battle_check = Region(1495, 841, 633, 707, 744, 755)
    coliseum_page_check = None

    game_control.add_drag('WorldToColiseum', coliseum_drag_start, coliseum_drag_end)

    world_b.click()
    time.sleep(2)
    game_control.drag('WorldToColiseum')
    coliseum_check.locate_click('coliseum')
    time.sleep(7)
    reward_b.click()
    time.sleep(2)
    reward_collect_b.click()
    game_control.back()
    time.sleep(3)

    while True:
        enemy_b.click()
        time.sleep(3)
        enemy_enter_b.click()
        time.sleep(20)

        if entered_battle_check.check_for('enter'):
            break

        auto_b.click()
        time.sleep(10)

        while not leave_check.check_for('leave'):
            time.sleep(1)

        leave_check.click()
        time.sleep(10)

    coliseum_bot.set_cooldown_time()
    game_control.back_to_main()


coliseum_bot.set_routine(coliseum_bot_routine)