import concurrent.futures
import os
import time
from game import loh
from routines.routines_setup import module_manager


def setup():
    print('Starting...')
    module_manager.load()
    module_manager.run_start()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(check_app_exit)

        try:
            executor.submit(app_running)
        except:
            print("app except raised")


def app_running():
    while loh.app.is_process_running():
        module_manager.run()


def check_app_exit():
    while loh.app.is_process_running():
        pass

    print("Process exited")
    print("Restarting in 5 seconds...")
    time.sleep(5)
    os.system('loader.py')


setup()
