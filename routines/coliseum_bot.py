import time
from game import game_control
from modules import Module
from position import Region, Point

# Coliseum Bot
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
    coliseum_page_check = Region(1649, 928, 543, 541, 676, 579)
    auto_b_check = Region(1649, 928, 381, 862, 425, 897)

    game_control.add_drag('WorldToColiseum', coliseum_drag_start, coliseum_drag_end)

    world_b.click()
    time.sleep(2)
    game_control.drag('WorldToColiseum')
    coliseum_check.locate_click('coliseum')
    time.sleep(7)

    if coliseum_page_check.check_for('defense'):
        while True:
            coliseum_bot.print('Waiting for Coliseum page.')
            while not coliseum_page_check.check_for('defense'):
                time.sleep(2)

            if coliseum_page_check.check_for('defense'):
                coliseum_bot.print('Attempting to start battle.')
                enemy_b.click()
                time.sleep(5)
                enemy_enter_b.click()
                time.sleep(5)

                # If did not enter battle
                if entered_battle_check.check_for('enter'):
                    coliseum_bot.print('No more battles. Exiting')
                    break

                # Loading Screen
                coliseum_bot.print('Waiting for battle start.')
                while not auto_b_check.check_for('A', filter_str=True, inside=True):
                    time.sleep(2)

            coliseum_bot.print('In battle.')
            time.sleep(2)
            auto_b.click()
            time.sleep(10)
            coliseum_bot.print('Waiting for battle end.')

            while not leave_check.check_for('leave'):
                time.sleep(2)

            coliseum_bot.print('Battle ended. Leaving.')
            leave_check.click()
            time.sleep(10)

    coliseum_bot.set_cooldown_time()
    game_control.back_to_main()


coliseum_bot.set_routine(coliseum_bot_routine)