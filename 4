from collections import deque

def hanoi(n):
    s = (0,) * n                      # state: s[k] = peg of disk k (0 = smallest)
    q, seen = deque([(s, [])]), {s}   # BFS queue of (state, moves so far)
    while q:
        s, p = q.popleft()
        if s == (2,) * n:             # goal: all disks on peg C
            return p
        for k in range(n):
            for b in range(3):
                if b != s[k] and all(s[m] not in (s[k], b) for m in range(k)):
                    t = s[:k] + (b,) + s[k+1:]
                    if t not in seen:
                        seen.add(t)
                        q.append((t, p + [(k + 1, s[k], b)]))

for d, a, b in hanoi(3):
    print(f"Move disk {d} from {'ABC'[a]} to {'ABC'[b]}")
