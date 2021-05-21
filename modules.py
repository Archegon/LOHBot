import time
from save import module_f


class Module:
    instances = []

    def __init__(self, name, cooldown):
        self.__class__.instances.append(self)
        self.cooldown = cooldown
        self.cooldown_end = 0
        self.name = name
        self.routine = None
        self.state = None
        self.enable = True

    def load(self):
        save_file = module_f.load()
        self.cooldown_end = save_file[self.name]['cooldown_end']
        self.enable = save_file[self.name]['enable']
        print(self.get_name(), "Loaded data")

    def save(self):
        save_dict = {
            self.name: {
                'cooldown_end': self.cooldown_end,
                'enable': self.enable
            }
        }

        module_f.update(save_dict)
        print(self.get_name(), "Saved data")

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

    def run_routine(self):
        print(self.get_name(), "Starting routine!")
        self.routine()

        # Set new cooldown time.
        self.cooldown_end = time.time() + self.cooldown
        self.save()
        print(self.get_name(), "Routine Ended!")

    # Check if the cooldown time has lapsed.
    def run(self):
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
