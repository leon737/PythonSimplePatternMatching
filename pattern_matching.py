def match(v=None):
    return pattern_matching(v)

def empty(*h):
    return h[0] is None


class pattern_matching:

    def __init__(self, v=None):
        self.v = v
        self.patterns = []

    def __or__(self, other):
        self.patterns.append(other)
        return self

    def do(self, v):
        for p in self.patterns:
            if isinstance(p, tuple):
                if self._check_simple(p[0], v):
                    return self._set(p[1], v)
                if callable(p[0]):
                    f = self._parse_list(v)
                    try:
                        if p[0](*f):
                            return self._set(p[1], v)
                    except:
                        pass
                if isinstance(p[0], tuple) and len(p[0]) == 0:
                    return self._set(p[1], v)
        return None

    def _check_simple(self, p, v):
        if isinstance(p, list):
            return self._any(lambda x: self._check_simple(x, v), p)
        if (type(p) == type and type(v) == p) or (type(self.v) == type(p) and v == p):
            return True

        return False

    def _set(self, f, v):
        if callable(f):
            if isinstance(v, list):
                if len(v) > 0:
                    return f(self.v[0] if len(self.v) > 0 else None, self.v[1:] if len(self.v) > 1 else [])
                else:
                    return None
            else:
                return f(self.v)
        else:
            return f

    def _parse_list(self, v):
        if isinstance(v, list):
            if len(v) == 0:
                return [None, None]
            elif len(v) == 1:
                return (v[0], [])
            else:
                return (v[0], v[1:])
        else:
            return (v,)

    def _any(self, p, l):
        for x in l:
            if p(x):
                return True
        return False

    def __call__(self, *args, **kwargs):
        if len(args) > 0: self.v = args[0]
        return self.do(self.v)