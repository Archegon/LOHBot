from game import game_control
from modules import Module
from routines import routines_setup

# Auto Restart
auto_restart = Module('Auto Restart', 3600, load_data=False)
auto_restart.set_cooldown_time()


def auto_restart_routine():
    routines_setup.module_manager.stop = True
    game_control.kill_program()


auto_restart.set_routine(auto_restart_routine)
