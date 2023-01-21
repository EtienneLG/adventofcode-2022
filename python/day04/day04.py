data = [[[int(k) for k in j.split("-")] for j in i.split(",")] for i in open("day04.txt").read().split("\n")]

def fully_countain(pairs):
    return (pairs[0][0] >= pairs[1][0] and pairs[0][1] <= pairs[1][1]) or (pairs[1][0] >= pairs[0][0] and pairs[1][1] <= pairs[0][1])

def overlap(pairs):
    return len(set(range(pairs[0][0], pairs[0][1]+1)) & set(range(pairs[1][0], pairs[1][1]+1))) > 0

part_one = [x for x in data if fully_countain(x)]
part_two = [x for x in data if overlap(x)]

print(len(part_one))
print(len(part_two))