import concurrent.futures
import os
import time
from game import loh
from routines.routines_setup import module_manager


def setup():
    module_manager.load()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        module_stuck_thread = executor.submit(module_manager.check_stuck)
        module_stuck_thread.add_done_callback(stuck)
        module_manager.run_start()
        module_thread = executor.submit(run_modules)

        try:
            module_thread.result()
        except:
            print("module_thread exception raised")
            app_restart()


def run_modules():
    while True:
        module_manager.run()


def stuck(future):
    if future.result():
        print('Module stuck. Exiting.')
        loh.kill()
        app_restart()


def app_restart():
    if not loh.app.is_process_running():
        print("Restarting in 5 seconds...")
        time.sleep(5)
        os.system('loader.py')


setup()
