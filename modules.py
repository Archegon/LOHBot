import time
from save import Savefile
from game import loh

module_save = 'saves/module_save.json'
module_f = Savefile(module_save)


class Module:
    instances = {}
    start_time = time.time()

    def __init__(self, name, cooldown=0, enable=True, start_only=False, load_data=True, standalone=False):
        temp_dict = {
            name: self
        }
        self.__class__.instances.update(temp_dict)
        self.cooldown = cooldown
        self.cooldown_end = 0
        self.load_data = load_data
        self.name = name
        self.start_only = start_only
        self.standalone = standalone
        self.routine = None
        self.enable = enable
        self.state = None

    def load(self):
        if self.load_data:
            save_file = module_f.load()

            try:
                self.cooldown_end = save_file[self.name]['cooldown_end']
                self.enable = save_file[self.name]['enable']
                self.print("Loaded data")
            except KeyError:
                self.print('No save found')

    def save(self):
        save_dict = {
            self.name: {
                'cooldown_end': self.cooldown_end,
                'enable': self.enable
            }
        }

        module_f.update(save_dict)
        self.print("Saved data")

    def get_name(self):
        name = self.name + ":"
        return name

    # To set the module current state. Trackable and logging
    def set_state(self, state):
        self.state = state
        print(self.get_name(), state)

    def print(self, txt):
        print(self.get_name(), txt)

    def set_routine(self, function):
        self.routine = function

    def set_cooldown_time(self, cooldown=None):
        if cooldown is None:
            self.cooldown_end = time.time() + self.cooldown
        else:
            self.cooldown_end = time.time() + cooldown

        self.print(f'Set cooldown time to {self.cooldown_end}')

    def run_routine(self):
        print("=========================================")
        self.print("Starting routine!")
        Module.start_time = time.time()
        loh.b_window.set_focus()
        self.routine()
        self.save()
        Module.start_time = None
        self.print("Routine Ended!")
        print("=========================================")

    # Check if the cooldown time has lapsed.
    def run(self):
        if not self.start_only and self.enable and not self.standalone:
            if time.time() >= self.cooldown_end:
                return True
            else:
                return False

    def run_start(self):
        if self.start_only and self.enable is True:
            if time.time() >= self.cooldown_end:
                return True
            else:
                return False


class ModuleManager:
    def __init__(self):
        self.modules = Module.instances
        self.stop = False
        self.time_out = 600

    # Run all enabled modules, depending on their cooldown timers.
    def run(self, module_name=None):
        if module_name is None:
            for key in self.modules:
                if not self.stop:
                    if self.modules[key].run():
                        self.modules[key].run_routine()
        else:
            self.modules[module_name].run_routine()

    def run_start(self):
        if not self.stop:
            for key in self.modules:
                if self.modules[key].run_start():
                    self.modules[key].run_routine()

    def check_stuck(self):
        # Use in a separate thread only
        if not self.stop:
            while True:
                if time.time() - Module.start_time >= self.time_out:
                    print("STUCK!")
                    return True
                time.sleep(5)

    def load(self):
        for key in self.modules:
            self.modules[key].load()

    def save(self):
        for key in self.modules:
            self.modules[key].save()
