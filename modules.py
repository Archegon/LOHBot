import time
from save import module_f


class Module:
    instances = []

    def __init__(self, name, cooldown=0, start_only=False):
        self.__class__.instances.append(self)
        self.cooldown = cooldown
        self.cooldown_end = 0
        self.name = name
        self.start_only = start_only
        self.routine = None
        self.state = None
        self.enable = True

    def load(self):
        save_file = module_f.load()
        self.cooldown_end = save_file[self.name]['cooldown_end']
        self.enable = save_file[self.name]['enable']
        self.print("Loaded data")

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

    def set_cooldown_time(self):
        self.cooldown_end = time.time() + self.cooldown

    def run_routine(self):
        self.print("Starting routine!")
        self.routine()
        self.save()
        self.print("Routine Ended!")

    # Check if the cooldown time has lapsed.
    def run(self):
        if self.start_only is False:
            if time.time() >= self.cooldown_end:
                return True
            else:
                return False

    def run_start(self):
        if self.start_only:
            if time.time() >= self.cooldown_end:
                return True
            else:
                return False


class ModuleManager:
    def __init__(self):
        self.modules = Module.instances

    # Run all enabled modules, depending on their cooldown timers.
    def run(self):
        for module in self.modules:
            if module.run():
                module.run_routine()

    def load(self):
        for module in self.modules:
            module.load()

    def save(self):
        for module in self.modules:
            module.save()
