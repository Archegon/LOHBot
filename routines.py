from modules import Module
from position import Region
from game import game_control


main_page_check = Region(1503, 845, 1345, 798, 1431, 825)
game_control.add_page('Main', 'world', main_page_check)
game_control.at_page('Main')

# Fairy Collector
fairy = Module('Fairy Collector', 1800)


def fairy_routine():
    pass


fairy.set_routine(fairy_routine())

