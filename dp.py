from functools import lru_cache
def optimal_events(ev):
    @lru_cache(maxsize=None)
    def mevents(t, pos):
        return ((t,) if t >= 1 and ev[t-1] == pos else ()) + (max(
                tuple(mevents(t + 1, p)
                    for p in range(pos - 1, pos + 2) if len(ev) - t >= abs(p - ev[-1])
                ), key=len) if t != len(ev) else ())
    return mevents(0, 0)
