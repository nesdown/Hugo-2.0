import platform

def get_system():
    system = platform.system() # Вернет тип системы.
    bit = platform.architecture() # Вернет кортеж, где разрядность — нулевой элемент

    print(system)
    print(bit[0])

    return system
