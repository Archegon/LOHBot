from routines import module_manager
from game import loh


AUTO_RESTART = False


def setup():
    module_manager.load()

    while loh.app.is_process_running():
        module_manager.run()
    else:
        print("Application ended.")

        if AUTO_RESTART:
            loh.app.wait_for_process_exit(timeout=20)
            print("Process exited")
            setup()


setup()
