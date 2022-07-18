#!/usr/bin/python3

import heapq as hq

def maximum_overlapping_intervals(S, E):
    ## Sort by start time
    S, E = list(zip(*sorted(zip(S, E))))
    pq = []
    count = 0
    for i, s in enumerate(S):
        if pq and pq[0] < s:
            _ = hq.heapreplace(pq, E[i])
        else:
            hq.heappush(pq, E[i])
        count = max(count, len(pq))
    return count

if __name__ == '__main__':
    pass