def are_adjacent(a ,b):
    return a[0] - b[0] in (-1, 0, 1) and  a[1] - b[1] in (-1, 0, 1)

def special_move(t, o, pos):
    return (t[-1-pos][0] - o[-1-pos][0], t[-1-pos][1] - o[-1-pos][1])

def simplify(t, pos, x, y):
    if t[-pos][0] == t[-1 - pos][0] and t[-pos][1] == t[-1 - pos][1] + 2:
        return 0, 1
    if t[-pos][0] == t[-1 - pos][0] and t[-pos][1] == t[-1 - pos][1] - 2:
        return 0, -1
    if t[-pos][1] == t[-1 - pos][1] and t[-pos][0] == t[-1 - pos][0] + 2:
        return 1, 0
    if t[-pos][1] == t[-1 - pos][1] and t[-pos][0] == t[-1 - pos][0] - 2:
        return -1, 0
    return x, y

def follow(tail, coords, steps, v):
    old_tail = tail[:]
    m = 0
    while m < steps:
        pos = 1
        tail[-pos] = (tail[-pos][0] + coords[0], tail[-pos][1] + coords[1])
        while pos < len(tail):
            if not are_adjacent(tail[-pos], tail[-1 - pos]):
                x, y = special_move(tail, old_tail, pos - 1)
                if x != 0 and y != 0:
                    x, y = simplify(tail, pos, x, y)
                    tail[-1 - pos] = (tail[-1 - pos][0] + x, tail[-1 - pos][1] + y)
                else:
                    tail[-1 - pos] = (old_tail[-pos][0], old_tail[-pos][1])
            pos += 1
        m += 1
        old_tail = tail[:]
        v.append(tail[0])
    return old_tail

def simulate_rope(rope_size, moves):
    tail = [(0, 0)] * rope_size

    visited = [(0, 0)]

    for move in moves:
        if move[0] == 'R': tail = follow(tail, (1, 0), int(move[1]), visited)
        if move[0] == 'L': tail = follow(tail, (-1, 0), int(move[1]), visited)
        if move[0] == 'U': tail = follow(tail, (0, 1), int(move[1]), visited)
        if move[0] == 'D': tail = follow(tail, (0, -1), int(move[1]), visited)

    return set(visited)


moves = [x.split(" ") for x in open("day09.txt").read().split("\n")]
print(len(simulate_rope(2, moves)))