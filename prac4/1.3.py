class A:
    pass


class B(A):
    pass


# class C(A, B):
class C(B):
    pass


c = C
