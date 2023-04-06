class Sample:
    def __init__(self, name):
        self.name = name

    def call(self):
        print(self.name, "called successfully")


sample = Sample("Class_sample")
method_to_call = input()
eval("sample." + method_to_call + "()")
