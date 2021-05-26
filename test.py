import re
import os
import sys
import time

read = 'A B~ C/// D *E'
read = re.sub(r"[^a-zA-Z0-9 ]+", '', read)


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


if __name__ == "__main__":
    print(read)
    time.sleep(2)
    restart_program()
