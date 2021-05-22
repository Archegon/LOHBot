import time
from modules import Module, ModuleManager
from position import Region, Point
from game import game_control

main_page_check = Region(1503, 845, 1345, 798, 1431, 825)
game_control.add_page('Main', 'world', main_page_check)
main_home_check = Region(1503, 845, 1022, 139, 1123, 170)
game_control.add_page('Main_Home', 'feats', main_home_check)
main_mystic_check = Region(1503, 845, 664, 239, 762, 278)
game_control.add_page('Main_Mystic', 'mystic', main_mystic_check)

# Drag to Main_mystic
# Set up drag start and end point
# Drag to mystic.
mystic_drag_start = Point(1503, 845, 1446, 334)
mystic_drag_end = Point(1503, 845, 67, 348)
game_control.add_drag('HomeToMystic', mystic_drag_start, mystic_drag_end)

# Drag to home.
home_drag_start = Point(1503, 845, 27, 81)
home_drag_end = Point(1503, 845, 1470, 90)
game_control.add_drag('MysticToHome', home_drag_start, home_drag_end)

# Set MAIN PAGE
quit_confirm_check = Region(1681, 945, 620, 421, 738, 466)
game_control.set_quit_confirmation('are you', quit_confirm_check)

# Login Module
login = Module('Login', start_only=True)


def login_routine():
    touch_to_start = Region(1637, 920, 582, 720, 1057, 820)
    touch_b = Point(1637, 920, 616, 517)

    while not game_control.at_page('Main'):
        if touch_to_start.check_for('touch to start'):
            touch_b.click()


login.set_routine(login_routine)

# Fairy Collector
fairy = Module('Fairy Collector', 1800)


def fairy_routine():
    # Set up button and region.
    fairy_status = Region(1514, 852, 721, 413, 816, 467)
    fairy_b = Point(1646, 926, 811, 524)  # Collect fairy gift button

    # Check if on home page.
    if game_control.at_page('Main_Home'):
        # Check if collectable.
        # If empty means collectable.
        if fairy_status.check_empty():
            fairy_b.click()
            fairy.print("Fairy gift collected")
            fairy.set_cooldown_time()
            time.sleep(1)
            game_control.back()
        else:
            fairy.print("No gift found.")


fairy.set_routine(fairy_routine)

# Mystic Shop
mystic_shop = Module('Mystic Shop', 2400)


def mystic_shop_routine():
    # Set up button and region
    mystic_shop_b = Point(1502, 845, 704, 257)

    mystic_purchase_b = Region(1502, 845, 519, 424, 993, 778)
    mystic_item1_status = Region(1502, 845, 659, 526, 747, 571)
    mystic_item2_status = Region(1502, 845, 958, 619, 1049, 669)
    mystic_item_sold_status1 = Region(1502, 845, 618, 471, 728, 520)
    mystic_item_sold_status2 = Region(1681, 945, 993, 632, 1149, 677)

    game_control.drag('HomeToMystic')
    mystic_shop_b.click()

    if not mystic_item_sold_status1.check_for('Sold'):
        if mystic_item1_status.check_for('Free'):
            mystic_item1_status.click()
            mystic_purchase_b.locate_click('Free')
            time.sleep(35)
            game_control.back()

    if not mystic_item_sold_status2.check_for('Sold'):
        if mystic_item2_status.check_for('Free'):
            mystic_item2_status.click()
            mystic_purchase_b.locate_click('Free')
            time.sleep(35)
            game_control.back()

    mystic_shop.set_cooldown_time()
    time.sleep(1)
    game_control.back()
    time.sleep(1)
    game_control.drag('MysticToHome')


mystic_shop.set_routine(mystic_shop_routine)

# Alliance Collector
alliance = Module('Alliance Collector', 900)


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

# Feats Collector
feats_collector = Module('Feats Collector', 1800)


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

    game_control.add_drag('WorldToColiseum', coliseum_drag_start, coliseum_drag_end)

    world_b.click()
    time.sleep(2)
    game_control.drag('WorldToColiseum')
    coliseum_check.locate_click('coliseum')
    time.sleep(5)
    reward_b.click()
    reward_collect_b.click()
    game_control.back()

    while True:
        enemy_b.click()
        enemy_enter_b.click()
        time.sleep(10)

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


module_manager = ModuleManager()
