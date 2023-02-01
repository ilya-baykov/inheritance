class H:
    pass


class D(H):
    pass


class E(H):
    pass


class F(H):
    pass


class G(H):
    pass


class B(D, E):
    pass


class C(F, G):
    pass


class A(B, C):
    pass


def mro_function(cls):
    print(*[c.__name__ for c in cls.mro()], sep=" -> ")


mro_function(A)
