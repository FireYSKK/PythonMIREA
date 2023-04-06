def get_inheritance(cls):
    return [cls.__name__] + (get_inheritance(cls.__base__) if cls.__base__ else list())


print(*get_inheritance(OSError), sep=' -> ')
