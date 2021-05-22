import os
import time
from modules import Module
from game import loh
from routines import module_manager

AUTO_RESTART = True


def setup():
    print('Starting...')
    Module.instances = []
    module_manager.load()
    module_manager.run_start()

    while loh.app.is_process_running():
        module_manager.run()

    if AUTO_RESTART:
        loh.app.wait_for_process_exit(timeout=20)
        print("Process exited")
        time.sleep(10)
        print("Restarting...")
        os.system('loader.py')
        setup()


setup()
