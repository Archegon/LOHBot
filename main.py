import concurrent.futures
import os
import time
from game import loh
from routines.routines_setup import module_manager


def setup():
    module_manager.load()
    module_manager.run_start()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        module_thread = executor.submit(run_modules)
        # module_check_stuck_thread = executor.submit(module_manager.check_stuck())

        try:
            module_thread.result()
        except:
            print("module_thread exception raised")
            app_restart()


def run_modules():
    while True:
        module_manager.run()


def app_restart():
    if not loh.app.is_process_running():
        print("Restarting in 5 seconds...")
        time.sleep(5)
        os.system('loader.py')


setup()
