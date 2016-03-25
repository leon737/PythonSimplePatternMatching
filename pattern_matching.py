
def match(v):
    return pattern_matching(v)

def myempty(*h):
    return h[0] is None


class pattern_matching:

    def __init__(self, v):
        self.v = v
        self.matched = False

    def __or__(self, other):
        if self.matched: return self
        if isinstance(other, tuple):
            if type(self.v) == type(other[0]) and self.v == other[0]:
                self.set(other[1])
            if callable(other[0]):
                p = self.parse_list()
                try:
                    if other[0](*p):
                        self.set(other[1])
                except:
                    pass
            if isinstance(other[0], tuple) and len(other[0]) == 0:
                self.set(other[1])
        return self

    def set(self, f):
        if callable(f):
            if isinstance(self.v, list):
                if len(self.v) > 0:
                    self.v = f(self.v[0] if len(self.v) > 0 else None, self.v[1:] if len(self.v) > 1 else [])
                else:
                    return
            else:
                self.v = f(self.v)
        else:
            self.v = f
        self.matched = True

    def parse_list(self):
        if isinstance(self.v, list):
            if len(self.v) == 0:
                return [None, None]
            elif len(self.v) == 1:
                return (self.v[0], [])
            else:
                return (self.v[0], self.v[1:])
        else:
            return self.v

    def __str__(self):
        return str(self.v) if self.matched else str(None)

    def __call__(self, *args, **kwargs):
        return self.v if self.matched else None