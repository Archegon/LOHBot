import concurrent.futures
import os
import time
from game import loh
from routines.routines_setup import module_manager


def setup():
    module_manager.load()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        def trackers():
            while True:
                time.sleep(3)
                if not loh.app.is_process_running():
                    return 'app ended'

                if module_manager.check_stuck():
                    return 'module stuck'

        def process_result(future):
            if future.result() == 'module stuck':
                loh.kill()

            app_restart()

        def app_restart():
            print("Restarting in 5 seconds...")
            module_manager.stop = True
            time.sleep(5)
            os.system('loader.py')

        trackers_thread = executor.submit(trackers)
        trackers_thread.add_done_callback(process_result)

        try:
            module_manager.run_start()
            module_manager.run()
        except:
            print("module_thread exception raised")
            loh.kill()


setup()
print("Program Exited")
