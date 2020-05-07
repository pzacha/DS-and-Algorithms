class tripple_step:
    def __init__(self, n):
        self.n = n
        self.number = 0

    def ts_rec(self, i=0):
        self.number += 1
        if self.n - i >= 3:
            self.ts_rec(i + 1)
            self.ts_rec(i + 2)
            self.ts_rec(i + 3)
        elif self.n - 1 == 2:
            self.ts_rec(i + 1)
            self.ts_rec(i + 2)
        elif self.n - 1 == 1:
            self.ts_rec(i + 1)

        return self.number


ts = tripple_step(4)
print(ts.ts_rec())
