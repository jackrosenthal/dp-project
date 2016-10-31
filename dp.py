from functools import lru_cache
ev = [1, -4, -1, 4, 5, -4, 6, 7, -2]
def evtuple(t, pos):
    return (t,) if t >= 1 and ev[t-1] == pos else tuple()

@lru_cache(maxsize=None)
def mevents(t, pos):
    if t == len(ev):
        return evtuple(t, pos)
    return evtuple(t, pos) + max(
            tuple(mevents(t + 1, p)
                for p in range(pos - 1, pos + 2) if len(ev) - t >= abs(p - ev[-1])
            ),
            key=len)
