class Sq:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mult(self, c):
        sum = self.a + self.b + c.a + c.b
        return sum


class Sz(Sq):
    def show(self):
        print(self.a)


def show_sum(obj1, obj2):
    print(obj1.mult(obj2))


msk = Sq(45, 60)
spb = Sz(87, 9)
ekb = Sq(188, 6587)
spb.show()

show_sum(msk, spb)
print(msk.mult(spb))
print(msk.mult(ekb))
