import time
from modules import Module
from position import Region

# Auto Primeval Halls
auto_primeval = Module('Auto Primeval', 7200, enable=False)


def auto_primeval_routine():
    energy_check = Region(1496, 841, 746, 12, 904, 47)
    battle_outcome_check = Region(1496, 841, 682, 736, 808, 788)
    next_b = 0

    energy = energy_check.read()[0][1]
    energy = energy[:energy.find('/')]
    energy = int(energy.replace(',', ''))
    energy_required = 10000

    print(energy)
    time.sleep(10)


auto_primeval.set_routine(auto_primeval_routine)
