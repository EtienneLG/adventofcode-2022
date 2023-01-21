from copy import deepcopy

data = [x.split("\n") for x in open("day05.txt").read().split("\n\n")]

crates = [[] for _ in range(len([x for x in data[0][-1] if x.isdigit()]))]
for i in data[0]:
    for j in range(len(i)):
        if i[j].isalpha():
            crates[j // 4].append(i[j])

orders = [[int(y) for y in x.split(" ") if y.isdigit()] for x in data[1]]

def one_by_one(o, c):
    for order in o:
        c[order[2] - 1] = list(reversed(c[order[1] - 1][:order[0]])) + c[order[2] - 1]
        del c[order[1] - 1][:order[0]]
    return c

def stack_by_stack(o, c):
    for order in o:
        c[order[2] - 1] = c[order[1] - 1][:order[0]] + c[order[2] - 1]
        del c[order[1] - 1][:order[0]]
    return c

print("".join([c[0] for c in one_by_one(orders, deepcopy(crates))]))
print("".join([c[0] for c in stack_by_stack(orders, deepcopy(crates))]))