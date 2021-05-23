from game import game_control
from modules import ModuleManager
from position import Region, Point

module_manager = ModuleManager()

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

