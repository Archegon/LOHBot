import time
from modules import Module
from position import Region, Point
from game import game_control


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