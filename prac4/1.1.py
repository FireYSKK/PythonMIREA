class Sample:
    def __init__(self):
        pass

    def method1(self):
        pass

    def method2(self):
        pass


def get_attrs(class_instance):
    return [k for k in class_instance.__dict__.keys()
            if not k.startswith('__') and not k.endswith('__')]


print(get_attrs(Sample))
