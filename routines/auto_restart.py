from game import game_control
from modules import Module
from routines.routines_setup import module_manager

# Auto Restart
auto_restart = Module('Auto Restart', 7200, load_data=False)
auto_restart.set_cooldown_time()


def auto_restart_routine():
    module_manager.stop = True
    game_control.kill_program()


auto_restart.set_routine(auto_restart_routine)
